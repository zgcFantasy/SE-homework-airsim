
# 左后转弯测试
import TestCases.myFunction as MyFun
import time
[client, car_controls, car_state] = MyFun.initAirSim()

car_controls.throttle = 1
car_controls.is_manual_gear = True
car_controls.manual_gear = -1
# 左转弯方向盘打满
car_controls.steering = -1
client.setCarControls(car_controls)

time.sleep(3)
client.enableApiControl(False)