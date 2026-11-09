import random

答案 = random.randint(1, 100)
次数 = 0

print("我想了一个 1 到 100 的数,来猜猜看!")

while True:
    猜 = int(input("你猜: "))
    次数 += 1
    if 猜 < 答案:
        print("小了")
    elif 猜 > 答案:
        print("大了")
    else:
        print(f"猜对了!你用了 {次数} 次")
        break
