# 倒车测试

import TestCases.myFunction as MyFun
import time

[client, car_controls, car_state] = MyFun.initAirSim()

car_controls.is_manual_gear = True
car_controls.manual_gear = -1
car_controls.throttle = 1
client.setCarControls(car_controls)

time.sleep(5)

if client.getCarState().gear == -1 and client.getCarState().speed < 0:
    print("倒车成功")
client.enableApiControl(False)
