#Given an integer (0 < x < 3999), convert it to Roman numerals

def integer_to_roman(num: int) -> str:
    roman = ""

    thousands = num // 1000
    roman += "M"*thousands
    num -= thousands*1000

    hundreds = num // 100
    roman += digit_to_roman(hundreds,"M","D","C")
    num -= hundreds*100

    tens = num // 10
    roman += digit_to_roman(tens,"C","L","X")
    num -= tens*10

    roman += digit_to_roman(num,"X","V","I")

    return roman

def digit_to_roman(digit: int, t_mark: str, f_mark: str, o_mark: str) -> str:
    roman = ""
    if digit > 5:
        if digit == 9:
            return o_mark + t_mark
        else:
            return f_mark + (digit-5)*o_mark
    elif digit == 5:
        return f_mark
    else:
        if digit == 4:
            return o_mark + f_mark
        else:
            return digit*o_mark 

if __name__ == "__main__":
    print(integer_to_roman(3))
    print(integer_to_roman(58))
    print(integer_to_roman(1994))
    print(integer_to_roman(3849))