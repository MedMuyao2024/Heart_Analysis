# 在现有代码上方添加
import numpy as np
import pydicom

def load_dicom_file(file_path):
    """加载DICOM格式的心脏MRI影像"""
    dicom_data = pydicom.dcmread(file_path)
    return dicom_data.pixel_array.astype(np.float32)

def normalize_image(image):
    """标准化MRI图像数据"""
    return (image - np.min(image)) / (np.max(image) - np.min(image))

def calculate_ef(edv, esv):  # 统一函数名和使用英文逗号
    """计算射血分数(左心室)"""
    stroke_volume = edv - esv  # 每搏输出量
    return (stroke_volume / edv) * 100  # EF = (EDV-ESV)/EDV * 100%

# 修改main部分
if __name__ == "__main__":
    # 加载DICOM文件（替换为实际文件路径）
    mri_image = load_dicom_file("data/heart_001.dcm")
    processed_image = normalize_image(mri_image)
    
    # 识别心室区域
    ventricle_mask = identify_ventricles(processed_image)
    
    # 计算容积（需先知道图像参数）
    pixel_size = (0.8, 0.8, 0.8)  # 示例值，实际应从DICOM头文件获取
    edv = calculate_volume(ventricle_mask, pixel_size)
    
    # TODO: 添加收缩末期处理
    esv = 0.6 * edv  # 临时占位值
    
    # 计算并输出射血分数
    ef = calculate_ef(edv, esv)
    print(f"左心室射血分数(LVEF): {ef:.1f}%")
    
    # 可视化结果（仅在有显示环境下）
    try:
        import matplotlib.pyplot as plt
        plt.imshow(processed_image, cmap='gray')
        plt.imshow(ventricle_mask, cmap='jet', alpha=0.3)
        plt.title("心室识别结果")
        plt.show()
    except ImportError:
        print("注意：未安装matplotlib，跳过可视化")
        
# 在calculate_ef函数下方添加
def identify_ventricles(image):
    """识别MRI中的左右心室（简易阈值法）"""
    # 实际应用应替换为AI模型
    threshold = 0.45 * np.max(image)
    return image > threshold

def calculate_volume(mask, pixel_size=(1.0, 1.0, 1.0)):
    """根据分割掩码计算心室容积"""
    # pixel_size 参数: (厚度, 高度, 宽度) mm/像素
    voxel_count = np.sum(mask)
    return voxel_count * pixel_size[0] * pixel_size[1] * pixel_size[2]
