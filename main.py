from fastapi import FastAPI

import ipinfo
import requests
import aiohttp

app = FastAPI()

async def get_ip_and_location():
    access_token = "b2a628e64768ef"

    handler = ipinfo.getHandlerAsync(access_token)
    details = await handler.getDetails()

    message = {
        'ip': details.ip,
        'current_city': details.city,
        'current_country_name': details.country_name,
        'latitude': details.latitude,
        'longitude': details.longitude
    }

    return message

async def get_temperature(lat, long):
    api_key = "9d93201d4cecb30c7fc02e4d6ca79703"

    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api_key}") as response:
            temp_info = await response.json()
            current_temp = temp_info['main']['temp']
            return current_temp

@app.get("/api/hello")
async def requester_location_info(visitor_name: str):
    try:
        location = await get_ip_and_location()
        print(location)
        temp = await get_temperature(location['latitude'], location['longitude'])

        message = {
            "client_ip": location['ip'],
            "location": location['current_city'],
            "greeting": f"Hello, {visitor_name}, the temperature is {temp} degrees Celcius in {location['current_city']}"
        }

        return message
    except Exception as e:
        print(e)
        return e


# print(get_temperature(10, 34.4))