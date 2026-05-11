from rapidfuzz import fuzz
import pandas as pd


def map_accounts(tb, coa):

    mapped_results = []

    coa_names = coa['account_name'].tolist()

    for _, tb_row in tb.iterrows():

        tb_account = tb_row['account_name']

        best_match = None
        best_score = 0
        best_type = None

        for _, coa_row in coa.iterrows():

            coa_account = coa_row['account_name']

            score = fuzz.ratio(
                tb_account.lower(),
                coa_account.lower()
            )

            if score > best_score:
                best_score = score
                best_match = coa_account
                best_type = coa_row['account_type']

        # Status Logic
        if best_score >= 90:
            status = "Auto Approved"

        elif best_score >= 70:
            status = "Needs Review"

        else:
            status = "Unmapped"

        mapped_results.append({
            "tb_account": tb_account,
            "matched_coa": best_match,
            "account_type": best_type,
            "confidence_score": best_score,
            "status": status
        })

    return pd.DataFrame(mapped_results)