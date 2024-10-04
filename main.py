import data_download as dd
import data_plotting as dplt


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), "
          "MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, "
          "макс. Также период времени может принимать конкретные даты начала и окончания")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc): ")
    period = input(("Введите период для данных или конкретные даты начала и окончания "
                    "(например, '1mo' для одного месяца или 2016.01.01-2016.06.01): "))

    # Fetch stock data
    try:
        stock_data = dd.fetch_stock_data(ticker, period)
        # Add moving average to the data
        stock_data = dd.add_moving_average(stock_data)
        # Plot the data
        dplt.create_and_save_plot(stock_data, ticker, period)

        # вычисляем и выводит среднюю цену закрытия акций за заданный период
        average_price = dplt.calculate_and_display_average_price(stock_data)
        print(f'Средняя цена акций {ticker} за период {period} оставляет {round(average_price, 2)}')

        # Вычисляем максимальное и минимальное значения цены закрытия и сравнивать разницу с заданным порогом. Если
        # разница превышает порог, пользователь получает уведомление.
        threshold = int(input("Введите порог колебания цен в данный период (например, 17): "))
        if dplt.notify_if_strong_fluctuations(stock_data, threshold) > 0:
            print(
                f'Цена акций за период {period} колебалась на {dplt.notify_if_strong_fluctuations(stock_data, threshold)}% '
                f'выше от заданного порога {threshold}')
        else:
            print(f'Цена акций за период {period} не превышала заданного порога {threshold}')

        # Cохраняем загруженные данные об акциях в CSV файл
        filename = input("Введите имя файла для сохранения данных (пример, My_file): ")
        dplt.export_data_to_csv(stock_data, filename=filename + ".csv")
    except:
        print("Были введены некорректные данные даты")


if __name__ == "__main__":
    main()
