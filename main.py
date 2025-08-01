import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from flask import Flask, request
from google import genai

# Load environment variables from .env
load_dotenv()

# Load tokens from environment
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_SIGNING_SECRET = os.environ.get("SLACK_SIGNING_SECRET")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# Initialize Flask app and Slack app
flask_app = Flask(__name__)
app = App(token=SLACK_BOT_TOKEN, signing_secret=SLACK_SIGNING_SECRET)
handler = SlackRequestHandler(app)

# Initialize Gemini client
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

@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=3000, debug=True)
