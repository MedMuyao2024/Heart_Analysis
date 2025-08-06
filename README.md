# 心脏影像分析项目 ❤️
> 基于人工智能的心脏MRI诊断工具

## 核心功能
- [ ] 左心室自动分割
- [ ] 心肌异常检测
- [ ] 血流动力学模拟

## 数据源
![AMRG心脏图谱](https://med.upenn.edu/cbica/amrg-cardiac-atlas/logo.png)
使用公开数据集：[AMRG Cardiac Atlas](https://www.med.upenn.edu/cbica/amrg-cardiac-atlas/)
## 💻 使用示例
```python
from src.image_processor import HeartProcessor

# 加载图像
processor = HeartProcessor("data/sample/patient01.dcm")

# 检测心室
ventricle_mask = processor.detect_ventricles()
```

## 📊 项目结构
```
心脏影像分析项目/
├── config/               # 配置参数
│   └── imaging_params.py
├── data/                 # 影像数据
├── src/                  # 源代码
│   ├── data_loader.py    # DICOM加载器
│   └── image_processor.py # 核心处理器
├── tests/                # 测试模块
└── README.md
