# 转弯程度测试
# 转弯程度应可控
import time
import TestCases.myFunction as MyFun
import matplotlib.pyplot as plt

[client, car_controls, car_state] = MyFun.initAirSim()

# 开启油门
car_controls.throttle = 1
# 方向盘程度
car_controls.steering = 1
while True:
    print(car_controls.steering)
    x = []
    y = []
    if car_controls.steering - 0 > 0.01:
        client.setCarControls(car_controls)
        t1 = time.clock()

    else:
        break
    while True:
        if time.clock() - t1 >= 20:
            t1 = time.clock()
            break
        else:
            time.sleep(0.1)
            car_state = client.getCarState()
            x.append(time.clock())
            y.append(car_state.kinematics_estimated.position.y_val)
    plt.plot(x, y)
    plt.show()
    car_controls.steering -= 0.2

client.enableApiControl(False)
