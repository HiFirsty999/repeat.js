try:
    Text = input("Enter text: ")
    Repeat = int(input("Enter repeat count: "))
    NumberAsk = input("With number?: ")
    NumberAskLower = NumberAsk.lower()

    print("\n")

    def WithNumber(Text):
        for x in range(1, Repeat + 1):
            print(f"{x}. {Text}")
        
    def WithoutNumber(Text):
                for x in range(1, Repeat + 1):
                    print(f"{Text}")
                    
except ValueError:
    print("Number only!")

else:
    if NumberAskLower == "yes":
        WithNumber(Text)
    elif NumberAskLower == "no":
        WithoutNumber(Text)