import requests, csv

def getWeather(cities):
    weather = []
    for c in cities:
        apiURL = 'https://api.openweathermap.org/data/2.5/weather?q=' + c + '&appid=' + str(apiKey)
        data = requests.get(apiURL).json()
        weather.append(data)
    return weather

def writeToCSV(weather):
    outputFile = open('test.csv', 'w', newline='')
    csvWriter = csv.writer(outputFile)
    csvWriter.writerow(['Name', 'Weather', 'Temp'])
    for w in weather:
        csvWriter.writerow([w['name'], w['weather'][0]['main'], w['main']['temp']])


apiKey = 'f4b4e38c6f0c8058fe74e738c4721056'
cities = ['Dallas', 'Houston', 'Austin', 'San+Antonio', 'Fort+Worth']
weather = getWeather(cities)
print(weather)
