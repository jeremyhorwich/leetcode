#Given a string, return the longest palindromic substring

def longest_palindromic_substring(s: str) -> str:
    j = len(s)
    while (j > 0):
        i = 0
        k = j
        while k <= len(s):
            if is_palindrome(s[i:k]):
                return s[i:k]
            i += 1
            k += 1
        j -= 1
    return s[0]


def is_palindrome(s: str) -> bool:
    i = 0
    while i < (len(s) - i  - 1):
        if s[i] != s[len(s) - i - 1]:
            return False
        i += 1
    return True

if __name__ == "__main__":
    print(longest_palindromic_substring("babad"))
    print(longest_palindromic_substring("cbbd"))
    print(longest_palindromic_substring("asjfhlaskjhhjks"))

#This solution works but it's inefficient. I was stumped and had to
#look up Manacher's algorithm