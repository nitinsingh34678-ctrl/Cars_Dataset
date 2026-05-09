s = input("Enter a String :: ")

print("\n Choose operations:")
print('''1. Remove leading and wide spaces
2. Convert string to lower case
3. count letter "o" 
4. Replace "Python" to "Java" 
5. Find Length of the String
6. Check if String Contains Vowels''')

choice = int(input("Enter Your Choice (1-6) :: "))

match choice:
    case 1 :
        result = s.strip()
        print(f"After removing spaces :: {result} ")
    case 2 :
        result = s.lower()
        print(f"Lower String:: {result} ")
    case 3 :
        result = s.count("o")
        print(f"Number of letter \"o\" :: {result} ")
    case 4 :
        result = s.replace("python" , "java").capitalize()
        print(f"After Replacing :: {result} ")
    case 5 :
        result = len(s)
        print(f"Length of String :: {result} ")
    case 6 :
        result = "aeiouAEIOU"
        if any (ch in result for ch in s):
            print("String Contains Vowels")
        else:
            print("String Doesnot Contain Vowels")
    case _default:
        print("Invalid Choice")