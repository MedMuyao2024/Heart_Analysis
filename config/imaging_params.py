"""
心脏MRI成像参数配置
"""
# 像素物理尺寸 (mm)
PIXEL_SPACING = {
    'default': (0.8, 0.8),
    'high_res': (0.5, 0.5)
}

# 心脏期相标签
CARDIAC_PHASES = ['ED', 'ES']
"""
config/imaging_params.py
心脏MRI成像参数配置 - 重建版
"""
# 图像处理参数
PREPROCESSING = {
    'normalization_range': (0, 1),
    'target_size': (256, 256),
    'crop_margin': 20
}

# 心脏分割参数
SEGMENTATION = {
    'ventricle_threshold': 0.45,
    'myocardium_threshold': 0.3
}

# 新增设备兼容参数
DEVICE_PROFILES = {
    "GE_1.5T": {"TR": 35.0, "TE": 2.5},
    "Siemens_3T": {"TR": 40.0, "TE": 1.8}
}
