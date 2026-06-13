import requests

while True:
    city = input("Enter city name (or 'exit'): ")

    if city.lower() == "exit":
        break

    try:
        response = requests.get(f"https://wttr.in/{city}?format=3")
        print(response.text)
    except:
        print("Unable to fetch weather.")