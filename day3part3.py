# mast question
age=int(input('Enter your age:'))
if age>18:
    print('you can ride the bike')
    petrol=int(input('Enter the cost of petrol'))
    if petrol<5:
        print("your ride id only for 3 hour",petrol)
    elif petrol>5 and petrol <10:
        print('your ride id only for 7 hour',petrol)   
    else:
        print('no time limit',petrol)     
else :
    print('you can not ride the bike ')    