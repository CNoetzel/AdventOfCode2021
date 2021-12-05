from enum import Enum

class Type(Enum):
    FIRST_WIN = 1,
    LAST_WIN = 0

# seperate drawn numbers and bingo board
def prepare_data(bingo_data):
    drawn_numbers = str(bingo_data[0]).strip().split(',')
    boards = []

    board = []
    for i in range(2, len(bingo_data)):
        rowValues = str(bingo_data[i]).strip().replace('  ', ' ').split(' ')
        if(len(rowValues) == 1):
            boards.append(board)
            board = []
            continue
        board_row = []
        for value in rowValues:
            board_row.append({
                'value': int(value),
                'marked': False
            })
        board.append(board_row)

    return {
        'drawn_numbers': drawn_numbers,
        'boards': boards
    }

def bingo_by_row(row_index, board):
    for entry in board[row_index]:
        if not entry['marked']: return False
    return True

def bingo_by_column(column_index, board):
    for row in board:
        if not row[column_index]['marked']: return False
    return True

def calculate_board_score(winning_number, winning_board):
    unmarked_sum = 0
    for row in winning_board:
        for entry in row:
            if not entry['marked']: unmarked_sum += int(entry['value'])
    print(f'Sum: {unmarked_sum} winning number: {winning_number}')
    return int(unmarked_sum) * int(winning_number)

def play_bingo(bingo_data, play_type):
    boards = bingo_data['boards']
    
    board_scores = [0 for i in range(len(boards))]
    last_winner = 0
    for drawn in bingo_data['drawn_numbers']:
        for board_index in range(len(boards)):
            board = boards[board_index]
            for row_index in range(len(board)):
                row = board[row_index]
                for column_index in range(len(row)):
                    entry = row[column_index]
                    has_already_won = board_scores[board_index] > 0
                    if not has_already_won and entry['value'] == int(drawn):
                        entry['marked'] = True

                        # evaluate for bingo if more that five numbers have been drawn
                        at_least_five_drawn = list(bingo_data['drawn_numbers']).index(drawn) > 4
                        if at_least_five_drawn and (bingo_by_row(row_index, board) or bingo_by_column(column_index, board)):
                            print(f'Board {board_index} identified as winner, calculating score...')
                            score = calculate_board_score(drawn, board)
                            board_scores[board_index] = score
                            last_winner = board_index
                            # return score if play type is first win otherwise proceed
                            if play_type == Type.FIRST_WIN:
                                return score
                        
    return board_scores[last_winner]

# tests
def test_diagnostics():
    f = open('day4_test_input.txt', 'r')
    test_bingo_data = f.readlines()

    prepared_data_first_win = prepare_data(test_bingo_data)
    score = play_bingo(prepared_data_first_win, Type.FIRST_WIN)
    assert score == 4512, 'should be 4512'

    prepared_data_last_win = prepare_data(test_bingo_data)
    score = play_bingo(prepared_data_last_win, Type.LAST_WIN)
    assert score == 1924, 'should be 1924'

f = open('day4_input.txt', 'r')
bingo_data = f.readlines()
prepared_data = prepare_data(bingo_data)

# part 1
prepared_data_first_win = prepare_data(bingo_data)
score_first_win = play_bingo(prepared_data_first_win, Type.FIRST_WIN)
print(f'Result for part 1 is {score_first_win}')

# part 2
prepared_data_last_win = prepare_data(bingo_data)
score_last_win = play_bingo(prepared_data_last_win, Type.LAST_WIN)
print(f'Result for part 2 is {score_last_win}')