def draw_christmas_tree(height):
    for i in range(height):
        print(' ' * (height - i - 1) + '*' * (2 * i + 1))

draw_christmas_tree(5)

def draw_christmas_tree(height):
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

draw_christmas_tree(5)