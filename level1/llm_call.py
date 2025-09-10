import os
from google import genai

client = genai.Client() 
user_input=input("Ask Gemini anything: ")
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_input
)

print("Gemini says:", response.text)
