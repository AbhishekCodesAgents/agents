import requests
from IPython.display import display, Markdown


# --- UTILITY FUNCTIONS ---
def print_markdown(text):
    """Displays text as Markdown in Jupyter."""
    display(Markdown(text))


# --- CONFIGURATION (Ensure you update these with your exact Pluralsight info) ---
url = "<<URL>>"
api_key = "8f7e26dc-5324-4f43-a5e1-92dc6a94ebb"  # Swap with your actual lab token

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 8f7e26dc-5324-4f43-a5e1-92dc6a94ebb7"
}

# --- PROMPT SETUP ---
# 2. Prompts
trip_planner_instructions = """
You are a friendly travel planner who designs simple one-day itineraries.
Create a realistic plan with a morning, afternoon, and evening activity.
Make your suggestions specific, safe, and tourist-friendly.
"""

itinerary_request = "City: Paris. Interests: museums, coffee shops, and night views."

# 3. Combine instructions and request into a single prompt string
full_text_prompt = f"{trip_planner_instructions.strip()}\n\nTask Input:\n{itinerary_request}"


# --- DATA PAYLOAD MAPPING ---
data = {
    "promptInput": full_text_prompt,  # Fixes the Pluralsight proxy fallback bug
    "prompt": full_text_prompt,       # Secondary custom endpoint fallback
    "model": "gpt-3.5-turbo",
    "messages": [                     # OpenAI standard legacy fallback
        {"role": "system", "content": trip_planner_instructions.strip()},
        {"role": "user", "content": itinerary_request}
    ],
    "max_tokens": 500
}

# --- PROCESS RAW NETWORK CALL ---
print(f"Asking the OpenAI endpoint to design a day for: '{itinerary_request}'")

try:
    response = requests.post(url, headers=headers, json=data)

    print(f"Status Code: {response.status_code}")
    print("\n### Trip Planner Agent's Response 1:\n")

    if response.status_code == 200:

        response_json = response.json()
        print(f" Trip Planner Agent's Response 2: '{response_json}'\n")

        print("\n### Trip Planner Agent's Response 3:\n")

        # Check if the output format is standard OpenAI or Pluralsight simplified
        if "choices" in response_json:
            plan_text = response_json["choices"][0]["message"]["content"]
        elif "response" in response_json:  # Handle the simplified format if the proxy returns it
            plan_text = response_json["response"]
        else:
            plan_text = str(response_json)

        # Display the result formatted nicely
        print(f"### ✈️ Trip Planner Results\n\n{plan_text}")
    else:
        print("Raw Server Error Message:")
        print(response.text)

except Exception as e:
    print(f"Network processing failed: {e}")
