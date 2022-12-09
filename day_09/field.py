import time


class OutOfBounds(Exception):
    pass


class Field(object):
    width = 20
    height = 30

    start = [height // 2, width // 2]

    head = start.copy()
    tail = start.copy()

    tail_history = set([tuple(tail)])

    def print(self, vert=(0, width), hor=(0, height)):
        lines = []
        for i in range(*vert):
            line = ""
            for j in range(*hor):
                if [i, j] == self.head:
                    line += "H"
                elif [i, j] == self.tail:
                    line += "T"
                elif [i, j] == self.start:
                    line += "s"
                else:
                    line += "."
            lines.append(line)
        print("\n".join(lines))

    def print_visited(self):
        # Find dimensions of the field
        vert = [0, 0]
        hor = [0, 0]
        for coord in self.tail_history:
            if coord[0] < vert[0]:
                vert[0] = coord[0]
            elif coord[0] > vert[1]:
                vert[1] = coord[0]
            if coord[1] < hor[0]:
                hor[0] = coord[1]
            elif coord[1] > hor[1]:
                hor[1] = coord[1]

        lines = []
        for i in range(*vert):
            line = ""
            for j in range(*hor):
                if (i, j) in self.tail_history:
                    line += "#"
                else:
                    line += "."
            lines.append(line)
        print("\n".join(lines))

    def check_within_bounds(self):
        for i, j, name in [[*self.head, "Head"], [*self.tail, "Tail"]]:
            if not (0 <= i < self.height or 0 <= j < self.width):
                raise OutOfBounds(f"{name} is out of bounds: {(i,j)}")

    def move(self, direction, print_step=False):
        match direction:
            case "U":
                self.head[0] -= 1
            case "R":
                self.head[1] += 1
            case "D":
                self.head[0] += 1
            case "L":
                self.head[1] -= 1

        # Calculate tail position
        delta_y = self.head[0] - self.tail[0]
        delta_x = self.head[1] - self.tail[1]

        if delta_y > 1:
            self.tail = [self.head[0] - 1, self.head[1]]
        elif delta_y < -1:
            self.tail = [self.head[0] + 1, self.head[1]]
        elif delta_x > 1:
            self.tail = [self.head[0], self.head[1] - 1]
        elif delta_x < -1:
            self.tail = [self.head[0], self.head[1] + 1]

        self.tail_history.add(tuple(self.tail))

        if print_step:
            self.check_within_bounds()
            self.print()
            print("\n")
            time.sleep(0.1)

    def move_n(self, direction, num_moves, print_steps=False):
        for _ in range(num_moves):
            self.move(direction, print_steps)
