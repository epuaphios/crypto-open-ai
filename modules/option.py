from rich.console import Console

console = Console()
from modules.investment_recommendation import get_investment_recommendation


def user_option(coin, coin_data, coin_opens, coin_highs, coin_lows, coin_closes, gpt_api, option, coin_date,day_prediction,coin_orders):
    investment_recommendation = get_investment_recommendation(coin, coin_data, coin_opens, coin_highs, coin_lows,coin_closes, gpt_api, option, coin_date,day_prediction,coin_orders)

    # print("\nInvestment Recommendation:", investment_recommendation)
    return
