#Given a string, determine the length of the longest substring
#which contains only unique characters

def length_of_longest_substring(s: str) -> int:
    substring_left = 0
    seen = {s[0] : 0}
    longest = 1
    for index in range(1,len(s)): #Slicing list[1:] for enum is O(n)
        char = s[index]
        if char not in seen:
            seen[char] = index
            continue
        longest = max(longest, index - substring_left)
        new_substring_left = seen[char] + 1
        for no_longer_seen in range(substring_left,new_substring_left):
            seen.pop(s[no_longer_seen])
        substring_left = new_substring_left
        seen[char] = index
    longest = max(longest, len(s) - substring_left)
    return longest


if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))
    print(length_of_longest_substring("bbbbb"))
    print(length_of_longest_substring("pwwkew"))
    print(length_of_longest_substring("dzdw"))