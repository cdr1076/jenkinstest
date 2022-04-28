

NAVYPIERWEATHER = "https://api.weather.gov/gridpoints/LOT/75,73/forecast"

# python3 -m pip install requests
import requests

def main():

    # make a request via requests library
    chiweather = requests.get(NAVYPIERWEATHER)
    
    # remove the json attached to the 200 response
    chiweather = chiweather()

    # display just the list (array) of space travelers
    print(chiweather.get("periods"))
    print(chiweather.get("icon"))
    print(chiweather.get("detailedForecast"))
    
if __name__ == "__main__":
    main()
