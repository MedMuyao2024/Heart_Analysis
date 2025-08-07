def validate_ef(calculated_ef):
    """验证射血分数临床可靠性"""
    NORMAL_RANGE = (55, 70)
    if calculated_ef < 40:
        return "重度心功能不全"
    elif 40 <= calculated_ef < 55:
        return "心功能中度受损"
    else:
        return f"心功能正常({calculated_ef}%)"
