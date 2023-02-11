

def get_pattern(name: str, shift: (int, int)) -> list[(int, int)]:
    if name == 'blinker':
        return get_blinker_pattern(shift)
    elif name == 'toad':
        return get_toad_pattern(shift)
    elif name == 'beacon':
        return get_beacon_pattern(shift)
    elif name == 'pulsar':
        return get_pulsar_pattern(shift)


def get_blinker_pattern(shift: (int, int)) -> list[(int, int)]:
    shift_x = shift[0]
    shift_y = shift[1]
    # defined blinker pattern
    return [(shift_x, shift_y),
            (shift_x, shift_y + 1),
            (shift_x, shift_y + 2)]


def get_toad_pattern(shift: (int, int)) -> list[(int, int)]:
    shift_x = shift[0]
    shift_y = shift[1]
    # defined toad pattern
    return [(shift_x, shift_y + 1),
            (shift_x, shift_y + 2),
            (shift_x + 1, shift_y + 3),
            (shift_x + 2, shift_y),
            (shift_x + 3, shift_y + 1),
            (shift_x + 3, shift_y + 2)]


def get_beacon_pattern(shift: (int, int)) -> list[(int, int)]:
    shift_x = shift[0]
    shift_y = shift[1]
    # defined beacon pattern
    return [(shift_x, shift_y),
            (shift_x + 1, shift_y),
            (shift_x, shift_y + 1),
            (shift_x + 1, shift_y + 1),
            (shift_x + 2, shift_y + 2),
            (shift_x + 3, shift_y + 2),
            (shift_x + 2, shift_y + 3),
            (shift_x + 3, shift_y + 3)]

def get_pulsar_pattern(shift: (int, int)) -> list[(int, int)]:
    shift_x = shift[0]
    shift_y = shift[1]
    # defined pulsar patter
    # first upper left part clockwise
    return [(shift_x + 2, shift_y),
            (shift_x + 3, shift_y),
            (shift_x + 4, shift_y),
            (shift_x + 5, shift_y + 2),
            (shift_x + 5, shift_y + 3),
            (shift_x + 5, shift_y + 4),
            (shift_x + 4, shift_y + 5),
            (shift_x + 3, shift_y + 5),
            (shift_x + 2, shift_y + 5),
            (shift_x, shift_y + 4),
            (shift_x, shift_y + 3),
            (shift_x, shift_y + 2),
            # upper right part clockwise
            (shift_x + 8, shift_y),
            (shift_x + 9, shift_y),
            (shift_x + 10, shift_y),
            (shift_x + 12, shift_y + 2),
            (shift_x + 12, shift_y + 3),
            (shift_x + 12, shift_y + 4),
            (shift_x + 10, shift_y + 5),
            (shift_x + 9, shift_y + 5),
            (shift_x + 8, shift_y + 5),
            (shift_x + 7, shift_y + 4),
            (shift_x + 7, shift_y + 3),
            (shift_x + 7, shift_y + 2),
            # lower right clockwise
            (shift_x + 8, shift_y + 7),
            (shift_x + 9, shift_y + 7),
            (shift_x + 10, shift_y + 7),
            (shift_x + 12, shift_y + 8),
            (shift_x + 12, shift_y + 9),
            (shift_x + 12, shift_y + 10),
            (shift_x + 10, shift_y + 12),
            (shift_x + 9, shift_y + 12),
            (shift_x + 8, shift_y + 12),
            (shift_x + 7, shift_y + 10),
            (shift_x + 7, shift_y + 9),
            (shift_x + 7, shift_y + 8),
            # lower left clockwise
            (shift_x + 2, shift_y + 7),
            (shift_x + 3, shift_y + 7),
            (shift_x + 4, shift_y + 7),
            (shift_x + 5, shift_y + 8),
            (shift_x + 5, shift_y + 9),
            (shift_x + 5, shift_y + 10),
            (shift_x + 4, shift_y + 12),
            (shift_x + 3, shift_y + 12),
            (shift_x + 2, shift_y + 12),
            (shift_x, shift_y + 10),
            (shift_x, shift_y + 9),
            (shift_x, shift_y + 8)]