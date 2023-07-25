def read_input(text_file) -> list[str]:
    with open(text_file, "r") as f:
        return f.readlines()

def create_path_list(path):
    path = path.strip().split(",")
    return path

def create_path_dict(path):
    path_dict = {}
    x = 0
    y = 0

    for item in path:
        direction = item[0]
        distance = int(item[1:])
        if direction == "D":
            for i in range(distance):
                y -= 1
                key = f"{x}, {y}"
                if key in path_dict.keys():
                    path_dict[key] = path_dict[key] + 1
                else:
                    path_dict[key] = 1
        if direction == "U":
            for i in range(distance):
                y += 1
                key = f"{x}, {y}"
                if key in path_dict.keys():
                    path_dict[key] = path_dict[key] + 1
                else:
                    path_dict[key] = 1
        if direction == "L":
            for i in range(distance):
                x -= 1
                key = f"{x}, {y}"
                if key in path_dict.keys():
                    path_dict[key] = path_dict[key] + 1
                else:
                    path_dict[key] = 1
        if direction == "R":
            for i in range(distance):
                x += 1
                key = f"{x}, {y}"
                if key in path_dict.keys():
                    path_dict[key] = path_dict[key] + 1
                else:
                    path_dict[key] = 1
        if direction == "D":
            for i in range(distance):
                y -= 1
                key = f"{x}, {y}"
                if key in path_dict.keys():
                    path_dict[key] = path_dict[key] + 1
                else:
                    path_dict[key] = 1
    crossovers = []
    for key, value in path_dict.items():
        if value > 1:
            crossovers.append(key)
    return crossovers


if __name__ == "__main__":
    input = read_input("day_3.txt")
    path_1 = create_path_list(input[0])
    path_2 = create_path_list(input[1])
    paths = path_1 + path_2
    crossovers = create_path_dict(paths)
    print(crossovers)
