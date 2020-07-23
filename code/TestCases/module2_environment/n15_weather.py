import airsim
import time

# connect to the AirSim simulator
client = airsim.CarClient()
client.confirmConnection()
client.enableApiControl(True)
car_controls = airsim.CarControls()
car_state = client.getCarState()
# 天气控制
client.simEnableWeather(True)
weather_list = {
        "Rain": 0,
        "Roadwetness": 1,
        "Snow": 2,
        "RoadSnow": 3,
        "MapleLeaf": 4,
        "RoadLeaf": 5,
        "Dust": 6,
        "Fog": 7,
        "Enabled": 8
    }
# 遍历一遍天气
for i in weather_list:
    print(i)
    client.simSetWeatherParameter(weather_list[i], 0.5)
    client.simSetWeatherParameter(weather_list[i]-1, 0)
    time.sleep(3)

client.enableApiControl(False)