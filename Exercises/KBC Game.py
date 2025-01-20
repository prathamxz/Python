Questions = [
    ["Which language was used to create facebook ?",
"Python","Java","C","PHP","French","None",5],

    ["Which language was used to create insta ?",
"Python","Java","C","PHP","French","None",5],

    ["Which language was used to create whatsapp ?",
"Python","Java","C","PHP","French","None",5],

    ["Which language was used to create facetime ?",
"Python","Java","C","PHP","French","None",5]
]

levels = [1000, 2000, 3000, 5000,8000,12000,15000,19000,23300,123322]
money = 0

for i in range(0 , len(Questions)):
    Questions=Questions[i]
    print(f"Question for Rs {levels[i]}")
    print(f"a.{Questions[1]}        b.{Questions[2]}")
    print(f"c.{Questions[3]}        d.{Questions[4]}")
    print(f"e.{Questions[5]}        f.{Questions[6]}")
    reply = int(input("Enter your Answer (1-4) : "))
    if reply ==Questions[-1]:
        print(f"Congratulations! Your answer is correct, you have won Rs {levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 1000000
    else:
        print("Sorry! Your answer is wrong, you have won Rs 0")
        break