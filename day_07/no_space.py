from day_07.file_system import parse_terminal_output, FileSystem

TEST_INPUT = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


def parse_input(input_string):
    input_stream = parse_terminal_output(input_string)
    fs = FileSystem.from_stream(input_stream)
    return fs


def solve_a(input_string=TEST_INPUT):
    fs = parse_input(input_string)
    cumulative_size = 0
    for name, cdir in fs.walk():
        if isinstance(cdir[name], dict):
            size = fs.size(name, cdir)
            if size < 100000:
                cumulative_size += size

    return cumulative_size


def solve_b(input_string=TEST_INPUT):
    fs = parse_input(input_string)
    total_size = sum(fs.size(name) for name in fs.ls())
    unused_space = 70_000_000 - total_size
    necessary_space = 30_000_000 - unused_space
    smallest_deletable_size = 30_000_000
    for name, cdir in fs.walk():
        if isinstance(cdir[name], dict):
            size = fs.size(name, cdir)
            if size >= necessary_space and size < smallest_deletable_size:
                smallest_deletable_size = size

    return smallest_deletable_size

    return parse_input(input_string)
