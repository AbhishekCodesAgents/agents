import requests
from agents import Agent
from agents import Runner
from dotenv import load_dotenv

url = "<<url>>"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 8f7e26dc-5324-4f43-a5e1-92dc6a94ebb7"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": "Hello, how can I help you?"}
    ],
    "max_tokens": 150
}

trip_planner_instructions = """
Context:
You are a friendly travel planner who designs simple one-day itineraries.

Instructions:
When given a city and a list of interests, create a realistic one-day plan with:
- A morning activity
- An afternoon activity
- An evening activity

Make your suggestions:
- Specific and easy to understand
- Safe and tourist-friendly
- Based only in the city mentioned

If the interests are unclear, choose popular attractions most visitors enjoy.

Input:
You will receive a short description that includes:
- The city name
- The traveler﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿s interests (e.g., museums, food, nightlife)

Output:
Respond with:
1. A clear title for the day (e.g., "One Perfect Day in Paris").
2. A bullet list with three sections:
   - Morning: ...
   - Afternoon: ...
   - Evening: ...
Each section should be 1﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿﷿2 short sentences.
"""

trip_planner_agent = Agent(
    name = "Trip Planner",                 # Name of the agent
    instructions = trip_planner_instructions,  # The rules and behavior for the agent
    model = "gpt-3.5-turbo"                 # The AI model (LLM) to use
)

# Print a confirmation message that the agent was created
print(f"Agent '{trip_planner_agent.name}' created successfully!")

response = requests.post(url, headers=headers, json=data)

# DEBUG: Print the status and raw content first
print(f"Status Code: {response.status_code}")
print("--- Raw Response Text Begin ---")
print(response.text)
print("--- Raw Response Text End ---")

# Only try JSON parsing if the response status is 200 OK
if response.status_code == 200:
    print(response.json())
else:
    print(f"Request failed with status: {response.status_code}")



