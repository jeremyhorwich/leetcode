#Given a list of strings, find the longest common prefix among them

def longest_common_prefix(strings: list[str]) -> str:
    prefix = ""
    for i, char in enumerate(strings[0]):
        for j in range(1,len(strings)):
            if i >= len(strings[j]):
                return prefix
            if char != strings[j][i]:
                return prefix
        prefix += char
    return prefix


if __name__ == "__main__":
    print(longest_common_prefix(["flower","flow","flight"]))
    print(longest_common_prefix(["dog","racecar","car"]))
    print(longest_common_prefix(["cowpoke","cowpoke","cowpoke"]))
    print(longest_common_prefix(["re","rebar","rebars"]))

