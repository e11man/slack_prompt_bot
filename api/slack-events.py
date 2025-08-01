import os
from slack_bolt import App
from slack_bolt.adapter.vercel import SlackRequestHandler
from google import genai

# Load tokens from environment
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_SIGNING_SECRET = os.environ.get("SLACK_SIGNING_SECRET")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# Initialize Slack app and Gemini client
app = App(token=SLACK_BOT_TOKEN, signing_secret=SLACK_SIGNING_SECRET)
client = genai.Client()  # Reads GEMINI_API_KEY automatically

@app.event("app_mention")
def handle_mention(event, say):
    # Extract message text without the bot mention
    text = event.get("text", "")
    user_mention = f"<@{event.get('user')}>"
    prompt = text.replace(user_mention, "").strip()

    # Call Gemini API to convert prompt to XML
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Convert this prompt to an XML prompt: {prompt}"
    )

    # Replace 'Cursor' with the actual Slack user ID of @Cursor to tag properly
    CURSOR_USER_ID = "U093ZEATVGU"  # @Cursor Slack User ID

    # Post the reply tagging @Cursor
    say(f"<@{CURSOR_USER_ID}> {response.text}")

# Vercel serverless function handler
def handler(request):
    return SlackRequestHandler(app).handle(request) 