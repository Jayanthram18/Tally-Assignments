from abc import ABC, abstractmethod

class BaseLogger(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def log_entry(self, date, name, work_done):
        pass
