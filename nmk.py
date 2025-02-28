#DET HÄR ÄR EN GAMMAL FIL. "new.pyt" INNEHÅLLER DEN AKTIVA KODEN.

import random
import time

def create_empty_matrix(rows, cols):
    return [[0 for _ in range(rows)] for _ in range(cols)]

def print_map(game_map):
    for row in game_map:
        print(row)


def spawn_mines(number, game_map):
    for _ in range(number):
        while True:
            row = random.randint(0, len(game_map) - 1)
            col = random.randint(0, len(game_map[0]) - 1)
            if game_map[row][col] == 0:
                game_map[row][col] = 1
                break

def create_game_map(rows, cols, mines):
    game_map = create_empty_matrix(rows, cols)
    spawn_mines(mines, game_map)
    return game_map

def check_adjacent_mines(game_map, row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if row + i < 0 or row + i >= len(game_map) or col + j < 0 or col + j >= len(game_map[0]):
                continue
            count += game_map[row + i][col + j]
    return count

def main():
    rows = 10
    cols = 10
    mines = 10
    minesDug = 0
    game_map = create_empty_matrix(rows, cols)
    game_map_hidden = create_game_map(rows, cols, mines)
    print_map(game_map)

    while True:
        row = int(input('Enter row: '))
        col = int(input('Enter col: '))
        if game_map_hidden[row][col] == 1:
            print('Game over!')
            break
        else:
            print('You are safe!')
            print(minesDug)
            adjacent_mines = check_adjacent_mines(game_map_hidden, row, col)
            game_map[row][col] = 9 if adjacent_mines == 0 else adjacent_mines
            print_map(game_map)
            minesDug += 1
            if minesDug == 5:
                print('Congratulations! You Win!')
                while True:
                    time.sleep(4)
                
            
if __name__ == '__main__':
    main()