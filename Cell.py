from CellWorld import CellWorld

class Cell:
    def __init__(self, position: (int, int), is_dead: bool, world: CellWorld):
        self.position = position
        self.is_dead = is_dead
        self.world = world

    def check_if_will_change_state(self) -> bool:
        neighbours = self.get_neighbours()
        alive_neighbours = [x for x in neighbours if not x.is_dead]


        if not self.is_dead: # if is alive
            # any cell with fewer than 2 neighbours dies
            # any cell with more than 3 neighobours dies
            if len(alive_neighbours) < 2 or len(alive_neighbours) > 3:
                return True
            else: # else stays alive
                return False
        else: # if is dead
            if len(alive_neighbours) == 3: # if has 3 alive neighbours than becomes alive
                return True
            else: # else stays dead
                return False



    # Get all neighbours of cell
    def get_neighbours(self) -> list:
        neighbours = list[Cell]
        # all neighbours
        neighbours_positions = [(self.position[0] - 1, self.position[1] - 1),
                                    (self.position[0], self.position[1] - 1)
                                    (self.position[0] + 1, self.position[1] - 1)
                                    (self.position[0] - 1, self.position[1])
                                    (self.position[0] + 1, self.position[1])
                                    (self.position[0] - 1, self.position[1] + 1)
                                    (self.position[0], self.position[1] + 1)
                                    (self.position[0] + 1, self.position[1] + 1)]

        #check for non-existing neighbours and delete them from neighbour list
        for position in neighbours_positions:
            if (position[0] < 0 or position[0] >= self.world.x_size or
                position[1] < 0 or position[1] >= self.world.y_size):
                neighbours_positions.remove(position)


        return neighbours

