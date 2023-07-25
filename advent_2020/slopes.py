def read_input(text_file) -> list[str]:
    with open(text_file, "r") as f:
        return f.readlines()


def count_trees_hit(layout):
    layout_list = []
    for line in layout:
        line = line.strip()
        layout_list.append(line)
    across = 0
    down = 0
    trees_hit = 0
    while across < len(layout_list):
        across += 3
        down += 1
        print("line length: " + str(len(layout_list[down])))
        right_index = across % len(layout_list[down]) + 1
        if right_index == 31:
            right_index = 0
        print("right index: " + str(right_index))
        if layout_list[down][right_index] == "#":
            trees_hit += 1
    print(trees_hit)
    return trees_hit



if __name__ == "__main__":
    layout = read_input("slopes.txt")
    count_trees_hit(layout)