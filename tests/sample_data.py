import numpy as np

def generate_sample_mri():
    """生成模拟心脏MRI图像"""
    img = np.zeros((256, 256))
    
    # 左心室
    cv2.circle(img, (128, 128), 40, 0.8, -1)
    # 心肌
    cv2.circle(img, (128, 128), 55, 0.5, 5)
    
    return img
