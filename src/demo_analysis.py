def calculate_ef(edv, esv):  # 统一函数名和使用英文逗号
    """计算射血分数(左心室)"""
    stroke_volume = edv - esv  # 每搏输出量
    return (stroke_volume / edv) * 100  # EF = (EDV-ESV)/EDV * 100%

# 示例测试数据
if __name__ == "__main__":
    edv = 150  # 舒张末期容积(ml)
    esv = 60   # 收缩末期容积(ml)
    
    # 格式化输出 (.1f表示保留1位小数)
    print(f"左心室射血分数(LVEF): {calculate_ef(edv, esv):.1f}%") 
