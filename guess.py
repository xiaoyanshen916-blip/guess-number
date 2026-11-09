import random

答案 = random.randint(1, 100)
次数 = 0
最多 = 7

print("我想了一个 1 到 100 的数,你有 7 次机会!")

while 次数 < 最多:
    猜 = int(input("你猜: "))
    次数 += 1
    if 猜 < 答案:
        print(f"小了,还剩 {最多 - 次数} 次")
    elif 猜 > 答案:
        print(f"大了,还剩 {最多 - 次数} 次")
    else:
        print(f"猜对了!你用了 {次数} 次")
        break
else:
    print(f"没猜中,答案是 {答案}")
