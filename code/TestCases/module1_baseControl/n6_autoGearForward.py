# 自动档测试

import TestCases.myFunction as MyFun
import time

[client, car_controls, car_state] = MyFun.initAirSim()

car_controls.is_manual_gear = False
car_controls.throttle = 1
client.setCarControls(car_controls)

gear = client.getCarState().gear
speed = client.getCarState().speed
print("gear = ", gear, " speed = ", speed)
# 持续加速，直到获取 5档 的各自速度
while True:
    if gear == client.getCarState().gear - 1:
        speed = client.getCarState().speed
        gear = client.getCarState().gear
        print("gear = ", gear, " speed = ", speed)
        if gear == 5:
            print("5档临界速度已获取，测试结束")
            break

client.enableApiControl(False)
