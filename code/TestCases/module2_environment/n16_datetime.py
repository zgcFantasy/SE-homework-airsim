import time
import TestCases.myFunction as MyFun

[client, car_controls, car_state] = MyFun.initAirSim()

client.simSetTimeOfDay(True, "", False, 1, 1, True)
client.enableApiControl(False)
