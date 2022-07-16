"""
See _10.py
Problem :
? = matches any single char
* = matches any sequence of chars (chars can be different or
    empty sequence). "*" matches anything.

Text and pattern must match exactly.
"""

def isMatch(t: str, p: str) -> bool:
    
    sizeT, sizeP = (len(t), len(p))
    
    arr = [[False for i in range(sizeT + 1)] for j in range(sizeP + 1)]
    arr[0][0] = True

    # Necessary in case of "" (empty) text. * can match with no char, so
    # if preceding result is True, result with * will also be True
    for j in range(1, sizeP + 1):
        if (p[j - 1] == '*'):
            arr[j][0] = arr[j - 1][0]

    repeatedChar = None
    for j in range(1, sizeP + 1):
        for i in range(1, sizeT + 1):

            # * can match with char equaling previous repeatedChar (copy)
            # and if such, no need to increment edge in pattern ([j] -> [j])
            if p[j - 1] == '*':
                if t[i-1] == repeatedChar:
                    arr[j][i] = arr[j][i - 1]
                    
                # Cases:
                # if t[i-1] == repeatedChar: * matches repeatedChar (copy)
                # arr[j - 1][i]: * matches zero char (so borrow prev result)
                # arr[j - 1][i - 1]: * matches with lone char (not repeated)
                arr[j][i] = arr[j][i] or arr[j - 1][i] or arr[j - 1][i - 1]
                
                # Prepare for next char in t with same edge in pattern
                if (arr[j][i]):
                    repeatedChar = t[i - 1]
                    
            elif p[j - 1] == '?' or p[j - 1] == t[i - 1]:
                arr[j][i] = arr[j - 1][i - 1]

    return arr[sizeP][sizeT]

if __name__ == "__main__":
    print("bc", " ?*?", "Correct" if isMatch("bc", "?*?") == True else "Incorrect")