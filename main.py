import requests


def get_current_weather(session, city_name):
    api_key = 'APIKEYHERE'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    r = session.get(url)
    return r.json()


def main():
    s = requests.Session()
    manc = get_current_weather(s, 'Manchester')
    lond = get_current_weather(s, 'London')
    print(manc, lond)


main()
