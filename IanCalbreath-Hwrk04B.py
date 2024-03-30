# Ian Calbreath's Sales Bar Chart Program
print("Ian Calbreath's Sales Bar Chart Program")

# Mac Littlefield's class

# User inputs sales numbers for each store

Sales1 = int(input("Enter today's sales for store 1: "))
Sales2 = int(input("Enter today's sales for store 2: "))
Sales3 = int(input("Enter today's sales for store 3: "))
Sales4 = int(input("Enter today's sales for store 4: "))
Sales5 = int(input("Enter today's sales for store 5: "))

# Divide sales numbers by 100 and convert to integer to get number of asterisks

NumAst1 = int(Sales1 / 100)
NumAst2 = int(Sales2 / 100)
NumAst3 = int(Sales3 / 100)
NumAst4 = int(Sales4 / 100)
NumAst5 = int(Sales5 / 100)


# Printing bar chart for each store using range
print('')
print('SALES BAR CHART')
print('')

print("Store 1: ", end='')
for col in range(NumAst1):
    print('*', end='')
print('')

print("Store 2: ", end='' )
for col in range(NumAst2):
    print('*', end='')
print('')

print("Store 3: ", end='' )
for col in range(NumAst3):
    print('*', end='')
print('')

print("Store 4: ", end='')
for col in range(NumAst4):
    print('*', end='')
print('')

print("Store 5: ", end='')
for col in range(NumAst5):
    print('*', end='')
print('')
