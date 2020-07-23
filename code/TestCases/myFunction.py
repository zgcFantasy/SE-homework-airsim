import airsim
import threading

client = airsim.CarClient()
client.confirmConnection()
client.enableApiControl(True)
car_controls = airsim.CarControls()
car_state = client.getCarState()


def initAirSim():
    return [client, car_controls, car_state]


'''
    设定天气情况，并选择是否进行速度限制
    调用示例：
        setWeatherOfMyAirSim("Rain", 0.5, True)
    参数说明：
        weather: string, 设定天气类型，参考 weather_list
        value: number, 0-1, 设定天气的程度
        islimit: boolean, True 代表开启限速功能，False 为关闭
'''


def setWeatherOfMyAirSim(weather, value, islimit):
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

    def limitSpeed():
        while True:
            client.enableApiControl(False)
            if client.getCarState().speed > 30 / 3.6:
                client.enableApiControl(True)
                car_controls.brake = 1
                client.setCarControls(car_controls)
                while True:
                    if client.getCarState().speed < 30 / 3.6:
                        car_controls.brake = 0
                        client.setCarControls(car_controls)
                        break

    # 设定天气
    client.simEnableWeather(True)
    client.simSetWeatherParameter(weather_list[weather], value)
    client.enableApiControl(False)
    # 触发条件
    if islimit and value >= 0.5:
        client.enableApiControl(True)
        # 最高 1 档
        car_controls.manual_gear = 1
        car_controls.is_manual_gear = True
        client.setCarControls(car_controls)

        # 创建一个线程，用于在运行时随时检测并限制速度
        t = threading.Thread(target=limitSpeed, name='LimitSpeed')
        t.start()
        return t
