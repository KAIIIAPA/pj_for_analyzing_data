import pandas as pd
import yfinance as yf


def fetch_stock_data(ticker, period):
    try:
        if period in ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]:
            stock = yf.Ticker(ticker)
            data = stock.history(period=period)
            return data
        else:
            period = period.replace("-", " ")
            period = period.replace(".", "-")
            start_period, end_period = period.split(" ", maxsplit=1)
            data = yf.download(ticker, start_period, end_period)
            return data
    except:
        return


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def rsifunc(data, periods=7):
    """
    Возвращает pd.Series с индексом относительной силы.
    """
    df = pd.DataFrame(data)
    close_delta = df['Close'].diff()

    # Делаем две серий: одну для низких закрытий и одну для высоких закрытий
    up = close_delta.clip(lower=0)
    down = -1 * close_delta.clip(upper=0)

    # Использование экспоненциальной скользящей средней
    ma_up = up.ewm(com=periods - 1, adjust=True, min_periods=periods).mean()
    ma_down = down.ewm(com=periods - 1, adjust=True, min_periods=periods).mean()

    rsi = ma_up / ma_down
    rsi = 100 - (100 / (1 + rsi))
    return rsi



# Функция для расчета стандартного отклонения
def calculate_std(data):
    '''
    :param data: DataFrame
    :return: расчет стандартного отклонения
    '''
    return data['Close'].std()
