# EXAMPLES:
# move((1, 1, 10), (-1, 0)) => (0, 1, 10)
# move((0, 1, 10), (-1, 0)) => (0, 1, 5)
# move((0, 9, 5), (0, 1)) => (0, 9, 0)

# "Don't let them go over the wall"

def move(player, direction):
    # The current position (x, y) and points (hp)
    x, y, hp = player

    # movements to x and y directions
    xm, ym = direction
    if x+xm < 0 or x+xm > 9:
        hp -= 5

    else:
        x += xm
    if y+ym < 0 or y+ym > 9:
        hp -= 5

    else:
        y += ym
    return x, y, hp