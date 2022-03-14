stocks = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}
}
stocks.update({'BTT': {'Boombit': 23}})

print(dict.values(stocks))

# -------------------------------------------------------
stocks = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}
}
stocks['BBT'] = {'Boombit': 23}
print(stocks.values())
