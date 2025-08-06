
"""
src/processing/data_loader.py
DICOM数据加载和处理模块
"""
import numpy as np
import pydicom

def load_dicom_file(file_path):
    """加载DICOM格式的心脏MRI影像"""
    dicom_data = pydicom.dcmread(file_path)
    return dicom_data.pixel_array.astype(np.float32)

def normalize_image(image):
    """标准化MRI图像数据"""
    return (image - np.min(image)) / (np.max(image) - np.min(image))

def get_dicom_metadata(file_path):
    """提取DICOM文件元数据"""
    dicom_data = pydicom.dcmread(file_path)
    return {
        'patient_id': getattr(dicom_data, 'PatientID', 'N/A'),
        'study_date': getattr(dicom_data, 'StudyDate', 'N/A'),
        'pixel_spacing': getattr(dicom_data, 'PixelSpacing', [1.0, 1.0])
    }
