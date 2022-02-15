def board_dims():
    while True:
        dimensions = input("Enter your board dimensions:").split()
        if ''.join(dimensions).isdigit() and \
            len(dimensions) == 2 and \
            int(dimensions[0]) > 0 and int(dimensions[1]) > 0:
            cols = int(dimensions[0])
            rows = int(dimensions[1])
            break
        else:
            print("Invalid dimensions!")
            continue
    return cols, rows


def create_board(cols, rows, digits):
    return [["_" * digits] * cols for _ in range(rows)]


def create_board_slots(cols, rows):
    return [[[i + 1, j + 1] for i in range(cols)] for j in reversed(range(rows))]


def find_in_list_of_list(mylist, char):
    for sub_list in mylist:
        if char in sub_list:
            return (mylist.index(sub_list), sub_list.index(char))
    raise ValueError("'{char}' is not in list".format(char = char))


def locate_knight():
    while True:
        start_pos = input("Enter the knight's starting position:").split()
        if ''.join(start_pos).isdigit() and \
                len(start_pos) == 2 and \
                0 < int(start_pos[0]) <= cols and 0 < int(start_pos[1]) <= rows:
            start_pos = [int(x) for x in start_pos]
            location = find_in_list_of_list(board_slots, start_pos)
            board[location[0]][location[1]] = 'X'.rjust(digits)
            break
        else:
            print("Invalid position!")
    return start_pos


def possible_moves(start_pos):
    list_moves = []
    list_moves.append([start_pos[0] + 2, start_pos[1] + 1])
    list_moves.append([start_pos[0] + 2, start_pos[1] - 1])
    list_moves.append([start_pos[0] - 2, start_pos[1] + 1])
    list_moves.append([start_pos[0] - 2, start_pos[1] - 1])
    list_moves.append([start_pos[0] + 1, start_pos[1] + 2])
    list_moves.append([start_pos[0] + 1, start_pos[1] - 2])
    list_moves.append([start_pos[0] - 1, start_pos[1] + 2])
    list_moves.append([start_pos[0] - 1, start_pos[1] - 2])
    board_slots_flat = [x for y in board_slots for x in y]
    list_moves = [x for x in list_moves if x in board_slots_flat]
    return list_moves


def update_board(moves):
    for i in range(len(moves)):
        avail_pos = len(possible_moves(moves[i])) - 1
        location = find_in_list_of_list(board_slots, moves[i])
        board[location[0]][location[1]] = str(avail_pos).rjust(digits)


def print_board():
    total_spaces = digits_start + 2 + len(" ".join(board[0])) + 2
    print_dashes = " " * digits_start + "-" * (total_spaces - digits_start)
    nums = [i for i in range(1, cols + 1)]
    nums_idx = [i for i in range(digits_start + 1 + digits, total_spaces, digits + 1)]
    nums_idx = [nums_idx[0]] if len(nums) == 1 else nums_idx
    empt_str = [" "] * total_spaces
    count = 0
    for i in range(total_spaces):
        if i in nums_idx:
            empt_str[i] = str(nums[count])
            count += 1
    cols_print = "".join(empt_str)
    print(print_dashes)
    for i in range(rows):
        # print(i)
        print_num = rows - i
        spaces = len(str(max(nums))) - len(str(print_num))
        print(f"{' ' * spaces}{print_num}| {' '.join(board[i])} |")
    print(print_dashes)
    print(cols_print)


cols, rows = board_dims()
digits = len(str(cols * rows))
digits_start = len(str(rows))
board = create_board(cols, rows, digits)
board_slots = create_board_slots(cols, rows)
start_pos = locate_knight()
moves = possible_moves(start_pos)
update_board(moves)
print()
print("Here are the possible moves:")
print_board()

# other
# def get_dimensions():
#     while True:
#         try:
#             _cols, _rows = [int(num) for num in input('Enter your board dimensions:').split()]
#             assert _cols > 0 and _rows > 0
#         except (TypeError, ValueError, AssertionError):
#             print("Invalid dimensions!")
#         else:
#             return _cols, _rows
#
#
# def get_position():
#     while True:
#         try:
#             _x, _y = [int(num) for num in input("Enter the knight's starting position:").split()]
#             assert 1 <= _x <= cols and 1 <= _y <= rows
#         except (TypeError, ValueError, AssertionError):
#             print("Invalid position!")
#         else:
#             return _x, _y
#
#
# def get_cell_size():
#     if cols == 1:
#         return 1
#     elif cols < 9:
#         return 2
#     else:
#         return 3
#
#
# def get_possible_moves(start_x, start_y):
#     steps = [[2, 1], [2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2], [-2, -1], [-2, 1]]
#     moves = []
#     for i in range(8):
#         _x = start_x + steps[i][0]
#         _y = start_y + steps[i][1]
#         if _x in range(1, cols + 1) and _y in range(1, rows + 1):
#             moves.append([_x, _y])
#     return moves
#
#
# def draw_possible_moves(_knight_moves):
#     for [_x, _y] in _knight_moves:
#         num_moves = len(get_possible_moves(_x, _y)) - 1
#         matrix[rows - _y][_x - 1] = ' ' * (cell_size - 1) + str(num_moves)
#
#
# def print_matrix(_matrix):
#     sep_line = '-' * (cols * 3 + 3)  # '---------------' length depends on number_of_columns
#     print(f' {sep_line}')
#     for i in range(rows):
#         print(rows - i, end='')
#         print('|', *_matrix[i], '|')
#     print(f' {sep_line}')
#     bottom_line = [i for i in range(1, cols + 1)]  # '   1 2 3 ...... number_of_columns'
#     print('  ', *bottom_line, sep=' ' * cell_size)
#
#
# cols, rows = get_dimensions()
# x, y = get_position()
#
# cell_size = get_cell_size()
# default_cell = '_' * cell_size  # depend on columns number default cell = '_' or '__' or '___'
# matrix = [[default_cell] * cols for _ in range(rows)]  # create empty matrix(board)
# matrix[rows - y][x - 1] = ' ' * (cell_size - 1) + 'X'  # draw start position on the board
#
# knight_moves = get_possible_moves(x, y)
# draw_possible_moves(knight_moves)
#
# print("\nHere are the possible moves:")
# print_matrix(matrix)