"""Практика в написании пакетов и модулей и игры крстики-нолики."""
from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def main():
    """Основная исполняемая функция кода и логика игры."""
    game = Board()
    current_player = 'X'
    running = True
    game.display()
    while running:
        print(f'Ход делают {current_player}')
        while True:
            try:
                row = int(input('Введите номер строки: '))
                if not 0 <= row < game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if not 0 <= column < game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}'
                )
                print(
                    'Пожалуйста, введите значения для строки и столбца снова.')
                continue
            except CellOccupiedError:
                print('Ячейка занята.')
                print('Введите другие координаты.')
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print(
                  'Пожалуйста, введите значения для строки и столбца заново.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
                continue
            else:
                break
        game.make_move(row, column, current_player)
        print('Ход сделан!')
        game.display()
        if game.check_win(current_player):
            winner_line = f'Победили {current_player}.'
            print(winner_line)
            game.save_result(winner_line)
            running = False
        if game.is_board_full():
            winner_line = 'Ничья!'
            print(winner_line)
            game.save_result(winner_line)
            running = False
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
