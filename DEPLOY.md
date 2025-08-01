# Deploying to Vercel

## 1. Install Vercel CLI
```bash
npm i -g vercel
```

## 2. Login to Vercel
```bash
vercel login
```

## 3. Set Environment Variables
```bash
vercel env add SLACK_BOT_TOKEN
vercel env add SLACK_SIGNING_SECRET
vercel env add GEMINI_API_KEY

update
```

## 4. Deploy
```bash
vercel --prod
```

## 5. Get Your URL
After deployment, you'll get a URL like:
```
https://your-app-name.vercel.app
```

## 6. Slack Configuration
In your Slack app settings, set the Event Subscriptions Request URL to:
```
https://your-app-name.vercel.app/api/slack-events
```

## Files Structure
```
├── api/
│   └── slack-events.py    # Vercel serverless function
├── vercel.json            # Vercel configuration
├── requirements.txt       # Python dependencies
└── .env                   # Local environment (not deployed)
```

## Environment Variables
Make sure to set these in Vercel:
- `SLACK_BOT_TOKEN` - Your Slack bot token
- `SLACK_SIGNING_SECRET` - Your Slack signing secret
- `GEMINI_API_KEY` - Your Gemini API key 