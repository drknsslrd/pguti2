# lab 1

set1 = {1,2,3,4}
set2 = {3,4,5,6}

print(set1.intersection(set2))

# lab 2

phone_book = {"VladiSlave" : {"phone" : "8 927 1488", "address" : "Home"},
              "YaroSlave" : {"phone" : "8 927 322 67 52", "address" : "not home"}}

name = str(input("Enter name:"))

if name in phone_book:
    print("phone:", phone_book[name]["phone"])
    print("address:", phone_book[name]["address"])
else:
    print("men no in DB")

# lab 3

tuple1 = ("ky", "322")
print(" ".join(tuple1))

# lab 4
def log(operation):
    with open("log.txt", "a") as file:
        file.write(operation + "\n")

log("Запуск программы")
log("Выполнена операция сложения")
log("Программа завершена")
