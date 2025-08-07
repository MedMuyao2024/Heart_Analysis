"""
src/demo_analysis.py - 心脏MRI分析主程序 (优化版)
整合了DICOM处理、心室识别、容积计算和射血分数分析功能
"""

import numpy as np
import pydicom
from config.imaging_params import PREPROCESSING
from src.segmentation import UnetModel
from src.image_processor import HeartProcessor
from tests.sample_data import generate_sample_mri  # 测试用模拟数据

def load_dicom_file(file_path):
    """加载DICOM格式的心脏MRI影像"""
    dicom_data = pydicom.dcmread(file_path)
    pixel_array = dicom_data.pixel_array.astype(np.float32)
    
    # 从DICOM头文件中获取关键参数
    pixel_spacing = getattr(dicom_data, 'PixelSpacing', [1.0, 1.0])
    slice_thickness = getattr(dicom_data, 'SliceThickness', 1.0)
    
    return pixel_array, (slice_thickness, pixel_spacing[0], pixel_spacing[1])

def normalize_image(image):
    """标准化MRI图像数据 (0-1范围)"""
    return (image - np.min(image)) / (np.max(image) - np.min(image))

def identify_ventricles(image, use_ai=False):
    """
    识别MRI中的心室区域
    :param use_ai: 是否使用AI模型 (默认使用阈值法)
    """
    if use_ai:
        # AI模型识别
        model = UnetModel(input_shape=(256, 256, 1))
        return model.predict(image[np.newaxis, ..., np.newaxis])[0]
    else:
        # 简易阈值法 (当前使用的临时方案)
        threshold = 0.45 * np.max(image)
        return (image > threshold).astype(np.uint8)

def calculate_volume(mask, voxel_size=(1.0, 1.0, 1.0)):
    """
    根据分割掩码计算心室容积 (单位: mL)
    :param voxel_size: 体素物理尺寸 (厚度, 高度, 宽度) mm/像素
    """
    voxel_count = np.sum(mask)
    # 将mm³转换为mL (1 mL = 1000 mm³)
    return (voxel_count * voxel_size[0] * voxel_size[1] * voxel_size[2]) / 1000

def calculate_ef(edv, esv):
    """
    计算射血分数 (左心室)
    :param edv: 舒张末期容积(mL)
    :param esv: 收缩末期容积(mL)
    :return: 射血分数百分比(%)
    """
    stroke_volume = edv - esv  # 每搏输出量
    return (stroke_volume / edv) * 100 if edv > 0 else 0

def run_analysis():
    """主分析流程"""
    print("=== 心脏MRI分析系统启动 ===")
    
    try:
        # 方法1: 从实际DICOM文件加载数据
        # mri_image, voxel_size = load_dicom_file("data/heart_001.dcm")
        
        # 方法2: 使用测试数据 (当前使用)
        mri_image = generate_sample_mri()
        voxel_size = (8.0, 0.8, 0.8)  # 测试数据体素尺寸
        
        # 标准化处理
        processed_image = normalize_image(mri_image)
        
        print(f"目标图像尺寸: {PREPROCESSING['target_size']}")
        print(f"体素物理尺寸: {voxel_size} mm")
        
        # 初始化AI模型 (配置中)
        # model = UnetModel(input_shape=(256, 256, 1))
        # print("✅ 心脏分割模型加载成功")
        
        # 识别心室区域 (目前使用阈值法)
        ventricle_mask = identify_ventricles(processed_image, use_ai=False)
        
        # 计算心室容积
        edv = calculate_volume(ventricle_mask, voxel_size)
        
        # 简化处理: 收缩末期容积暂设为舒张末期的60%
        esv = 0.6 * edv
        
        # 计算射血分数
        ef = calculate_ef(edv, esv)
        print(f"\n左心室射血分数(LVEF): {ef:.1f}%")
        
        # 可视化结果
        visualize_results(processed_image, ventricle_mask)
        
    except Exception as e:
        print(f"❌ 分析过程中出错: {str(e)}")
        print("请检查: 1. 数据文件路径 2. 依赖库安装")

def visualize_results(image, mask):
    """结果可视化"""
    try:
        import matplotlib.pyplot as plt
        
        # 创建2x2分析面板
        fig, axs = plt.subplots(2, 2, figsize=(12, 10))
        
        # 原始图像
        axs[0, 0].imshow(image, cmap='gray')
        axs[0, 0].set_title("原始MRI影像")
        
        # 分割结果
        axs[0, 1].imshow(mask, cmap='jet')
        axs[0, 1].set_title("心室识别结果")
        
        # 叠加显示
        axs[1, 0].imshow(image, cmap='gray')
        axs[1, 0].imshow(mask, cmap='jet', alpha=0.3)
        axs[1, 0].set_title("影像叠加")
        
        # 功能预留面板
        axs[1, 1].axis('off')
        axs[1, 1].text(0.5, 0.5, "血流模拟分析\n(功能开发中)", 
                       ha='center', va='center', fontsize=12)
        
        plt.tight_layout()
        plt.savefig("results.png")
        print("✅ 分析结果已保存至 results.png")
        plt.show()
        
    except ImportError:
        print("⚠️ 未安装matplotlib，跳过可视化功能")

if __name__ == "__main__":
    run_analysis()
