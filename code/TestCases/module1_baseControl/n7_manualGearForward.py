# 手动档测试

import TestCases.myFunction as MyFun
import time

[client, car_controls, car_state] = MyFun.initAirSim()

car_controls.is_manual_gear = True
car_controls.manual_gear = 0
car_controls.throttle = 1
client.setCarControls(car_controls)
speed = client.getCarState().speed
# 从 0 开始，每次只提升一档，看车速是否会超过临界值
while True:
    time.sleep(5)
    if client.getCarState().speed - speed > 0.1:
        speed = client.getCarState().speed
    else:
        speed = client.getCarState().speed
        print("gear = ", car_controls.manual_gear, " maxspeed = ", speed)
        car_controls.manual_gear += 1
        if car_controls.manual_gear == 6:
            break
        client.setCarControls(car_controls)
client.enableApiControl(False)
