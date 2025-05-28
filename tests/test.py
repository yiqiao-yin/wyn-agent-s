import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")



# Print loaded keys (for demonstration purpose, avoid printing secrets in production)
# print("OpenAI API Key:", openai_api_key)
# print("Twilio Account SID:", twilio_account_sid)
# print("Twilio Auth Token:", twilio_auth_token)
# print("SerpAPI API Key:", serpapi_api_key)
# print("PY Email Key:", py_email_key)


# Import the agent
from wyn_agent_s.main import AgentX

# Initialize and start the chat!
agent = AgentX(
    openai_api_key=OPENAI_API_KEY,
    serpapi_key=SERPAPI_API_KEY
)

# Run the chat
agent.start_chat()