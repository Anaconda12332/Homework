def shapes(answers):
    if answers == 'е':
        b=0
        
        for i in range(1, 6): 
            print('|{:<10}'.format(('* ' * (b+1))), end='')
            b +=1
            print('{:>10}|'.format((' *' * b)))
            
        for i in range(1, 5): 
            print('|{:<10}'.format(('* ' * (b-1))), end='')
            b -=1
            print('{:>10}|'.format((' *' * b)))
                            
    elif answers == 'ж':
        b=0

        for i in range(1, 6): 
            print('|{:<10}|'.format(('* ' * (b+1))))
            b +=1

        for i in range(1, 5): 
            print('|{:<10}|'.format(('* ' * (b-1))))
            b -=1
            
    elif answers == 'з':
        b=0

        for i in range(1, 6): 
            b +=1
            print('|{:>10}|'.format((' *' * b)))
            
        for i in range(1, 5): 
            b -=1
            print('|{:>10}|'.format((' *' * b)))

    elif answers == 'и':
        b=11

        for i in range(1, 11): 
            print('|{:<30}|'.format(' * ' * (b - 1)))
            b -=1
            
    elif answers == 'к':
        b=0

        for i in range(1, 11): 
            print('|{:>30}|'.format(' * ' * (b + 1)))
            b +=1

       
def main():
    user_input=input('Какую фигуру вы хотите вывести?(е,ж,з,и,к): ')
    return shapes(user_input)


if __name__=='__main__':
    main()