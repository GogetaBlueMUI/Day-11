def convertion(str):
    try:
        str=int(str)
        print("Convertion: ", str)
    except:
        print("None.")
str=input("Enter a string: ")
convertion(str)
