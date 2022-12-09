from day_09.field import Field

TEST_INPUT = """\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""


def parse_input(input_string: str):

    for line in input_string.split("\n"):
        direction, num_moves = line.split(" ")
        yield direction, int(num_moves)


def solve_a(input_string=TEST_INPUT):
    field = Field()
    moves = parse_input(input_string)

    for move in moves:
        field.move_n(*move)

    field.print_visited()
    return len(field.tail_history)


def solve_b(input_string=TEST_INPUT):
    return parse_input(input_string)
