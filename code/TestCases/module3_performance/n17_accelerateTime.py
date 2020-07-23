import time
import TestCases.myFunction as MyFun
# 百公里加速用时
[client, car_controls, car_state] = MyFun.initAirSim()

# 开启油门
car_controls.throttle = 1
client.setCarControls(car_controls)
t1 = time.clock()

# 百公里加速
while True:
    if client.getCarState().speed * 3.6 >= 100:
        t2 = time.clock()
        print("百公里加速用时：", t2 - t1)
        break
client.enableApiControl(False)
