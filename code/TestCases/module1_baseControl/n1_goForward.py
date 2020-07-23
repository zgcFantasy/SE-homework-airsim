# 油门功能测试，即是否可以加速

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

# step2 是否正常加速
time.sleep(3)
if client.getCarState().speed > speed:
    print("加速成功")
    speed = client.getCarState().speed
else:
    print("加速失败")
    client.enableApiControl(False)

# 回到手动控制
client.enableApiControl(False)
