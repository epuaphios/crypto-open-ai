import requests

def get_investment_recommendation(btc_data, eth_data, btc_opens, btc_highs, btc_lows, btc_closes, eth_opens, eth_highs, eth_lows, eth_closes, gpt_api, option):
    url = "https://api.openai.com/v1/engines/text-davinci-003/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {gpt_api}",
    }
    btc_price = btc_data[0][4]
    print("Here are the current prices for bitcoin and etherium")
    # print("Please wait, generating your response...")
    eth_price = eth_data[0][4]
    btc_prompt = f"\n\nXRP-USD historical data:\n- Opens: {btc_opens}\n- Highs: {btc_highs}\n- Lows: {btc_lows}\n- Closes: {btc_closes}"
    eth_prompt = f"\n\nETH-USD historical data:\n- Opens: {eth_opens}\n- Highs: {eth_highs}\n- Lows: {eth_lows}\n- Closes: {eth_closes}"
    prompt = f"XRP gecmis verilere gore bir analiz yapip 30 dk icinde kac fiyati kac olur ? etherium gecmisinide verdim buna gore yorumlar misin ? {option} investment strategy.{btc_prompt}{eth_prompt}\n\nBTC-USD price: {btc_price}\nXRP-USD price: {eth_price}"
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