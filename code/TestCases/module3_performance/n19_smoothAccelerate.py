# 平滑的加速曲线
# 除换挡瞬间外，不能有明显阶跃
import time
import TestCases.myFunction as MyFun
import matplotlib.pyplot as plt

[client, car_controls, car_state] = MyFun.initAirSim()

# 开启油门
car_controls.throttle = 1
client.setCarControls(car_controls)
x = []
y = []
time.clock()
while True:
    if time.clock() > 40:
        break
    time.sleep(0.1)
    x.append(time.clock())
    y.append(client.getCarState().speed)
plt.plot(x, y)
plt.show()
client.enableApiControl(False)