"""Модуль с исключениями для игры крестики-нолики."""


class FieldIndexError(IndexError):
    """Выбрасывается, если указано значение вне поля."""
    def __init__(self,
                 message='Введено значение за пределами игрововго поля!'):
        super().__init__(message)


class CellOccupiedError(ValueError):
    """Выбрасывается при попытке хода в уже занятую клетку."""
    def __init__(self,
                 message='Попытка изменить занятую ячейку.'):
        super().__init__(message)
