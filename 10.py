def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
s = input("Enter a string: ")
result = reverse_string(s)
print("The reversed string is:", result)
