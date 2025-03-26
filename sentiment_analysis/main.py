# Run sentiment analysis using OpenAI

# Dependencies
import openai
import os

# Load API key
with open(os.path.join(os.path.dirname(__file__), "secrets.txt"), "r") as f:
    api_key = f.read()
# Connect to OpenAI
openai.api_key = api_key

# Set model
model = "gpt-4o-mini"

# Get text
text = """
Climate change is a threat to our world. The effects of climate change are already being felt around the world.
The world is getting warmer, and this is causing more extreme weather events, such as hurricanes, droughts, and floods.
The polar ice caps are melting, and sea levels are rising. This is causing coastal erosion and threatening the homes of millions of people.
"""

positivity = """
However, recent efforts from a large coalition of nations offers hope.
"""
# text += positivity

# Run sentiment analysis
instruct = "Evaluate the sentiment of this text 0 (completely negative) to 10 (completely positive). Your only output should be a number 0-10 evaluating the snentiment."
response = openai.chat.completions.create(
    model=model,
    messages=[
        {"role": "user", "content": f"{text}\n{instruct}"},
    ],
)

# Get sentiment score
sentiment = response.choices[0].message.content.strip() # Corrected to access message.content
print(f"Sentiment score: {sentiment}")
