from google import genai
from dotenv import load_dotenv
import os

# Initialize the client
load_dotenv()
API_KEY = os.getenv("API_KEY")
client = genai.Client(api_key=API_KEY)

user_input = "Act like a moderate wallstreetbets user. Make responses short and sweet. "
# Start a conversation with the first request
response = client.models.generate_content(model="gemini-2.0-flash", contents=user_input)
print(response.text)

# Store the response to maintain context for the next request
conversation_history = user_input + response.text

print("----------------------------------------------------------------------------------------------------")
user_input = input()

while user_input != "end":
    response = client.models.generate_content(model="gemini-2.0-flash", contents=user_input + "\nconversation history, use only for context: \n" + conversation_history)
    print(response.text)

    # Store the response to maintain context for the next request
    conversation_history =user_input + response.text + conversation_history

    print("----------------------------------------------------------------------------------------------------")
    
    user_input = input()
