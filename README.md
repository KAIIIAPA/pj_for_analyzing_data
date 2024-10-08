Документация проекта для анализа и визуализации данных об акциях

Общий обзор

Этот проект предназначен для загрузки исторических данных об акциях и их визуализации. Он использует библиотеку yfinance для получения данных и matplotlib для создания графиков. Пользователи могут выбирать различные тикеры и временные периоды для анализа, а также просматривать движение цен и скользящие средние на графике.


Структура и модули проекта

1. data_download.py:

- Отвечает за загрузку данных об акциях.

- Содержит функции для извлечения данных об акциях из интернета и расчёта скользящего среднего.


2. main.py:

- Является точкой входа в программу.

- Запрашивает у пользователя тикер акции, временной период и стиль графика, загружает данные, обрабатывает их и выводит результаты в виде графика.


3. data_plotting.py:

- Отвечает за визуализацию данных.

- Содержит функции для создания и сохранения графиков цен закрытия и скользящих средних.


Описание функций


1. data_download.py:

- fetch_stock_data(ticker, period): Получает исторические данные об акциях для указанного тикера и временного периода. Возвращает DataFrame с данными.

- add_moving_average(data, window_size): Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия.

- def rsifunc(data, periods=7): Вычисление RSI с использованием экспоненциальной скользящей средней (EMA).

- def calculate_std(data): Вычисление стандартного отклонения.


2. main.py:

- main(): Основная функция, управляющая процессом загрузки, обработки данных и их визуализации. Запрашивает у пользователя ввод данных, вызывает функции загрузки и обработки данных, а затем передаёт результаты на визуализацию.


3. data_plotting.py:

- create_and_save_plot (data, ticker, period, style="fivethirtyeight", filename=None): Создаёт график, отображающий цены закрытия, скользящие средние и технический индекатор RSI. Предоставляет возможность выбора стиля графика и сохранения его в файл. Параметр filename опционален; если он не указан, имя файла генерируется автоматически.

- calculate_and_display_average_price(data), функция которая вычисляет и выводит в консоль среднюю цену закрытия акций за заданный период

- notify_if_strong_fluctuations(data, threshold), функция которая вычисляет максимальное и минимальное значения цены закрытия и сравнивать разницу с заданным порогом. Если разница превышает порог, пользователь получает уведомление в консоль.
  
- export_data_to_csv(data, filename), функция будет сохранять данные в указанный SCV файл.

Пошаговое использование

1. Запустите main.py.

2. Введите интересующий вас тикер акции (например, 'AAPL' для Apple Inc).
3. Введите желаемый временной период для анализа (например, '1mo' для данных за один месяц или период времени 2023.01.01-2023.08.01).
4. Введите стиль оформления графика (по умолчанию установлен: fivethirtyeight). Например, 'fast'.
5. Программа обработает введённые данные, загрузит соответствующие данные об акциях, рассчитает скользящее среднее и отобразит график.

![image](https://github.com/user-attachments/assets/2d959032-8d4b-4805-b524-598a029036c9)

6. Вычисляет и выводит в консоль среднюю цену закрытия акций за заданный период

![image](https://github.com/user-attachments/assets/9cb2762a-dd5b-490a-b67b-983379839733)

7. Введите порог колебания цен в данный период (например, 17). Если разница превышает порог, пользователь получает уведомление в консоль.

![image](https://github.com/user-attachments/assets/706bafe1-83e1-40ef-880b-c8953d4de44d)

8. Для сохранення данных введите имя файла. Если Вы хотите завершить работу программы ввете "Close"

![image](https://github.com/user-attachments/assets/5cd435a8-abf5-4e99-85ce-189acd01057d)

Задания нацелены на улучшение пользовательского опыта и расширение аналитических возможностей проекта, предоставляя глубокие и настраиваемые инструменты для анализа данных об акциях.
