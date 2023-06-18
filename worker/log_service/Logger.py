from enum import Enum
from datetime import datetime


class LoggerMethod(Enum):
    CREATE = 0
    UPDATE = 1
    DELETE = 2


def logger(log_info: LoggerMethod, msg: str, output_file_path: str = 'log.txt'):
    """Декоратор записывающий действия над бд в файл
    log_info: LoggerMethod(CREATE,UPDATE,DELETE) - Действие обертываемой функции
    msg: str - сообщение в лог
    output_file_path: str - файл для вывода логов (по умолчанию log.txt в этой же папке"""
    def decorator(function):

        def wrapped_function_args(request):
            time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
            with open(output_file_path, 'a') as fw:

                function(request)
                print(log_info.name, time, msg, file=fw)

            return function(request)
        return wrapped_function_args
    return decorator
