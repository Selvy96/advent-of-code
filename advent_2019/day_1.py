import math

def read_input(text_file) -> list[str]:
    with open(text_file, "r") as f:
        return f.readlines()


def find_fuel_requirement(input):
    total = 0
    for line in input:
        line = int(line.strip())
        num = line
        subtotal = 0
        while num >= 9:
            divided = num / 3
            floor = math.floor(divided)
            num = floor - 2
            subtotal += num
        total += subtotal

    return total
        

if __name__ == "__main__":
    input = read_input("day_1.txt")
    total = find_fuel_requirement(input)
    print(total)
