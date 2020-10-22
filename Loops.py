# rng = list(range(6))
# print(rng)

# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# for num in lst:
#     print(num*2)
# print(lst)

# # range(6) -> [0, 1, 2, 3, 4, 5]
# # range(8) -> [0, 1, 2, 3, 4, 5, 6, 7]
# #

# list_length = len(lst)
# for index in range(len(lst)):
#     lst[index] = 2 * lst[index]
#     print(lst[index])

# items_on_sale = ["Blue Shirt", "Striped Socks", "Knit Dress", "Red Headband"]

# for items in items_on_sale:
#     if items == "Knit Dress":
#         print("Knit Dress is on sale!")
#         break

# print("End of search!")

nums = [1, 2, 3, 4, 5, 6, 7]

for num in nums:
    if num%2 == 0:
        continue
print(num)