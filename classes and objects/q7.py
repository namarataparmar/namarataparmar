class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters

today_weather = Weather(["Temperature", "Humidity", "Pressure", "Wind", "Visibility"])

print("Humidity" in today_weather) 
print("rainfall" in today_weather)
