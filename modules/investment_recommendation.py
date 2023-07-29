import requests


def chat_with_gpt4(prompt, url, headers):
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


def get_investment_recommendation(coin, coin_data, coin_opens, coin_highs, coin_lows,coin_closes, gpt_api, option):
    url = "https://api.openai.com/v1/engines/text-davinci-003/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {gpt_api}",
    }
    coin_price = coin_data[0][4]
    print("Here are the current prices for bitcoin and etherium")
    print("Please wait, generating your response...")
    coin_prompt = f"\n\n{coin}-USD historical data:\n- Opens: {coin_opens}\n- Highs: {coin_highs}\n- Lows: {coin_lows}\n- Closes: {coin_closes}"
    prompt = f"{coin} coinin gecmis verilere gore destek ve direnc fiyatini soyleyebilir misin ?  {option} investment strategy. gecmis fiyat bilgileri burda 90 gunluktur : {coin_prompt}\n\n{coin}-USD live price: {coin_price}\n\n"
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
    print(completion)
    choise = input("Do you want to continue? (y/n): ")
    if choise == 'n':
        return completion
    else:
        while True:
            new_prompt = input("Enter your message (or 'exit' to quit): ")
            prompt += new_prompt
            print(prompt)
            completion = chat_with_gpt4(prompt, url, headers=headers)
            print(completion)
            if prompt.lower() == 'exit':
                break
        return completion
