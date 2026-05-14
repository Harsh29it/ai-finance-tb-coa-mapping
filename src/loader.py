import pandas as pd
import json


def load_data():
    # csv loding
    tb = pd.read_csv("data/trial_balance.csv")
    coa = pd.read_csv("data/chart_of_accounts.csv")
    prior_tb = pd.read_csv("data/prior_period_tb.csv")
    fx = pd.read_csv("data/fx_rates.csv")

    #  JSON file
    with open("data/manual_adjustments.json", "r") as f:
        adjustments = json.load(f)

    return tb, coa, prior_tb, fx, adjustments
