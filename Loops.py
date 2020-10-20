rng = list(range(6))
print(rng)

lst = [1, 2, 3, 4, 5, 6, 7, 8]
for num in lst:
    print(num*2)
print(lst)

# range(6) -> [0, 1, 2, 3, 4, 5]
# range(8) -> [0, 1, 2, 3, 4, 5, 6, 7]
#

list_length = len(lst)
for index in range(len(lst)):
    lst[index] = 2 * lst[index]
    print(lst[index])