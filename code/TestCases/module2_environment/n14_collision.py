import time
import TestCases.myFunction as MyFun

[client, car_controls, car_state] = MyFun.initAirSim()

# 开启油门
car_controls.throttle = 1
client.setCarControls(car_controls)
# 一直跑，直到与物体碰撞

while True:
    if client.simGetCollisionInfo().has_collided:
        print("车辆碰到障碍物")
        print(client.simGetCollisionInfo())
        break
client.enableApiControl(False)
