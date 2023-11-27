#Write a Python function that checks whether a passed string is palindrome or not 

def isPalindrome(a):
    return a==a[::-1]

a="janvi"
ans=a[::-1]
print(ans)

if ans==a:
    print("yes")
else:
    print("no")