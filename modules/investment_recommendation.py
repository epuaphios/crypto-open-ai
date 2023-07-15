import requests

def get_investment_recommendation(coin, coin_data, eth_data, coin_opens, coin_highs, coin_lows, coin_closes, eth_opens, eth_highs, eth_lows, eth_closes, gpt_api, option):
    url = "https://api.openai.com/v1/engines/text-davinci-003/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {gpt_api}",
    }
    coin_price = coin_data[0][4]
    print("Here are the current prices for bitcoin and etherium")
    print("Please wait, generating your response...")
    eth_price = eth_data[0][4]
    coin_prompt = f"\n\n{coin}-USD historical data:\n- Opens: {coin_opens}\n- Highs: {coin_highs}\n- Lows: {coin_lows}\n- Closes: {coin_closes}"
    eth_prompt = f"\n\nETH-USD historical data:\n- Opens: {eth_opens}\n- Highs: {eth_highs}\n- Lows: {eth_lows}\n- Closes: {eth_closes}"
    prompt = f"{coin} gecmis verilere gore bir analiz yapip 1 saat icinde kac fiyati kac olur ?  {option} investment strategy. gecmis fiyat bilgileri burda : {coin_prompt}{eth_prompt}\n\n{coin}-USD price: {coin_price}\nETH-USD price: {eth_price}"
    print(prompt)
    body = {
          "prompt": prompt,
          "max_tokens": 585,
          "temperature": 0.1
           }
    response = requests.post(url, headers=headers, json=body)
    result = response.json()
    choices = result.get('choices', []) 
    completion = choices[0]['text'].strip() if choices else '' 
    return completion