def explain_score(financial_data, rules):
    explanation = []

    for rule in rules:
        value = getattr(financial_data, rule.field, None)
        if value is None:
            continue

        contribution = value * rule.weight

        explanation.append({
            "rule": rule.name,
            "field": rule.field,
            "value": value,
            "weight": rule.weight,
            "contribution": contribution
        })

    return explanation