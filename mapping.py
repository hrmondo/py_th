
# The instructions say that when "the item is a double pipe (||) ...
# instead of printing the item, print a new line (\n)." So the double pipe symbols should not appear in the output.

# That print statement that had no contents but set "end" to an empty string became a no-op (a "do nothing").
# But the print statement with no contents at all still puts out a blank line.

TILES = ('-', ' ', '-', ' ', '-', '||',
         '_', '|', '_', '|', '_', '|', '||',
         '&', ' ', '_', ' ', '||',
         ' ', ' ', ' ', '^', ' ', '||'
)

for tile in TILES:
    if tile == '||':
        print()
    else:
        print(tile, end="")


