# Deploying to Vercel

## 1. Install Vercel CLI
```bash
npm i -g vercel
```

## 2. Login to Vercel
```bash
vercel login
```

## 3. Deploy
```bash
vercel --prod
```

## 4. Set Environment Variables in Vercel Dashboard
After deployment, go to your Vercel project dashboard and add these environment variables:
- `SLACK_BOT_TOKEN` - Your Slack bot token
- `SLACK_SIGNING_SECRET` - Your Slack signing secret
- `GEMINI_API_KEY` - Your Gemini API key

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
├── runtime.txt            # Python version specification
└── .env                   # Local environment (not deployed)
```

## Environment Variables
Make sure to set these in Vercel Dashboard:
- `SLACK_BOT_TOKEN` - Your Slack bot token
- `SLACK_SIGNING_SECRET` - Your Slack signing secret
- `GEMINI_API_KEY` - Your Gemini API key

## Troubleshooting
If the build fails:
1. Check that all environment variables are set in Vercel dashboard
2. Ensure the Python version matches (3.9)
3. Verify all dependencies are in requirements.txt 