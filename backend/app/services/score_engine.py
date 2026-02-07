def calculate_score(financial_data, rules):
    score = 0

    for rule in rules:
        value = getattr(financial_data, rule.field, None)

        if value is None:
            continue

        score += value * rule.weight

    return max(0, min(1000, int(score)))
