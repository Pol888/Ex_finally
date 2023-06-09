class LessDataError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"LessDataError, {self.message}"
        else:
            return "Мало данных"

class MoreDataError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"LessDataError, {self.message}"
        else:
            return "Много данных"

class NameError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"LessDataError, {self.message}"
        else:
            return "Данные о ФИО не корректные"


class DateError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"LessDataError, {self.message}"
        else:
            return "Данные о дате не корректные"

class GenderError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"LessDataError, {self.message}"
        else:
            return "Данные о поле не корректные"

class TelError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"LessDataError, {self.message}"
        else:
            return "Данные о телефоне не корректные"