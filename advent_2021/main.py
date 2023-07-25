def read_input(text_file) -> list[str]:
    with open(text_file, "r") as f:
        return f.readlines()


def count_bigger_numbers(input_list: list) -> int:
    count = 0

    for num in input_list:
        num = num.replace("\n", "")

    for i in range(1, len(input_list)):
        if int(input_list[i]) > int(input_list[i - 1]):
            count += 1
    print(count)
    return count


def count_bigger_numbers_in_threes(input_list: list) -> int:
    count = 0
    three_nums = int(input_list[0]) + int(input_list[1]) + int(input_list[2])
    for num in input_list:
        num = num.replace("\n", "")

    for i in range(2, len(input_list) - 2):
        current_three_nums = int(input_list[i]) + int(input_list[i + 1]) + int(input_list[i + 2])
        if current_three_nums > three_nums:
            count += 1
        three_nums = current_three_nums
    print(count)
    return count


def calculate_direction(directions):
    
    horizontal_position = 0
    depth = 0
    aim = 0
    for item in directions:
        item = item.replace("\n", "")
        if item.rfind("forward") >= 0:
            move = int(item[8:])
            horizontal_position += move
            depth_change = move * aim
            depth += depth_change
        elif item.rfind("down") >= 0:
            move = int(item[5:])
            aim += move
        elif item.rfind("up") >=0:
            move = int(item[3:])
            aim -= move
    print(horizontal_position * depth)
    return horizontal_position * depth


def calculate_binary_rates(input: list) -> int:
    most_common = []
    least_common = []
    for i in range(12):
        one_count = 0
        zero_count = 0
        for item in input:
            if item[i] == "1":
                one_count += 1
            else:
                zero_count += 1
        if one_count > zero_count:
            most_common.append("1")
            least_common.append("0")
        else:
            most_common.append("0")
            least_common.append("1")
    gamma_rate = "".join(most_common)
    epsilon_rate = "".join(least_common)
    print(gamma_rate)
    print(epsilon_rate)
    gamma = int(gamma_rate, 2)
    epsilon = int(epsilon_rate, 2)
    print(gamma * epsilon)
    return gamma * epsilon


def get_most_common_number(input: str, index: int) -> int:

    one_count = 0
    zero_count = 0
    for item in input:
        if item[index] == "1":
            one_count += 1
        else:
            zero_count += 1
    if zero_count > one_count:
        return "0"
    else:
        return "1"


def get_least_common_number(input: str, index: int) -> int:

    one_count = 0
    zero_count = 0
    for item in input:
        if item[index] == "1":
            one_count += 1
        else:
            zero_count += 1
    if zero_count <= one_count:
        print(0)
        return "0"
    else:
        print(1)
        return "1"


def get_oxygen_generator_rating(input: list):
    item_list = []
    for item in input:
        item_list.append(item)
    
    for i in range(len(item_list[0])):
        if len(item_list) == 1:
            return item_list[0]
        most_common = get_most_common_number(item_list, i)
        new_list = []
        for item in item_list:
            if item[i] == most_common:
                new_list.append(item)
        item_list = new_list
        print(item_list)
    return item_list[0]


def get_scrubber_rating(input: list):
    item_list = []
    for item in input:
        item_list.append(item)

    for i in range(len(item_list[0])):
        if len(item_list) == 1:
            return item_list[0]
        most_common = get_least_common_number(item_list, i)
        new_list = []
        for item in item_list:
            if item[i] == most_common:
                new_list.append(item)
        item_list = new_list
        print(item_list)
    return item_list[0]



def get_life_support_rating(oxygen, scrubber):
    oxygen_rate = int(oxygen, 2)
    scrubber_rate = int(scrubber, 2)
    print(oxygen_rate * scrubber_rate)
    return oxygen_rate * scrubber_rate


test_list = ["001111011011", "000110001010", "011010111111"]
new_list = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

if __name__ == "__main__":
    my_list = read_input("input.txt")
    binary_input = read_input("binary.txt")
    oxygen = get_oxygen_generator_rating(binary_input)
    scrubber = get_scrubber_rating(binary_input)
    get_life_support_rating(oxygen, scrubber)
