# %%
gaming = {
    '11B': 362.5,
    'CDR': 297.0,
    'CIG': 0.85,
    'PLW': 318.0,
    'TEN': 300.0
}

#[print(stock) for stock in gaming if gaming[stock] > 100]
for stock in gaming:
    if gaming[stock] > 100:
        print(stock)

# ---------------------------------------------------------------
for ticker, close in gaming.items():
    if close > 100.0:
        print(ticker)
