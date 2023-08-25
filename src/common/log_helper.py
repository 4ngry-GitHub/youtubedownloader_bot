from abc import ABC, abstractmethod
from enum import Enum

import loguru

from settings import settings


class LoggerBase(ABC):
    @abstractmethod
    def get_logger(self):
        """method should return logger object."""
        pass


class LogLevel(Enum):
    NOTSET = 0
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50

    def __init__(self, log_level) -> None:
        super().__init__()
        self.log_level = log_level

    def get_level_as_int(self) -> int:
        """
        :param log_level: string log level
        :return: value log_level in integer (10, 20, 30, 40, 50) or 0
        """
        if not isinstance(self.log_level, str):
            return 0
        
        log_level_dict: dict = {
            "NONSET": self.NOTSET.value,
            "DEBUG": self.DEBUG.value,
            "INFO": self.INFO.value,
            "WARNING": self.WARNING.value,
            "ERROR": self.ERROR.value,
            "CRITICAL": self.CRITICAL.value
            }
        
        return log_level_dict.get(self.log_level.upper(), 0)
    
    def get_level_as_str(self) -> str:
        """
        :param log_level: int log level
        :return: value log_level in string (DEBUG, INFO, WARNING, ERROR, CRITICAL) or NONSET
        """
        if not isinstance(self.log_level, int):
            return "NONSET"
        
        log_level_dict: dict = {
            self.NOTSET.value: "NONSET",
            self.DEBUG.value: "DEBUG",
            self.INFO.value: "INFO",
            self.WARNING.value: "WARNING",
            self.ERROR.value: "ERROR",
            self.CRITICAL.value: "CRITICAL"
            }
        
        return log_level_dict.get(self.log_level, "NONSET")


class Logger(LoggerBase):
    def __init__(self, logger_object, log_level = None) -> None:
        self.logger =  logger_object
        # self.log_level = LogLevel(log_level)
        # self.logger.level = self.log_level.get_level_as_int()
    
    def get_logger(self):
        return self.logger


logger = Logger(loguru.logger, settings.log_level)


def get_logger():
    return logger.get_logger()
