import investpy
import pandas as pd

# Buscar todas as ações listadas na bolsa brasileira
stocks = investpy.get_stocks(country='brazil')

# Exibir as colunas disponíveis
print(stocks.columns)

# Selecionar as colunas disponíveis
br_stocks_df = stocks[['symbol', 'name']]

# Renomear colunas para seguir o padrão anterior
br_stocks_df.rename(columns={
    'symbol': 'Ticker',
    'name': 'Company Name'
}, inplace=True)

# Adicionar o sufixo '.SA' aos tickers para compatibilidade com o Yahoo Finance
br_stocks_df['Ticker'] = br_stocks_df['Ticker'] + '.SA'

# Salvar como CSV
br_stocks_df.to_csv('data/br_stocks.csv', index=False)

print("CSV gerado com sucesso!")
