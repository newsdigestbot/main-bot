import os, tweepy, time

# 1. ANAHTAR VAR MI?
print("=== ANAHTAR KONTROLÜ ===")
for key in ['TWITTER_API_KEY', 'TWITTER_API_SECRET', 'TWITTER_ACCESS_TOKEN', 
            'TWITTER_ACCESS_TOKEN_SECRET', 'TWITTER_BEARER_TOKEN']:
    durum = "✅ VAR" if os.environ.get(key) else "❌ YOK"
    print(f"{key}: {durum}")

# 2. BAĞLANTI KURULUYOR MU?
print("\n=== TWITTER BAĞLANTISI ===")
try:
    client = tweepy.Client(
        bearer_token=os.environ.get('TWITTER_BEARER_TOKEN'),
        consumer_key=os.environ.get('TWITTER_API_KEY'),
        consumer_secret=os.environ.get('TWITTER_API_SECRET'),
        access_token=os.environ.get('TWITTER_ACCESS_TOKEN'),
        access_token_secret=os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
    )
    print("✅ Bağlantı kuruldu!")
except Exception as e:
    print(f"❌ Bağlantı HATASI: {e}")

# 3. TWEET ATILIYOR MU?
print("\n=== TWEET DENEMESİ ===")
try:
    tweet = f"🤖 TEST {time.strftime('%H:%M:%S')}: Bot bağlantısı tamam!"
    response = client.create_tweet(text=tweet)
    print(f"✅ TWEET BAŞARILI! ID: {response.data['id']}")
except Exception as e:
    print(f"❌ T
