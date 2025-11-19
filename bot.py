import tweepy
import os
import time

# HATA AYIKLAMA: Anahtarları kontrol et
print("=== API KONTROLÜ ===")
print(f"API Key var mı? {'EVET' if os.environ.get('TWITTER_API_KEY') else 'HAYIR'}")
print(f"Access Token var mı? {'EVET' if os.environ.get('TWITTER_ACCESS_TOKEN') else 'HAYIR'}")

try:
    # Twitter bağlantısı kur
    print("\n=== TWITTER BAĞLANTISI ===")
    client = tweepy.Client(
        bearer_token=os.environ.get('TWITTER_BEARER_TOKEN'),
        consumer_key=os.environ.get('TWITTER_API_KEY'),
        consumer_secret=os.environ.get('TWITTER_API_SECRET'),
        access_token=os.environ.get('TWITTER_ACCESS_TOKEN'),
        access_token_secret=os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
    )
    print("✅ Bağlantı kuruldu")

    # Zorla tweet at (test için)
    print("\n=== TWEET ATILIYOR ===")
    tweet_text = f"🤖 TEST {time.strftime('%H:%M:%S')}: Bot bağlantısı tamam!"
    response = client.create_tweet(text=tweet_text)
    print(f"✅ BAŞARILI! Tweet ID: {response.data['id']}")

except Exception as hata:
    print(f"\n❌ HATA DETAYI:")
    print(f"Mesaj: {hata}")
    print(f"Tip: {type(hata).__name__}")
    print("--- Twitter hesabınızın 'Elevated' seviyesinde olduğundan emin olun!")

print("\n=== BİTTİ ===")
