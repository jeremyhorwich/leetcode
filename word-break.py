#Given a string and dictionary of strings,
#Check if the string can be made up of values
#from the dictionary

def wordBreak(s: str, wordDict: list[str]) -> bool:
        checked = set()
        def checkWordBreak(s, wordDict):
            if len(s) == 0:
                return True
            if s in checked:
                return False
            for i in range(0, len(s)):
                if s[0:i+1] in wordDict:
                    if checkWordBreak(s[(i+1):], wordDict):
                        return True
            checked.add(s)
            return False
        return checkWordBreak(s, wordDict)