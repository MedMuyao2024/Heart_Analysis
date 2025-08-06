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
心脏MRI标准配置参数
"""
import numpy as np

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

# 计算参数
ANALYSIS = {
    'ejection_fraction_range': (55, 70),  # 正常射血分数范围
    'wall_thickness_range': (5, 10)       # 正常室壁厚度(mm)
}
