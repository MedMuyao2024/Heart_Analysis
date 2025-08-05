import monai
model = monai.networks.nets.FlexibleUNet(
    in_channels=1, 
    out_channels=3,  # 左室/心肌/背景
    backbone="efficientnet-b3"
)
if __name__ == "__main__":
    print("心脏分割模型初始化成功！")
    print(f"模型结构: {model}")
  
