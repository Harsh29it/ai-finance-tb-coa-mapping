def validate_mappings(mapped_df):

    validation_issues = []

    # Low confidence mappings
    low_confidence = mapped_df[
        mapped_df['confidence_score'] < 70
    ]

    for _, row in low_confidence.iterrows():

        validation_issues.append(
            f"Low confidence mapping: "
            f"{row['tb_account']} "
            f"-> {row['matched_coa']} "
            f"({row['confidence_score']})"
        )

    # Unmapped accounts
    unmapped = mapped_df[
        mapped_df['status'] == "Unmapped"
    ]

    for _, row in unmapped.iterrows():

        validation_issues.append(
            f"Unmapped account: "
            f"{row['tb_account']}"
        )

    return validation_issues


def validate_adjustments(adjustments):

    issues = []

    entries = adjustments['entries']

    for entry in entries:

        total_debit = 0
        total_credit = 0

        for line in entry['lines']:

            total_debit += line['debit']
            total_credit += line['credit']

        if total_debit != total_credit:

            issues.append(
                f"{entry['id']} is unbalanced: "
                f"Debit={total_debit}, Credit={total_credit}"
            )

    return issues