import os
from dotenv import load_dotenv

load_dotenv()

app_name = os.getenv("APP_NAME", "My First Python Repo")
api_key = os.getenv("API_KEY")

if not api_key:
    print("Error: API_KEY is not configured.")
    raise SystemExit(1)

print(f"App name: {app_name}")
print(f"API_KEY loaded: {bool(api_key)}")
print("Project is set up correctly!")