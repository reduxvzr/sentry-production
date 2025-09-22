import sentry_sdk
import random
import time

# Инициализация Sentry SDK с DSN
sentry_sdk.init(
    dsn="https://dsn_number@sentry-k8s.travellata.ru/2",
    debug=True,
    environment="development_test",
    release="my-app@1.0.0",
)

def divide_by_zero():
    """Функция, которая вызывает ZeroDivisionError."""
    return 1 / 0

def index_error():
    """Функция, которая вызывает IndexError."""
    lst = []
    return lst[1]

def key_error():
    """Функция, которая вызывает KeyError."""
    dct = {}
    return dct['missing']

def send_test_message():
    """Отправка тестового сообщения в Sentry."""
    sentry_sdk.capture_message("Это случайное тестовое сообщение без ошибки!")

def do_work():
    """Функция, которая выполняет 'рабочие' действия без ошибок."""
    print("Все прошло успешно! Никаких ошибок")

def generate_random_behavior():
    """Случайным образом вызывает ошибку или нет."""
    choice = random.choice(['zero_division', 'index_error', 'key_error', 'message', 'ok'])
    
    print(f"Выбран сценарий: {choice}")
    
    try:
        if choice == 'zero_division':
            divide_by_zero()
        elif choice == 'index_error':
            index_error()
        elif choice == 'key_error':
            key_error()
        elif choice == 'message':
            send_test_message()
        elif choice == 'ok':
            do_work()
    except Exception as e:
        sentry_sdk.capture_exception(e)
        print(f"Исключение перехвачено и отправлено в Sentry: {type(e).__name__}")

if __name__ == "__main__":
    print("Запуск тестового скрипта Sentry...")
    try:
        minutes = float(input("Введите время работы скрипта в минутах: "))
        total_seconds = minutes * 60
    except ValueError:
        print("Неверный формат. Используйте число, например: 1.5 или 0.5")
        exit(1)

    start_time = time.time()

    while time.time() - start_time < total_seconds:
        generate_random_behavior()
        time.sleep(2)  # Задержка между событиями для имитации реальной работы

    print(f"Время работы {minutes} минут истекло. Скрипт завершен.")
