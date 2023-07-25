def read_input(text_file) -> list[str]:
    with open(text_file, "r") as f:
        return f.readlines()
    

def create_expenses_list(expenses):
    expenses_list = []
    for line in expenses:
        num = line.strip()
        expenses_list.append(int(num))
        
    return expenses_list


def find_total_2020(expenses_list, total=2020):
    is_searching = True
    while is_searching:
        num = expenses_list.pop()
        to_find = total - num
        for i in range(len(expenses_list)):
            if expenses_list[i] == to_find:
                print(expenses_list[i])
                print(num)
                print(expenses_list[i] * num)
                return expenses_list[i] * num

    for i in range(1):
        num = expenses_list.pop()
        print(num)


def find_total_for_three(expenses_list):
    """Find three"""

    for i in range(len(expenses_list)):
        first_num = expenses_list[i]
        for j in range(len(expenses_list)):
            if expenses_list[j] != first_num:
                second_num = expenses_list[j]
                looking_for = 2020 - first_num - second_num
                for h in range(len(expenses_list)):
                    if expenses_list[h] != first_num and expenses_list[h] != second_num:
                        if expenses_list[h] == looking_for:
                            print(expenses_list[h])
                            print(first_num)
                            print(second_num)
                            return [first_num * second_num * expenses_list[h]]



if __name__ == "__main__":
    expenses = read_input("expenses.txt")
    expenses_list = create_expenses_list(expenses)
    #find_total_2020(expenses_list)
    print(find_total_for_three(expenses_list))

        
