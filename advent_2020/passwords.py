def read_input(text_file) -> list[str]:
    with open(text_file, "r") as f:
        return f.readlines()


def find_valid_passwords(passwords):
    count = 0
    for password in passwords:
        password = password.split(" ")
        pass_nums = password[0].split("-")
        letter = password[1][0]
        num_of_letters = password[2].count(letter)
        if int(pass_nums[0]) <= num_of_letters <= int(pass_nums[1]):
            count += 1
    print(count)
    return count

def find_actual_valid_passwords(passwords):
    count = 0
    for password in passwords:
        password = password.split(" ")
        pass_nums = password[0].split("-")
        letter = password[1][0]
        if password[2][int(pass_nums[0]) - 1] == letter and password[2][int(pass_nums[1]) - 1] != letter:
            count += 1
        elif password[2][int(pass_nums[0]) - 1] != letter and password[2][int(pass_nums[1]) - 1] == letter:
            count += 1
    print(count)
    return count



if __name__ == "__main__":
    passwords = read_input("passwords.txt")
    #find_valid_passwords(passwords)
    find_actual_valid_passwords(passwords)