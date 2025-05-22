from abc import ABC, abstractmethod

class BaseLogger(ABC):
    def __init__(self):
        self._date = None
        self._name = None
        self._work_done = None

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.replace(" ", "").isalnum():
            raise ValueError(" Name must contain only alphanumeric characters and spaces.")
        self._name = value

    @property
    def work_done(self):
        return self._work_done

    @work_done.setter
    def work_done(self, value):
        if not value.replace(" ", "").isalnum():
            raise ValueError(" Task must contain only alphanumeric characters and spaces.")
        self._work_done = value

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def log_entry(self):
        pass
