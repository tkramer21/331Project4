list1 = []

first = 'D'
middle = 'A'
last = 'C'

print("Original list", list1)
print("Original Size: ", len(list1))

ptr = -1
i = 0

while i <= len(list1) - 1:
    if list1[i] == first:
        list1[ptr + 1], list1[i] = list1[i], list1[ptr + 1]  # swap first el after last swap and current el
        ptr += 1
    i += 1

print("List after First", list1)
print("New Size: ", len(list1))

i = 0
while i <= len(list1) - 1:
    if list1[i] == middle:
        list1[ptr + 1], list1[i] = list1[i], list1[ptr + 1]
        ptr += 1
    i += 1

print("List after Middle", list1)
print("New Size: ", len(list1))
