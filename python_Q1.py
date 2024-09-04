def create_tree(leaf_char, middle_char, height):
    for i in range(height):
        leaves = (leaf_char + middle_char) * i + leaf_char
        spaces = ' ' * (height - i - 1)
        print(spaces + leaves + spaces)

leaf_char = '*'
middle_char = '0'
height = 5

create_tree(leaf_char, middle_char, height)