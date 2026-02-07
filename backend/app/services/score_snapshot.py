def build_rules_snapshot(rules):
    snapshot = []

    for rule in rules:
        snapshot.append({
            "id": rule.id,
            "name": rule.name,
            "field": rule.field,
            "weight": rule.weight,
            "enabled": rule.enabled
        })

    return snapshot