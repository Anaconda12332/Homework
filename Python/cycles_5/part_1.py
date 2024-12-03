def shapes(answers):
    if answers == 'а':
        b=11

        for i in range(1, 11): 
            print('|%20s|' %(' *' * (b-1))) 
            b -=1
           
    elif answers == 'б':
        b=0

        for i in range(1, 11):
            print('|%-20s|' %('* ' * (b + 1))) 
            b +=1
            
    elif answers == 'в':
        b=11
    
        for i in range(1, 11): 
            print('|{:^30}|'.format(' * ' * (b - 1)))
            b -=1

    elif answers == 'г':
        b=0
        
        for i in range(1, 11): 
            print('|{:^30}|'.format(' * ' * (b + 1)))
            b +=1
            
    elif answers == 'д':
        b=11
    
        for i in range(1, 11): 
            print('|{:^30}|'.format(' * ' * (b - 1)))
            b -=1
        b=0
        
        for i in range(1, 11): 
            print('|{:^30}|'.format(' * ' * (b + 1)))
            b +=1


def main():
    user_input=input('Какую фигуру вы хотите вывести?(а,б,в,г,д): ')
    return shapes(user_input)

       

if __name__=='__main__':
    main()