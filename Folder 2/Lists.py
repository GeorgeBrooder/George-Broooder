# names = ["Jenny", "Alexus"]

# print(names[0] + " " + names[1])
# # #0, 1, 2, 3, 4 ...

# # names_and_heights = [["Jenny", 67], ["Alexus", 70]]
# # print(names_and_heights[0][1])
# # print(names_and_heights[0][0] + " is " + str(names_and_heights[0][1])+ " inches tall")

# # names = ["Jenny", "Alexus", "Same"] #zip() does not include items from longer list is list lengths are not the same
# # heights = [67, 70]

# # names_and_heights = list(zip(names, heights))
# # # names_and_heights == [("jenny", 67), ("alexus", 70)]

# # #tuples: (x, y) and cannot be changed
# # # list: [x, y]

# # print(list(names_and_heights))

# # print(names_and_heights[0][0])

# names = ["Jenny", "Alexus"]
# print("Before adding \"Sam\": " + str(names))
# names.append("Sam")
# print("After adding \"Sam\": " + str(names))

# # names.insert(0, "alex")

# #range(x)
# #start: 0
# #stop: x-1
# #step: 1
# new_range = list(range(10))
# print(new_range)

# #range(x, y, z)
# #start: x
# #stop: y-1
# #step: z

# even_range = list(range(0, 21, 2))
# print(even_range)

# #range(x, y)
# #start: x
# #stop: y-1
# #step: 1

# zero_to_five = list(range(0, 6))
# print(zero_to_five)

names_and_heights = [["jenny", 67], ["alexus", 70]]

for student in names_and_heights:
    for attribute in student:
        if type(attribute) is string:
            print("name: " + attribute)
        else:
            print("height: "+ str(attribute))