def palindrome (s, left, right):
    if len(s)%2 == 0  and left+1 == right:
        return True

    if len(s)%2 != 0 and left+2 == right:
        return True

    if s[left] == s[right] and palindrome(s, left+1, right-1 ):
        return True
    else:
        return False

s = "salsa".lower()
# s = input().lower()
s = "".join(s.split())

result = palindrome(s, 0, len(s)-1)
print(result)
