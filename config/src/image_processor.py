"""
核心图像处理引擎
"""
import numpy as np
from .data_loader import load_dicom_file
from config.imaging_params import PREPROCESSING

class HeartProcessor:
    def __init__(self, dicom_path):
        self.raw_image = load_dicom_file(dicom_path)
        self.processed_image = self.preprocess()
        
    def preprocess(self):
        """DICOM图像标准化处理"""
        # 1. 像素值归一化
        img = (self.raw_image - np.min(self.raw_image)) / (np.max(self.raw_image) - np.min(self.raw_image))
        
        # 2. 尺寸调整
        target_size = PREPROCESSING['target_size']
        if img.shape != target_size:
            # 简化的调整方法 (实际应使用插值)
            img = img[:target_size[0], :target_size[1]]
        
        return img
    
    def detect_ventricles(self):
        """简易心室检测方法（用于原型开发）"""
        # 基于阈值的检测
        threshold = 0.5 * np.max(self.processed_image)
        return self.processed_image > threshold
