        
prompt = input("What is the average growth of the drive?: ")
calculate_6mo = float(prompt) * 26 #26 is half of the year which is 52 weeks in a year
round_6mo = round(calculate_6mo /10) * 10
print(f"we can estimate that the new drive will require {round_6mo}GB of storage")
prompt_free = input("What is the current free space?:" )
free = float(prompt_free)
calculate_remain = round_6mo - free
print(f"adding to the current space remaining will give us {calculate_remain}GB")
      

if calculate_remain <= 50:
    prompt = input("Do you want to round this to 50? \n(use y or n): ")
    if prompt.lower() == 'y':
        calculate_remain = 50
        print(f"You should add {calculate_remain}GB to the drive")
    else:
        print(calculate_remain)
elif 50 < calculate_remain <= 100:
    prompt = input("Do you want to round this to 100? \n(use y or n): ")
    if prompt.lower() == 'y':
        calculate_remain = 100
        print(f"You should add {calculate_remain}GB to the drive")
    else:
        print(calculate_remain)
elif 100 < calculate_remain < 150:
    prompt = input("Do you want to round this to 150? \n(use y or n): ")
    if prompt.lower() == 'y':
        calculate_remain = 150
        print(f"You should add {calculate_remain}GB to the drive")
    else:
        print(calculate_remain)
elif 150 < calculate_remain < 200:
    prompt = input("Do you want to round this to 200? \n(use y or n): ")
    if prompt.lower() == 'y':
        calculate_remain = 200
        print(f"You should add {calculate_remain}GB to the drive")
    else:
        print(calculate_remain)
else:
    print(f"You should add {calculate_remain}GB to the drive")

      
prompt = input("\nWhich letter drive are you adding size to?: ").upper()
print(f"The drive letter {prompt} will now be added to the drive")
letter_drive = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5
                , 'F':6, 'G':7, 'H':8, 'I':9, 'J':10
                , 'K':11, 'L':12, 'M':13, 'N':14, 'O':15
                , 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20
                , 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
def driver_function():
    if prompt in letter_drive: # uses the prompt as a key and returns the value of letter drive which is an interger and adds it to the rounded 6 months
        return letter_drive[prompt] + calculate_remain
print(f"the size we are adding is now {driver_function()}")


ask = input("\nWhat is the current size of the drive?: ")
make_it_a_float = float(ask)
add_drive = make_it_a_float + driver_function()  #calculates the size of the drive after adding the new amount of GB
print(f"the total drive size will be {add_drive}GB now")
        
exit()
