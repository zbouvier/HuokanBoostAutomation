
# Date and time of the run: 6/29/2020 at 11:08 am cst
# Offer poster (@Name-Realm): @Braelight-Zul'jin 
# Tank (@Name-Realm): @Kiwey-Zul'jin 
# Healer (@Name-Realm): @Abicas-Zul'jin 
# DPS1 (@Name-Realm): @Nyntein-Illidan 
# DPS2 (@Name-Realm): @Embreo-illidan

contents = []
while True:
    try:
        line = input()
        
        if(line == ""):
            break
        else:
            x = line.split(': @')
    except EOFError:
        break
    contents.append(x[1])

keyLevel = input("Level of key -> ")
keyType = input("base, armor stack, timed, key etc.. -> ")
print("---------------")
print("!keycompleted")
print("Braelight-Zul'jin")
print("unpaid")
print(keyLevel)
print(keyType)
print("0")
for thing in contents:
    print(thing)
