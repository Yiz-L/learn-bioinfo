# 成年人BMI计算
height = float(input("请输入您的身高（米）："))
weight = float(input("请输入您的体重（千克）："))
BMI = weight / (height ** 2)
print("您的BMI为:"+str(BMI))
