weather = {"Sunny": 200, "Rainy": 120, "Cloudy": 150, "Stormy": 80}
most_common = max(weather, key=weather.get)
print(most_common)
