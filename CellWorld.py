from Cell import Cell
from Patterns import get_pattern

class CellWorld:
    def __init__(self, size: (int, int), pattern: str, shift: (int, int)):
        self.x_size = size[0]
        self.y_size = size[1]
        self.world = [[Cell((x, y), True, self) for y in range(self.y_size)] for x in range(self.x_size)]
        self.set_pattern(pattern, shift)

    def advance(self):
        cells_to_switch_state = []

        # get cells that will change state
        for row in self.world:
            for cell in row:
                if cell.check_if_will_change_state():
                    cells_to_switch_state.append(cell)

        # change state of cells chosen in previous step
        for cell in cells_to_switch_state:
            cell.is_dead = not cell.is_dead

    def set_pattern(self, name: str, shift: (int, int)):

        positions = get_pattern(name, shift)

        for pos in positions:
            self.world[pos[0]][pos[1]].is_dead = False

