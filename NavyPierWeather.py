

NAVYPIERWEATHER = "https://api.weather.gov/gridpoints/LOT/75,73/forecast"

# python3 -m pip install requests
import requests

def main():

    # make a request via requests library
    chiweather = requests.get(NAVYPIERWEATHER).json
    
    chiweather = chiweather()
   
    print(chiweather.get("properties").get("periods"))
    
    for subdata in chiweather.get("properties").get("periods"):
        print(subdata.get("name"))
        print(subdata.get("temperature"))
        print(subdata.get("temperatureUnit"))
        print(subdata.get("temperatureTrend"))
        print(subdata.get("windSpeed"))
        print(subdata.get("windDirection"))
        print(subdata.get("icon"))
        print(subdata.get("detailedForecast"))
    
if __name__ == "__main__":
    main()
