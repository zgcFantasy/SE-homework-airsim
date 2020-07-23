import TestCases.myFunction as MyFun
import math
# 百公里时速下刹车距离

[client, car_controls, car_state] = MyFun.initAirSim()

# 开启油门
car_controls.throttle = 1
client.setCarControls(car_controls)

x = 0
y = 0
length = 0
# 先百公里加速
while True:
    # 100 km/h 以后开始刹车
    if client.getCarState().speed * 3.6 >= 100:
        x = client.getCarState().kinematics_estimated.position.x_val
        y = client.getCarState().kinematics_estimated.position.y_val
        car_controls.throttle = 0
        car_controls.brake = 1
        client.setCarControls(car_controls)
        print("速度已达到 100 km/h, 开始刹车")

        while True:
            if client.getCarState().speed == 0:
                x = client.getCarState().kinematics_estimated.position.x_val - x
                y = client.getCarState().kinematics_estimated.position.y_val - y
                length = math.sqrt(x * x + y * y)
                print("刹车完成，刹车距离为：", length, "m")
                break

        break
client.enableApiControl(False)
