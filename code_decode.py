while True:
    coding = input("press 1 to code & 0 to decode\n")

    str = input("Enter a message\n")

    r1 = "kfjsd"
    r2 = "seofe"

    if(coding == "1"):
        coding = True
    else:
        coding = False
    if(coding):
        if(len(str)>=3):
            str = r1+str[1:]+str[0]+r2          #str = r1+str[1:len(str)]+str[0]+r2
        else:
            str = r1+str[1]+str[0]+r2
        
        print("\nCoded data:\n",str)
    else:
        if(len(str)>=13):
            str = str[-6]+str[5:-6]
        else:
            str = str[6]+str[5]
        
        print("\nDecoded data:\n",str)
    play_again = input("\nWant to do again? (Y/N): ").lower()
    
    if play_again !="y":
        break