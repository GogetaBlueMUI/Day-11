def converstion(num):
    try:
        num=str(num)
        print("Converted: ", num)
    except:
        print("None.")
num=int(input("Enter number: "))
converstion(num)