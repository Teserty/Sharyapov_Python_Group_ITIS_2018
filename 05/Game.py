def mult(f, file, a):
    for line in f:
        file.write(line*a)
def sum(second, f, file):
    for i in f:
        file.write(i)
    for i in second:
        file.write(i)
if __name__=="__main__":
    a = int(input("Умножить = 1, Сложить = 2"))
    with open("file.txt", "r") as f, open("MultedFile.txt", "w") as file:
        if a == 1:
            a = int(input("На сколько умножить?"))
            mult(f, file, a)
        else:
            with open("secondFile", "r") as second:
                sum(second, f, file)