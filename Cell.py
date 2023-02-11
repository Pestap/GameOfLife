class Cell:
    def __init__(self, position: (int, int), is_dead: bool, world):
        self.position = position
        self.is_dead = is_dead
        self.world = world

    # check if cell should change state
    def check_if_will_change_state(self) -> bool:
        neighbours = self.get_neighbours()
        alive_neighbours = [x for x in neighbours if not x.is_dead]

        # if is alive
        if not self.is_dead:
            # any cell with fewer than 2 neighbours dies
            # any cell with more than 3 neighobours dies
            if len(alive_neighbours) < 2 or len(alive_neighbours) > 3:
                return True
            # else stays alive
            else:
                return False
        # if is dead
        else:
            # if has 3 alive neighbours than becomes alive
            if len(alive_neighbours) == 3:
                return True
            # else stays dead
            else:
                return False

    def get_neighbours(self) -> list:
        neighbours = list()
        # all valid positions (around cell position)
        neighbours_positions = [(self.position[0] - 1, self.position[1] - 1),
                                (self.position[0], self.position[1] - 1),
                                (self.position[0] + 1, self.position[1] - 1),
                                (self.position[0] - 1, self.position[1]),
                                (self.position[0] + 1, self.position[1]),
                                (self.position[0] - 1, self.position[1] + 1),
                                (self.position[0], self.position[1] + 1),
                                (self.position[0] + 1, self.position[1] + 1)]

        # check for invalid positions
        neighbours_to_remove = []
        for position in neighbours_positions:
            if (position[0] < 0 or position[0] >= self.world.x_size or
                    position[1] < 0 or position[1] >= self.world.y_size):

                neighbours_to_remove.append(position)

        # subtract invalid positions from valid positions
        neighbours_positions = [x for x in neighbours_positions if x not in neighbours_to_remove]

        # determine neighbouring cells from valid positions
        for position in neighbours_positions:
            neighbours.append(self.world.world[position[0]][position[1]])

        return neighbours


