def generate_doughnut(size):
    doughnut = [[' ' for _ in range(size * 2 + 1)] for _ in range(size * 2 + 1)]

    for y in range(size * 2 + 1):
        for x in range(size * 2 + 1):
            distance_to_center = ((size - y) ** 2 + (size - x) ** 2) ** 0.5
            if size - 3 <= distance_to_center <= size + 3:
                doughnut[y][x] = '*'
            elif size - 5 <= distance_to_center <= size + 5:
                doughnut[y][x] = '%'
            elif size - 7 <= distance_to_center <= size + 7:
                doughnut[y][x] = '^'
            elif size - 9 <= distance_to_center <= size + 9:
                doughnut[y][x] = '~'
            elif size - 11 <= distance_to_center <= size + 11:
                doughnut[y][x] = '!'
            elif size - 13 <= distance_to_center <= size + 13:
                doughnut[y][x] = '/'

    return '\n'.join(''.join(row) for row in doughnut)


size = 10
print(generate_doughnut(size))
