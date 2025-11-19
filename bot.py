import tweepy
import openai
import os

# API Keys - Secrets'ten gelecek
TW_API_KEY = os.getenv('TW_API_KEY')
TW_API_SECRET = os.getenv('TW_API_SECRET')
TW_ACCESS_TOKEN = os.getenv('TW_ACCESS_TOKEN')
TW_ACCESS_SECRET = os.getenv('TW_ACCESS_SECRET')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Twitter Client
client = tweepy.Client(
    consumer_key=TW_API_KEY,
    consumer_secret=TW_API_SECRET,
    access_token=TW_ACCESS_TOKEN,
    access_token_secret=TW_ACCESS_SECRET
)

openai.api_key = OPENAI_API_KEY

def generate_tweet():
    prompt = """
    Write a short tweet about trending crypto news or common trading mistakes.
    Include a casual call-to-action like 'Support my caffeine addiction' and link to buymeacoffee.com/newsdigestx
    Max 280 chars, informal tone.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def tweet():
    try:
        text = generate_tweet()
        client.create_tweet(text=text)
        print(f"Tweeted: {text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    tweet()
