# ********************************** Fraud Multiplication Table *************************************

# Importing Library
import random

# Findind the table of perticular number
def table(num):
    for i in range(1, 11):
        table_1.append(num*i)

# we have to make the fraud / wrong table
def defect_table(num):
    choice = random.randint(1, 11)
    for i in range(1, 11):
        if i == choice:
            table_2.append((num*i) + choice)
        else:
            table_2.append(num*i)
    print(table_2)

# This function will find that what is the fraud and the occurance or argfraud number in table
def defect_found():
    for i in range(0, 10):
        if table_1[i] != table_2[i]:
            print(f"Defect is found in step {i + 1} : {table_2[i]} has to {table_1[i]} in list...!")
            print("Rohan Das is a fraud and he cheated with the class guys..!")
            
if __name__ == '__main__':
    while True:
        a = table_1 = []
        b = table_2 = []
        try:
            num = int(input("\nEnter the number:"))
        except Exception as e:
            print("Invalid input..!")
            continue
        table(num)
        defect_table(num)
        defect_found()
        continue
