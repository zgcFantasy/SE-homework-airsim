
# 刹车功能测试
import TestCases.myFunction as MyFun
import time

[client, car_controls, car_state] = MyFun.initAirSim()

# 先加速
car_controls.throttle = 1
client.setCarControls(car_controls)

time.sleep(5)

# 停止加速，开始刹车
car_controls.brake = 1
car_controls.throttle = 0
print("开始刹车")
client.setCarControls(car_controls)


while True:
    time2 = time.clock()
    if client.getCarState().speed == 0 :
        print("刹车成功")
        break

client.enableApiControl(False)
