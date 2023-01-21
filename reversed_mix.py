message = "this is a test message for educational purposes"

reversd = message[::-2]
second = message[-2::-2]
print(reversd)
print(second)

l = len(reversd) + len(second)

reciphered = []
k = 1
j = 1
for i in range(1, l):
    if i % 2 == 1:
        reciphered.append(reversd[-k])
        k += 1
    else:
        reciphered.append(second[-j])
        j += 1

for letter in reciphered:
    print(letter, end="")
