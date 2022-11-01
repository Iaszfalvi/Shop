# Write a program to output the “times table” for the number 12. The output should be 10 rows:

#     1 x 12 is 12
#     2 x 12 is 24
#     (3-9 x 12)
#     10 x 12 is 120

mylist = [1, 2, 3,4,5,6,7,8,9,10,11,12]

for n1 in mylist:
    for n2 in mylist:
        print(f"{n1} x {n2} is {n1 * n2}")

for num_one in range(1,13):
    for num_two in range(1,13):
        print(f"{num_one} x {num_two} is {num_one * num_two}")