# 雨雪天气最大速度限制
# 不超过 30km/h 即大约 8.3 m/s
# 通过键盘操控，查看速度是否被限制在一定范围
import TestCases.myFunction as MyFun


[client, car_controls, car_state] = MyFun.initAirSim()


# 不限速
MyFun.setWeatherOfMyAirSim("Rain", 0.8, False)



