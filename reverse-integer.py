#Given a signed 32-bit integer, return it with digits reversed

def reverse(num: int) -> int:
    negative = False
    if num < 0:
        negative = True
        num = abs(num)        
    num_as_string = str(num)
    num_as_string = num_as_string[::-1]
    reversed = int(num_as_string)
    if negative:
        reversed *= -1
    return reversed if reversed.bit_length() < 32 else 0

if __name__ == "__main__":
    print(reverse(123))
    print(reverse(-123))
    print(reverse(120))
    print(reverse(2147483647))