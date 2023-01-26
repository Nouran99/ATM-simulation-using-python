print('Nice to meet you!')
password = 1234
userpass = int(input('Enter your password :  '))
if  userpass == password :
    flag1 = 1
else:
    print('wrong password')
    flag1 = 0

Account_Balance = 30000

while ( True ):
    print("\n\n")
    print("1. Withdraw Cash")
    print("2. View Account Balance")
    print("3. Fast Cash")
    print("4. Quit")
    req = int(input("Enter number to proceed > "))
    print("\n\n")

    match req:

        case 4:
            print("Exiting...")
            print("\n\n")
            print("See you again. Thank you!")
            flag1 =0
            break

        case 2:
            print("your Account Balance is = ", Account_Balance)
            continue

        case 3:
            print("\n\n")
            print("1. 100")
            print("2. 1000")
            print("3. 10000")
            print("4. 100000")
            amount = int (input("Enter the amount > "))
            match amount :
                    case 1 if Account_Balance > 100:
                            print("TRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
                            Account_Balance-=100
                            print("your Account Balance is = ", Account_Balance)


                    case 2 :
                        if Account_Balance > 1000 :
                            print("TRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
                            Account_Balance-= 1000
                            print("your Account Balance is = ", Account_Balance)
                        else:
                            print ("this value is forbeden")
                        continue

                    case 3 :
                        if Account_Balance >10000 :
                            print("TRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
                            Account_Balance -= 10000
                            print("your Account Balance is = ", Account_Balance)
                        else:
                            print ("this value is forbeden")
                        continue
                    case 4:
                        if Account_Balance > 100000 :
                            print("TRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
                            Account_Balance -= 100000
                            print("your Account Balance is = ", Account_Balance)
                        else:
                            print ("this value is forbeden")
                        continue

                    case _:
                        print("wronge choice")
                        continue
            continue

        case 1 :
            amou =int(input("choose the amount >>"))
            if Account_Balance > amou and amou %100==0:
                print("TRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
                Account_Balance -= amou
                print("your Account Balance is = ", Account_Balance)
            else:
                print ("this value is forbeden")
            continue
