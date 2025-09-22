# from requests_html import HTMLSession
# import speech_to_text
# s=HTMLSession()
# query='patna'
# url=f"https://www.google.com/search?q=weather+{query}"
# r=s.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'})
# temp=r.html.find('span.wob_t.q8U8x',first=True)
# unit=r.html.find('div.vk_bk.wob-unit span.wob_t',first=True)
# des=r.html.find('div.VQF4g span#wob_dc',first=True)
# if temp:
#     temp1 = temp
#     print(f"Temperature: {temp1.text}")
# else:
#     print("Temperature data not found.")

# if unit:
#     unit1 = unit
#     print(f"Unit: {unit1.text}")
# else:
#     print("Unit data not found.")

# if des:
#     des1 = des
#     print(f"Description: {des1.text}")
# else:
#     print("Description data not found.")
import requests

def weather():
    API_KEY = "233b7d41da182897ab7e95f62464b5e1"  # Replace with your API key
    CITY ='bangalore'   # Change to your desired location
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"


   
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        print(f"Temperature: {temp}°C")
        print(f"Weather Description: {weather_desc.capitalize()}")
        return f"Temperature: {temp}°C" + f"Weather Description: {weather_desc.capitalize()}"
    
    else:
        print("Failed to retrieve weather data.")

    


