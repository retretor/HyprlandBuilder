# logger.py

from time import ctime
from enum import Enum, auto

class LoggerStatus(Enum):
    ERROR = auto()
    SUCCESS = auto()

# ANSI escape sequences for colors
COLOR_RESET = "\033[0m"
COLOR_GREEN = "\033[32m"
COLOR_RED = "\033[31m"
COLOR_BOLD = "\033[1m"

class Logger:
    filename = "build_debug.log"

    @staticmethod
    def add_record(text: str, *, status: LoggerStatus = LoggerStatus.SUCCESS) -> None:
        time_str = ctime()
        if status == LoggerStatus.ERROR:
            # Red color for errors
            formatted_text = f"{COLOR_RED}[ERROR] | {text} | {time_str}{COLOR_RESET}\n"
        else:
            # Green color for success / normal messages
            formatted_text = f"{COLOR_GREEN}[OK]   | {text} | {time_str}{COLOR_RESET}\n"

        print(formatted_text, end='')

        with open(Logger.filename, "a", encoding="UTF-8") as file:
            file.write(formatted_text)
