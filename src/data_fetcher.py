import pandas as pd
import yfinance as yf


class DataFetcher:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.stocks_df = self._load_stocks()

    def _load_stocks(self):
        """
        Carrega os tickers e nomes das ações a partir de um arquivo CSV.
        """
        try:
            stocks_df = pd.read_csv(self.csv_path)
            return stocks_df
        except Exception as e:
            print(f"Erro ao carregar o CSV: {e}")
            return None

    def fetch_stock_data(self, ticker, start="2020-01-01", end="2024-01-01"):
        """
        Baixa os dados históricos de uma ação usando o yfinance.
        """
        try:
            stock_data = yf.download(ticker, start=start, end=end)
            if stock_data.empty:
                raise ValueError(f"Nenhum dado encontrado para {
                                 ticker}. Pode estar deslistado.")
            return stock_data
        except Exception as e:
            print(f"Erro ao baixar dados para {ticker}: {e}")
            return None

    def fetch_all_stocks(self):
        """
        Busca os dados históricos de todas as ações listadas no CSV.
        """
        if self.stocks_df is not None:
            stock_data = {}
            for index, row in self.stocks_df.iterrows():
                ticker = row['Ticker']
                data = self.fetch_stock_data(ticker)
                if data is not None:
                    stock_data[ticker] = data
            return stock_data
        else:
            print("DataFrame de ações não carregado corretamente.")
            return None


# Exemplo de uso
if __name__ == "__main__":
    fetcher = DataFetcher('data/br_stocks.csv')
    data = fetcher.fetch_all_stocks()
    print(data)
