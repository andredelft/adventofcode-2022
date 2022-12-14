import click
from datetime import datetime
from aocd import get_data, submit as aocd_submit
from pathlib import Path
import yaml
import importlib


TEMPLATE = """TEST_INPUT = \"\"\"\\
\"\"\"


def parse_input(input_string: str):
    return input_string


def solve_a(input_string=TEST_INPUT):
    parse_input(input_string)


def solve_b(input_string=TEST_INPUT):
    parse_input(input_string)
"""

TEST_TEMPLATE = """from {day_path}.{module_name} import solve_a, solve_b

EXPECTED_SOLUTION_A = None
EXPECTED_SOLUTION_B = None


def test_a():
    assert solve_a() == EXPECTED_SOLUTION_A


def test_b():
    assert solve_b() == EXPECTED_SOLUTION_B
"""

TODAY = datetime.now().day

ENTRYPOINTS_FILENAME = "entrypoints.yaml"
with open(ENTRYPOINTS_FILENAME) as f:
    ENTRYPOINTS = yaml.safe_load(f)


def update_entrypoints():
    with open(ENTRYPOINTS_FILENAME, "w") as f:
        yaml.safe_dump(ENTRYPOINTS, f)


def get_day_path(day: int):
    return Path(f"day_{day:02d}")


def get_module_name(day: int) -> str | None:
    return ENTRYPOINTS.get(day, None)


def get_solution(part: str, day: int, input_string: str | None = None):
    module_name = get_module_name(day)
    if not module_name:
        click.BadParameter(f"Day {day} is not initialized yet")

    m = importlib.import_module(f"{get_day_path(day)}.{module_name}")
    solve = getattr(m, f"solve_{part}")
    return solve(input_string) if input_string else solve()


arg_module_name = click.argument("module_name")
arg_part = click.argument("part", type=click.Choice(["a", "b"]))
arg_day = click.argument("day", default=TODAY, type=int)


@click.command()
@arg_module_name
@arg_day
def prepare(module_name, day):
    day_path = get_day_path(day)
    day_path.mkdir(exist_ok=True)

    with open(day_path / "input.txt", "w") as f:
        f.write(get_data(day=day))

    with open(day_path / f"{module_name}.py", "w") as f:
        f.write(TEMPLATE)

    with open(day_path / f"test_{module_name}.py", "w") as f:
        f.write(TEST_TEMPLATE.format(module_name=module_name, day_path=day_path))

    ENTRYPOINTS[day] = module_name
    update_entrypoints()


@click.command()
@arg_part
@arg_day
def test(part, day):
    click.echo(get_solution(part, day))


@click.command()
@arg_part
@arg_day
def solve(part, day):
    with open(get_day_path(day) / "input.txt") as f:
        click.echo(get_solution(part, day, f.read()))


@click.command()
@arg_part
@arg_day
def submit(part, day):
    with open(get_day_path(day) / "input.txt") as f:
        solution = get_solution(part, day, f.read())
        if solution == None:
            click.echo("Nothing to submit")
            return
        aocd_submit(solution, part=part, day=day)
