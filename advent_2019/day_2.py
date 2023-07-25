def read_input(text_file) -> list[str]:
    with open(text_file, "r") as f:
        return f.read()


def get_input_list(text_file):
    input = read_input("day_2.txt")
    output = input.split(",")
    return output


def run_program(output):
    is_running = True
    index = 0
    my_list = output
    while is_running:
        opcode = int(my_list[index])
        if opcode == 99:
            is_running = False
        else:
            num1_index = int(my_list[index + 1])
            num2_index = int(my_list[index + 2])
            total_index = int(my_list[index + 3])
            if opcode == 1:
                total = int(my_list[num1_index]) + int(my_list[num2_index])
            elif opcode == 2:
                total = int(my_list[num1_index]) * int(my_list[num2_index])
            else:
                total = 0
            if total_index < len(my_list):
                my_list[total_index] = total
            index += 4
    return my_list


def find_noun_and_verb():
    for i in range(100):
        noun = i
        for j in range(100):
            verb = j
            output = get_input_list("day_2.txt")
            output[1] = noun
            output[2] = verb
            program_output = run_program(output)
            if program_output[0] == 19690720:
                print("Noun: ")
                print(noun)
                print("Verb: ")
                print(verb)
                return 100 * noun + verb
    print("Fail")
    return None




if __name__ == "__main__":
    output = get_input_list("day_2.txt")
    # output[1] = 12
    # output[2] = 2
    # final_list = run_program(output)
    # print(final_list)
    answer = find_noun_and_verb()
    print(answer)

