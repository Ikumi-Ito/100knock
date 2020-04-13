#10
with open("hightemp.txt", "r") as file:
    text_10 = file.readlines()
    print(len(text_10))

#11
with open("hightemp.txt", "r") as file:
    for i in file:
        print(i.replace("\t", " "), end="")

#12
with open("hightemp.txt", "r") as file, open("col1.txt", "w") as col1, open("col2.txt", "w") as col2:
    for i in file:
        i = i.split("\t")
        col1.write(i[0] + "\n")
        col2.write(i[1] + "\n")

#13
with open("col1.txt","r") as col1, open("col2.txt", "r") as col2, open("marge.txt", "w") as mar:
    for x, y in zip (col1, col2):
        x = x.replace("\n", "")
        y = y.replace("\n", "")
        mar.write(x + "\t" + y + "\n")

#14
n = input("数字を入力14 :")

with open("hightemp.txt", "r") as file:
    file = file.readlines()
    print("".join(file[:int(n)]))

#15
n = input("数字を入力15 :")

with open("hightemp.txt", "r") as file:
    file = file.readlines()
    print("".join(file[len(file)-int(n):]))

#16
n = input("数字を入力16 :")

with open("hightemp.txt", "r") as file:
    file = file.readlines()
    start = 0
    a = int(len(file)/int(n))
    for i in range(int(n)):
        print("".join(file[start:start+a]))
        start += a

#17
with open("hightemp.txt", "r") as file:
    out = set()
    for i in file:
        i = i.split("\t")
        out.add(i[0])
    print(out)

#18
with open("hightemp.txt", "r") as file:
    out = []
    for i in file:
        k = i.split("\t")
        out.append([k[2], "".join(i)])
    out.sort()  #二次元配列の場合は、それぞれのリストの最初の要素を比較してソートする
    for x, y in out:
        print("".join(y), end="")

#19
with open("hightemp.txt", "r") as file:
    a = []
    ziku = set()
    for i in file:
        i = i.split("\t")
        a.append(i[0])
        ziku.add(i[0])
    a.sort()
    out = {}
    n = 1
    for j in ziku:
        for k in a:
            if j == k:
                n += 1
                out[j] = n
            else:
                pass
    out = sorted(out.items(), key = lambda x: x[1], reverse=True)
    for b in out:
        print(b[0], str(b[1])+"回")