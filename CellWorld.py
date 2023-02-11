from Cell import Cell
class CellWorld:
    def __init__(self, size: (int, int), pattern: str):
        self.x_size = size[0]
        self.y_size = size[1]

        self.world = [[Cell((x, y), True, self) for y in range(self.y_size)] for x in range(self.x_size)]

        self.set_pattern(pattern)

    # self.world.world[position[0]][position[1]]
    def advance(self):
        cells_to_switch_state = [] # [cell for cell in row if cell.check_if_will_change_state() for row in self.world]]

        for row in self.world:
            for cell in row:
                if cell.check_if_will_change_state():
                    cells_to_switch_state.append(cell)

        for cell in cells_to_switch_state:
            print(cell.is_dead)
            cell.is_dead = not cell.is_dead
            print(cell.is_dead)

    def set_pattern(self, pattern_name: str):
        if pattern_name == 'blinker':
            self.world[4][1].is_dead = False
            self.world[4][2].is_dead = False
            self.world[4][3].is_dead = False
        elif pattern_name == 'glider':
            self.world[4][2].is_dead = False
            self.world[5][3].is_dead = False
            self.world[6][1].is_dead = False
            self.world[6][2].is_dead = False
            self.world[6][3].is_dead = False

