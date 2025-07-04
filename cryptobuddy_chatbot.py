# -*- coding: utf-8 -*-
"""CryptoBuddy_Chatbot

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iZdE3-lTFlzWaGmociI8H6noHyhxY1OC
"""

print("👋 Hey there! I'm *CryptoBuddy*, your AI-powered financial sidekick 💸🌱")
print("Ask me about crypto trends, sustainability, or long-term investments!")

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    }
}

def recommend_crypto(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query or "eco" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"🌱 Invest in {recommend}! It’s eco-friendly and has long-term potential.")

    elif "trending" in user_query or "price" in user_query:
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        print(f"📈 Trending up: {', '.join(trending)}")

    elif "long-term" in user_query or "growth" in user_query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] > 7:
                print(f"🚀 {coin} is great for long-term growth and sustainability!")
                return
        print("🔍 No strong long-term candidates found.")

    elif "high market cap" in user_query:
        big_caps = [coin for coin in crypto_db if crypto_db[coin]["market_cap"] == "high"]
        print(f"💼 High Market Cap Coins: {', '.join(big_caps)}")

    elif "energy" in user_query:
        for coin, data in crypto_db.items():
            print(f"{coin} uses {data['energy_use']} energy.")

    else:
        print("🤖 Sorry, I didn’t catch that. Try asking about sustainability, trends, or market cap.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("👋 Goodbye! Remember, crypto is risky—always do your own research! 🔍💸")
        break
    recommend_crypto(user_input)