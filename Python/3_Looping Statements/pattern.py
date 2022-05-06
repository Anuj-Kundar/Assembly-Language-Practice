# Write a program to construct the rigth andle trianle pattern, using a nested loop number(two levels of loop statements)
for i in range(1,6):
    for j in range(1,6):
        if i>=j:
            print('0', end = ' ' )
    print('\n')
