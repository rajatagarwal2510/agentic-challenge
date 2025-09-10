from fastmcp import FastMCP
import requests

API_KEY = "c262bf6578ace24a68759f0f38535aeb" 

mcp = FastMCP("Weather Server")

@mcp.tool
def get_weather(city: str) -> str:
  
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        desc = data['weather'][0]['description'].capitalize()
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        return (
            f"Weather in {city}: {desc}, {temp}°C "
            f"(feels like {feels_like}°C), Humidity: {humidity}%"
        )
    else:
        return f"Error: {response.status_code} - {response.text}"

if __name__ == "__main__":
    mcp.run(transport="http", port=8080)
