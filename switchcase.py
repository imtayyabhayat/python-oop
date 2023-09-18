# Calculate the average of the comma seperated input numbers
def average(numbers):
    integer_list = [int(value.strip()) for value in numbers.split(",")]
    sum = 0
    for i in integer_list:
        sum += i
    return sum / len(integer_list) 

# Calculate the percentage
def percentage(total, result):
    return round((result / total)*100, 2)

# Calculate the value of the percentage
def valuecalc(percent, total):
    return round((percent / 100) * total, 2)

# Print the table of the selected value
def tableoutput(table):
    if(table <= 10):
        result = (f"Table of {table}\n")
        for i in range(1,11):    
            result += (f"{table} * {i} = {table * i}\n")
            7
        return result
    else:
        return "Table out of range"

while True:
    # Try/Catch block
    try:
        listoptions = int(input('''1: Table Print
2: Average Print
3: Percentage Print
4: Percentage Value Calc
99: Error Log
0: Exit
Response: '''))
        # if statement
        if(listoptions == 0):
            break
        else:
            # Switch Case to show the required function
            match listoptions:
                case 1:
                    table = int(input("Enter a number: "))
                    print(tableoutput(table))
                case 2:
                    ave = input("Enter comma seperated numbers: ")
                    print(average(ave))
                case 3:
                    total = int(input("Enter total: "))
                    result = int(input("Enter result: "))
                    print(percentage(total, result))
                case 4:
                    percentage = int(input("Enter percentage: "))
                    total = int(input("Enter total: "))
                    print(valuecalc(percentage, total))
                case 99:
                    # Read a file
                    with open("error.txt", "r") as f:
                        error = f.read()
                        print(error)
                case _:
                    print("Invalid input")
    except Exception as e:
        # Wite a file
        with open("error.txt", "a") as f:
            f.write(f"{e}\n")
        print("Error occurred, see log file for details")
        # Break the while loop
        break