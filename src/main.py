from loader import load_data

from mapper import map_accounts
from llm_reasoning import get_llm_reasoning
from validator import validate_mappings
from validator import validate_adjustments


tb, coa, prior_tb, fx, adjustments = load_data()
"""
print("\n=== Trial Balance ===")
print(tb.head())

print("\n=== Chart of Accounts ===")
print(coa.head())

print("\n=== Prior Period TB ===")
print(prior_tb.head())

print("\n=== FX Rates ===")
print(fx.head())

print("\n=== Manual Adjustments ===")
print(adjustments)

print("\n=== Manual Adjustments ===")

for key, value in adjustments.items():
    print(f"\n{key}:")
    print(value[:2] if isinstance(value, list) else value)

print("\n=== Missing Values in TB ===")
print(tb.isnull().sum())

print("\n=== Missing Values in COA ===")
print(coa.isnull().sum())

print("\n=== Duplicate Accounts in TB ===")

duplicates = tb[tb.duplicated()]

print(duplicates)

missing_accounts = tb[
    ~tb['account_code'].isin(coa['account_code'])
]

print("\n=== Accounts Missing in COA ===")
print(missing_accounts)

total_debit = tb['debit'].sum()
total_credit = tb['credit'].sum()

print("\n=== Trial Balance Check ===")
print("Total Debit:", total_debit)
print("Total Credit:", total_credit)

difference = total_debit - total_credit

print("Difference:", difference)

print("\n=== Missing FX Rates ===")
print(fx.isnull().sum())"""

## account maping form mapper.py
mapped_df = map_accounts(tb, coa)

print("\n=== Account Mapping Results ===")
print(mapped_df.head(10))

# from validator.py
issues = validate_mappings(mapped_df)

print("\n=== Validation Issues ===")

if len(issues) == 0:
    print("No validation issues found.")

else:
    for issue in issues:
        print("-", issue)

adjustment_issues = validate_adjustments(adjustments)

print("\n=== Adjustment Validation ===")

if len(adjustment_issues) == 0:
    print("All journal entries are balanced.")

else:
    for issue in adjustment_issues:
        print("-", issue)


print("\n=== LLM Reasoning Layer ===")

for _, row in mapped_df.iterrows():

    if row['confidence_score'] < 70:

        reasoning = get_llm_reasoning(
            row['tb_account']
        )

        print("\nAccount:", row['tb_account'])
        print(reasoning)


with open("output/validation_report.txt", "w") as f:

    # Mapping validation issues
    f.write("=== Mapping Validation Issues ===\n")

    if len(issues) == 0:
        f.write("No mapping issues found.\n")

    else:
        for issue in issues:
            f.write(f"- {issue}\n")

    # Adjustment validation
    f.write("\n=== Adjustment Validation Issues ===\n")

    if len(adjustment_issues) == 0:
        f.write("All journal entries are balanced.\n")

    else:
        for issue in adjustment_issues:
            f.write(f"- {issue}\n")

    # LLM reasoning layer
    f.write("\n=== LLM Reasoning Layer ===\n")

    for _, row in mapped_df.iterrows():

        if row['confidence_score'] < 70:

            reasoning = get_llm_reasoning(
                row['tb_account']
            )

            f.write(f"\nAccount: {row['tb_account']}\n")
            f.write(reasoning)
            f.write("\n")

print("\nValidation report saved.")