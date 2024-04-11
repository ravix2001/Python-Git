#Exception Handling

try:
    num = int(input("Enter the numerator : "))
    den = int(input("Enter the denominator : "))
    result = num/den

#except Exception:
    #print("Something went wrong.")

except ZeroDivisionError as e:
    print(e)
    print("A number cannot be divided by 0.")

except ValueError as e:
    print(e)
    print("Please enter numbers only.")

else:
    print(result)