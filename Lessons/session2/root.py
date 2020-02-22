from getpass import getpass
username = 'mindx'
password = 'xdmim'
loop = True
count = 0
while loop:
    count = count + 1
    # viết tắt: count += 1
    print(count)
    if count == 7:
        print('spam vừa thôi T.T')
        loop = False
        # False nhưng phải chạy đến hết vì vẫn thuộc vòng lặp while
    else:
        input_username = input('username?')
        if input_username == username:
            input_password = getpass()
            print(input_password)
            if input_password == password:
                print('Welcome to mindx')
                loop = False
            else:
                print('wrong password')
        else:
            print('wrong username')