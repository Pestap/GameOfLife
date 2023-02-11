from Cell import Cell
class CellWorld:
    def __init__(self, size: (int, int)):
        self.x_size = size[0]
        self.y_size = size[1]

        self.world = [[Cell((x, y), True, self) for x in range(self.x_size)] for y in range(self.y_size)]

    def advance(self):
        cells_to_switch_state = [cell for cell in self.world if cell.check_if_will_change_state()]

        for cell in cells_to_switch_state:
            cell.is_dead = not cell.is_dead

    def set_pattern(self, pattern_name: str):



