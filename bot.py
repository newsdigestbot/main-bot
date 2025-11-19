import os, sys

# HATA YAKALAMA
try:
    import tweepy
    print("✅ tweepy yüklü")
except:
    print("❌ tweepy yüklü değil")
    sys.exit(1)

# ANAHTAR KONTROLÜ
print("\n=== ANAHTAR KONTROLÜ ===")
keys = ['TWITTER_API_KEY', 'TWITTER_API_SECRET', 'TWITTER_ACCESS_TOKEN', 
        'TWITTER_ACCESS_TOKEN_SECRET', 'TWITTER_BEARER_TOKEN']
for key in keys:
    deger = os.environ.get(key)
    if deger:
        print(f"{key}: ✅ VAR ({deger[:10]}...)")
    else:
        print(f"{key}: ❌ YOK")
        sys.exit(1)

# BAĞLANTI TESTİ
print("\n=== TWITTER BAĞLANTISI ===")
try:
    client = tweepy.Client(
        bearer_token=os.environ.get('TWITTER_BEARER_TOKEN'),
        consumer_key=os.environ.get('TWITTER_API_KEY'),
        consumer_secret=os.environ.get('TWITTER_API_SECRET'),
        access_token=os.environ.get('TWITTER_ACCESS_TOKEN'),
        access_token_secret=os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
    )
    print("✅ Bağlantı kuruldu")
except Exception as e:
    print(f"❌ Bağlantı HATASI: {e}")
    sys.exit(1)

# TWEET TESTİ
print("\n=== TWEET DENEMESİ ===")
try:
    tweet = f"🤖 TEST {os.environ.get('TWITTER_API_KEY', '')[:5]}..."
    response = client.create_tweet(text=tweet)
    print(f"✅ TWEET BAŞARILI! ID: {response.data['id']}")
except Exception as e:
    print(f"❌ TWEET HATASI: {e}")
    print(f"\n🔍 HATA DETAYI:")
    print(f"Tip: {type(e).__name__}")
    print(f"Mesaj: {str(e)[:200]}")

print("\n=== BİTTİ ===")
