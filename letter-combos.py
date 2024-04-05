#Given a phone number, return all possible letter
#combinations it could represent

def letter_combinations(digits: str) -> list[str]:
    letters_by_number = {
                   2: "abc", 3: "def",
        4: "ghi",  5: "jkl", 6: "mno",
        7: "pqrs", 8: "tuv", 9: "wxyz"
    }

    combinations = [""]
    for digit in digits:
        if digit == "1":
            continue
        new_combinations = list()
        for combination in combinations:
            for letter in letters_by_number[int(digit)]:
                new_combinations.append(combination + letter)
        combinations = new_combinations
        
    return combinations

if __name__ == "__main__":
    print(letter_combinations("23"))
    print(letter_combinations(""))
    print(letter_combinations("2"))
    print(letter_combinations("1234"))