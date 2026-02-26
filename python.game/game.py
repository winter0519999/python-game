import random

print("🎮 歡迎來到猜數字遊戲！")
print("我已經想好一個 1 到 100 的數字。")

number = random.randint(1, 100)
guess = None
attempts = 0

while guess != number:
    guess = int(input("請輸入你的猜測數字："))
    attempts += 1

    if guess < number:
        print("太小了！再試一次。")
    elif guess > number:
        print("太大了！再試一次。")
    else:
        print(f"🎉 恭喜你猜對了！總共猜了 {attempts} 次。")
        