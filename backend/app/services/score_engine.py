def calculate_score(financial_data):
    score = 0

    score += financial_data.income * 0.3
    score += financial_data.history * 0.4
    score += (100 - financial_data.debt) * 0.2
    score += financial_data.consistency * 0.1

    final_score =int(min(max(score, 0), 1000))
    return final_score