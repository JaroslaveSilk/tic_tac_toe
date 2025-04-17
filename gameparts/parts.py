"""Модуль с классами для практики в написании игр."""


class Board:
    """Класс, который описывает игровое поле."""

    field_size = 3

    def __init__(self):
        self.board = [
          [' ' for _ in range(self.field_size)] for _ in range(self.field_size)
        ]

    def make_move(self, row, col, player):
        """Метод, который обрабатывает ходы игроков."""
        self.board[row][col] = player

    def display(self):
        """Метод, который отрисовывает игровое поле."""
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def is_board_full(self):
        """Метод проверяющий заполнено ли поле."""
        for i in range(self.field_size):
            for j in range(self.field_size):
                if self.board[i][j] == ' ':
                    return False
        return True

    def check_win(self, player):
        """Метод проверки победителя"""
        for i in range(self.field_size):
            if (all([self.board[i][j] == player
                     for j in range(self.field_size)])
                    or
                    all([self.board[j][i] == player
                         for j in range(self.field_size)])):
                # Проверка по вертикали и горизонтали.
                return True

        if (all([self.board[i][i] == player
                 for i in range(self.field_size)])
                or all([self.board[i][self.field_size - 1 - i] == player
                        for i in range(self.field_size)])):
            # Проверка по диагонали.
            return True

        return False

    def save_result(self, statistics_line: str):
        """Метод записывающий резултаты игр в файл для статистики"""
        file = open('win_statistics.txt', 'a', encoding='utf-8')
        file.write(statistics_line + '\n')
        file.close()

    def __str__(self):
        """Метод, который выводит информацию о размерах игрового поля."""
        return (
            'Объект игрового поля размером'
            f'{self.field_size}x{self.field_size}'
        )


# Создать игровое поле - объект класса Board.
# game = Board()
# Отрисовать поле в терминале.
# game.display()
# Разместить на поле символ по указанным координатам - сделать ход.
# game.make_move(1, 1, 'X')
# print('Ход сделан!')
# Перерисовать поле с учётом сделанного хода.
# game.display()
