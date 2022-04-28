

NAVYPIERWEATHER = "https://api.weather.gov/gridpoints/LOT/75,73/forecast"

# python3 -m pip install requests
import requests

def main():

    # make a request via requests library
    chiweather = requests.get(NAVYPIERWEATHER)
    
    chiweather = chiweather()
   
    print(chiweather.get("properties").get("periods"))
    #print(chiweather.get("icon"))
    #print(chiweather.get("detailedForecast"))
    
if __name__ == "__main__":
    main()
