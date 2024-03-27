f=open("game.txt",encoding="UTF-8")
sp=[]
for i in f:
    sp.append(i.split("$"))

while True:
    flag = False
    zapros = input('Введите имя персонажа - ')
    if zapros == 'game':
        break
    else:
        a=[]
        k=0
        for i in range(len(sp)):
            if sp[i][1] == zapros:
                k+=1
                if k==1:
                    print("Персонаж",zapros,"встречается в играх:")
                if k<=5:
                    print(sp[i][0])
                if k>5:
                    print("и др")
                    break
                flag = True

        if not(flag):
            print('Этого персонажа не существует')

f.close()
