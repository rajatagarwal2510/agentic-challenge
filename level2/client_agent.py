from fastmcp.client import Client
import asyncio
import re

def extract_city(user_input: str) -> str:
    
    match = re.search(r"(?:in|of)\s+([A-Za-z\s]+)", user_input, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    else:
        return user_input.strip()

async def main():
    async with Client("http://127.0.0.1:8080/mcp") as client:
        question = input("Ask about weather: ")

        city = extract_city(question)
        print(f"Detected city: {city}")

        result = await client.call_tool("get_weather", {"city": city})

        if hasattr(result, "data"):
            print(result.data)
        else:
            print(result)

if __name__ == "__main__":
    asyncio.run(main())
