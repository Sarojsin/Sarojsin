# plane ticket booking
name=input('Enter the name of user:')
Duration_time=('Chose the peorid of time you want:')
age=input('Enter the age:')
booking_seat=int(input('Enter the number of seat u want'))
if booking_seat>1:
    print('you are getting the some discount')
    if booking_seat ==2:
        print("your amount is 6500")
    elif booking_seat ==3:
        print('your amount is 6000')
    elif booking_seat==4:
          print('your amount is 5500') 
    else:
        print('contact to thr air line for more booking')       
else:
    print('you need to pay 70000')    