import tweepy
import os
import time

# 1. API anahtarlarını kontrol et (debug)
print("=== API ANAHTARLARI KONTROLÜ ===")
print(f"TWITTER_API_KEY: {'VAR' if os.environ.get('TWITTER_API_KEY') else 'YOK!'}")
print(f"TWITTER_ACCESS_TOKEN: {'VAR' if os.environ.get('TWITTER_ACCESS_TOKEN') else 'YOK!'}")
print(f"OPENAI_API_KEY: {'VAR' if os.environ.get('OPENAI_API_KEY') else 'YOK!'}")

try:
    # 2. Twitter bağlantısı kur
    print("\n=== TWITTER BAĞLANTISI KURULUYOR ===")
    client = tweepy.Client(
        bearer_token=os.environ.get('TWITTER_BEARER_TOKEN'),
        consumer_key=os.environ.get('TWITTER_API_KEY'),
        consumer_secret=os.environ.get('TWITTER_API_SECRET'),
        access_token=os.environ.get('TWITTER_ACCESS_TOKEN'),
        access_token_secret=os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
    )
    print("✅ Bağlantı kuruldu")

    # 3. Zorla tweet at
    print("\n=== TWEET ATILIYOR ===")
    tweet_text = f"🤖 TEST {time.strftime('%H:%M:%S')}: Bot çalışıyor!"
    response = client.create_tweet(text=tweet_text)
    print(f"✅ TWEET BAŞARILI! ID: {response.data['id']}")
    print(f"Tweet metni: {tweet_text}")

except Exception as e:
    print(f"\n❌ HATA: {e}")
    print(f"Hata tipi: {type(e).__name__}")

print("\n=== BOT BİTTİ ===")
