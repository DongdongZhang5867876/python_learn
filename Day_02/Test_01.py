int_true_age = 18
count = 0
while True:
    count += 1
    if count <= 3:
        int_guess_age = int(input('你猜我多大了啊：\n'))
        if int_guess_age < int_true_age:
            print('猜小了哦！')
        elif int_guess_age > int_true_age:
            print('猜大了哦！')
        else:
            print("yeah,you're right!")
            break
    else:
        is_continue = input('已经三次了哦，你要继续猜吗？(Y/N)\n').lower()
        if is_continue == 'y':
            count = 0
            continue
        elif is_continue == 'n':
            print('Game over!')
            break
        else:
            print('我说了你只能输入(Y/N)（大小写均可）！你不听话不和你玩了！')
            break