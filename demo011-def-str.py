def print_string(str, no_of_time):
    for i in range(1, no_of_time+1):
        print(str)


print_string("Welcome to Python",10)

print("=====")

def print_string(str="Hello World", no_of_time=5):
    for i in range(1, no_of_time+1):
        print(str)

print_string()

print("=====")

def print_multiplication_table(table, no_of_time):
    for i in range(1,no_of_time+1):
        print(f"{table} * {i} = {table*i}")

print_multiplication_table(3,5)

print("=====")

def print_table(table, start, end):
    for i in range(start, end+1):
        print(f"{table} * {i} = {table*i}")

print_table(2, 3, 10)