s1 = "race a car"
s2 = s1[::-1]



def isPalindrome(s):
    s = ''.join(ch for ch in string_value1 if ch.isalnum())
    print(s)
    s1 = s[::-1]
    print(s == s1)


string_value1 = "A man, a plan, a canal: Panama".lower()
s = ''.join(ch for ch in string_value1 if ch.isalnum())
print(s)
s1 = s[::-1]
print(s == s1)
isPalindrome(string_value1)

string_value2 = "raceacar".lower()
s = ''.join(ch for ch in string_value2 if ch.isalnum())
print(s)
s1 = s[::-1]
print(s == s1)
isPalindrome(string_value2)

string_value3 = " ".lower()
s = ''.join(ch for ch in string_value3 if ch.isalnum())
print(s)
s1 = s[::-1]
print(s == s1)
isPalindrome(string_value3)

