from abc import ABC, abstractmethod

class BaseLogger(ABC):
    def __init__(logger_details):
        logger_details._date = None 
        logger_details._name = None 
        logger_details._work_done = None 

    @property
    def date(logger_details):
        return logger_details._date

    @date.setter
    def date(logger_details, value):
        logger_details._date = value

    @property
    def name(logger_details):
        return logger_details._name

    @name.setter
    def name(logger_details, value):
        if not all(word.isalnum() for word in value.split()):
            raise ValueError("Name must contain only alphanumeric characters and spaces.")  
        if len(value.split()) > 100: 
            raise ValueError("Name cannot exceed 100 words.")  
        logger_details._name = value  

    @property
    def work_done(logger_details):
        return logger_details._work_done

    @work_done.setter
    def work_done(logger_details, value):
        if not all(word.isalnum() for word in value.split()):
            raise ValueError("Task must contain only alphanumeric characters and spaces.") 
        if len(value.split()) > 100: 
            raise ValueError("Task description cannot exceed 100 words.")
        logger_details._work_done = value 

    @abstractmethod
    def connect(logger_details):
        pass

    @abstractmethod
    def log_entry(logger_details):
        pass
