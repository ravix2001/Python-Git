# Take input from the user for the array
input_str = input("Enter elements of the array separated by space: ")
try:
    # Convert the input string into a list of integers
    array = [int(x) for x in input_str.split()]
    
    # Sort the array
    sorted_array = sorted(array)
    
    # Display the sorted array
    print("Sorted array:", sorted_array)

except ValueError:
    print("Please enter valid integers separated by space.")
