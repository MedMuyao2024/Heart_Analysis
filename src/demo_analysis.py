# 心脏功能快速分析演示
def calculate_ef(edv, esv):
    """计算射血分数 (医学黄金指标)"""
    return (edv - esv) / edv * 100

# 示例：正常心脏数据
edv = 150  # 舒张末期容积(ml)
esv = 60   # 收缩末期容积(ml)
print(f"左心室射血分数(LVEF)：{calculate_ef(edv, esv):.1f}%")
