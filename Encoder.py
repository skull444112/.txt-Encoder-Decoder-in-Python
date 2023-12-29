import random,string

chars = string.ascii_letters + string.digits + string.punctuation + " "
chars = list(chars)
key = chars.copy()

random.shuffle(key)
main = zip(chars, key)
main = list(main)

def fileconf():
    path = input("Enter the path of the file: ")
    path += "\\"
    fileName = input("Enter the file Name: ")
    with open(path + fileName, 'r') as file:
        letter = file.read()
        print(f"File content:\n{letter}\n==========")
        return letter,path

def encode():
    print("===== Encoding! =====")
    letter,path = fileconf()
    for i in letter:
        for j in main:
            if i == j[0]:
                letter = letter.replace(j[0],j[1])

    fileName = "Encoded.txt"
    with open(path + fileName, 'w+') as file:
        file.write(letter)
    print(f"Encoded: \n{letter}\n==========\nFile saved at {path+fileName}")
    input("Press enter to continue..")


def decode():
    print("===== Decoding! =====")
    letter, path = fileconf()
    for i in letter:
        for j in main:
            if i==j[1]:
                letter = letter.replace(j[1],j[0])

    fileName = "Decoded.txt"
    with open(path + fileName, 'w+') as file:
        file.write(letter)
    print(f"Decoded: \n{letter}\n==========\nFile saved at {path + fileName}")
    input("Press enter to continue..")


running = True

while running:
    options = int(input("Choose an option: \n1-Encode\n2-Decode\n3-Exit\n++>"))

    match options:
        case 1:
            encode()
        case 2:
            decode()
        case 3:
            running = False