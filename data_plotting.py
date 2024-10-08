import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl


import data_download


def create_and_save_plot(data, ticker, period, style="fivethirtyeight", filename=None):
    """
    :param data: - DataFrame
    :param ticker: - Тикер акции
    :param period: - Периоды времени для данных
    :param style: - Стиль оформления графика
    :param filename: - Имя файла для сохранения данных
    :return: - Возвращаем построенный график согласно введенным параметрам и сохраняем согласно заданному имени
    """
    plt.figure(figsize=(16, 6))
    plt.style.use([style])

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
            rsi_series = data_download.rsifunc(data)
            plt.plot(rsi_series, label='RSI')
            # Вычисление стандартного отклонения
            std_close = data_download.calculate_std(data)
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')
        rsi_series = data_download.rsifunc(data)
        plt.plot(rsi_series, label='RSI')
        # Вычисление стандартного отклонения
        std_close = data_download.calculate_std(data)

    plt.title(f"{ticker} Цена акций с течением времени + RSI Indicator")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    # Добавление информации о стандартном отклонении под графиком
    plt.text(0.9, 0.3, f'Стандартное отклонение: ${std_close:.2f}', ha='right', va='bottom', transform=plt.gca().transAxes)
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    plt.show()
    print(f"График сохранен как {filename}")


def calculate_and_display_average_price(data):

    '''
    :param data: - DataFrame
    :return: - возвращаем среднюю цену закрытия акций за заданный период
    '''

    return data['Close'].mean()


def notify_if_strong_fluctuations(data, threshold):

    '''
    :param data: - DataFrame
    :param threshold: - порог колебания цен в данный период
    :return: - возвращаем процент колебания цена от заданного порога
    '''

    max_ = data['Close'].max()
    min_ = data['Close'].min()
    difference_max_min = max_ - min_

    if difference_max_min > threshold:
        return round(((difference_max_min*100)/threshold)-100, 2)
    else:
        return 0


def export_data_to_csv(data, filename):
    """
    :param data:  - DataFrame
    :param filename: - имя файла
    :return: - текст файл сохранен
    """
    if filename == 'Close':
        print('Работа программы завершена')
    else:
        # Создаем DataFrame из данных
        df = pd.DataFrame(data)
        # Сохраняем DataFrame в CSV файл
        df.to_csv(filename, index=True)
        print(f'Данные сохранены в файл {filename}. Работа программы завершена')

