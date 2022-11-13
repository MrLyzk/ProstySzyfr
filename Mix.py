lines = []


# funkcja zwracająca zdanie w odwrotnej kolejności
def rev(sentence):
    return sentence[::-1]


# otwarcie pliku za pomocą with automatycznie go zamyka
with open("tekstowy") as f:
    i = 0
    for line in f:
        lines.append(rev(line))
        i = i + 1

# odwrócenie kolejności całych linii
lines.reverse()


# wyświetlenie końcowego efektu
for line in lines:
    print(line)


with open("tekstowy_zaszyfrowany.txt", mode='w') as file:
    file.writelines(lines)
