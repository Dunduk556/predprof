f=open("game.txt",encoding="UTF-8")
sp=[]
for i in f:
    sp.append(i.split("$"))
for i in sp:
    if "55" in i[2] :
        print("У персонажа",i[1],"в игре",i[0],"нашлась ошибка с кодом:",i[2],".Дата фиксации:",i[3][:-1])

for i in range(len(sp)):
            if "55" in sp[i][2]:
                sp[i][2]="Done"
                sp[i][3]="0000-00-00"+"\n"

f1 = open('game_new.csv', 'w', encoding="UTF-8")
for i in range(0, len(sp)):
    f1.write(str(sp[i][0]) + ',' + str(sp[i][1]) + ',' + str(sp[i][2]) + ',' + str(sp[i][3]))

f.close()
f1.close()
