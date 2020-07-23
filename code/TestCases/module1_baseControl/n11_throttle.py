# 油门测试
# 加速度应可控
import time
import TestCases.myFunction as MyFun

[client, car_controls, car_state] = MyFun.initAirSim()

# 开启油门
car_controls.throttle = 1
client.setCarControls(car_controls)
lastThrottle = car_controls.throttle
aTime = 0
t1 = time.clock()
print("------------油门", car_controls.throttle, "开始启动---------")
while True:
    if client.getCarState().speed >= 5:
        t2 = time.clock()
        print("油门:", car_controls.throttle, "5m/s 加速用时:", t2 - t1)
        print("开始刹车")
        car_controls.brake = 1
        car_controls.throttle = 0
        client.setCarControls(car_controls)
        while True:
            if client.getCarState().speed == 0:
                print("刹车成功")
                break
        car_controls.brake = 0
        lastThrottle -= 0.1
        if lastThrottle - 0.4 < 0.01:
            break
        if t2 - t1 < aTime:
            print("油门开关异常，测试结束")
            break
        else:
            aTime = t2 - t1
        car_controls.throttle = lastThrottle
        client.setCarControls(car_controls)
        print("------------油门", car_controls.throttle, "开始启动---------")
        t1 = time.clock()
client.enableApiControl(False)
