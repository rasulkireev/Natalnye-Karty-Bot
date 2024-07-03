import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv(override=True)

antropic_client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)
