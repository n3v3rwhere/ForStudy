import os
from dotenv import load_dotenv

load_dotenv()

app_name = os.getenv("APP_NAME")
api_key = os.getenv("API_KEY")

if not app_name:
    print("Error: APP_NAME is not configured.")
    raise SystemExit(1)
if not api_key:
    print("Error: API_KEY is not configured.")
    raise SystemExit(1)

print(f"App name: {app_name}")
print(f"API_KEY loaded: {bool(api_key)}")