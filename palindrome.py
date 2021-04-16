

ch = str(input("Enter a String = "))
ch = ch.casefold()
rev_str = reversed(ch)

if list(ch) == list(rev_str):
    print(ch,"is palindrome")
else:print(ch,"is not palindrome")


