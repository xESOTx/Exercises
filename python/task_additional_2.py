level=int(input("Podaj poziom choinki do wygenerowania: "))
height=3
for i in range(0, level):
    for x in range(1, height):
        print(x * "#")
    height+=1
