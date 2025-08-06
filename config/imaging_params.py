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
