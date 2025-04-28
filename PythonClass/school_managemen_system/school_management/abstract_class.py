from abc import ABC, abstractmethod

class User(ABC):

    def __init__(self, first_name: str, last_name: str, email:str):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__full_name = first_name + ' ' + last_name

    def get_first_name(self) -> str:
        return self.__first_name

    def get_last_name(self) -> str:
        return self.__last_name

    def get_email(self) -> str:
        return self.__email

    def get_full_name(self) -> str:
        return self.__full_name

    @abstractmethod
    def user_info(self):
        pass