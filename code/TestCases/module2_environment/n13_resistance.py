# 阻力环境测试

import time
import TestCases.myFunction as MyFun

[client, car_controls, car_state] = MyFun.initAirSim()

# 开启油门
car_controls.throttle = 1
client.setCarControls(car_controls)
# step1 启动，等待1s
time.sleep(1)

speed = client.getCarState().speed
if speed > 0:
    print("启动成功")
else:
    print("启动太慢/失败")
    client.enableApiControl(False)

time.sleep(5)

# 关闭油门
car_controls.throttle = 0
speed = client.getCarState().speed
client.setCarControls(car_controls)
if speed > client.getCarState().speed:
    print("不踩油门时会自动减速")
else:
    print("该环境没有阻力")

while True:
    if client.getCarState().speed == 0:
        print("汽车已停")
        break
# 回到手动控制
client.enableApiControl(False)
