def shapes(answers):
    S=21

    match answers:
        case'а':
            return [['*' if j>i-1 else ' ' for j in range(S)
                    ] for i in range(S)]
            

        case'б':
            return [['*' if j<i+1 else ' ' for j in range(S)
                    ] for i in range(S)]


        case'в':
            return [['*' if (S)//2-(i-(S//2)) >= j >= (S)//2+(i-(S//2)
                    ) else ' ' for j in range(S)] for i in range(S)]


        case'г':
            return [['*' if (S)//2-(i-(S//2)) <= j <= (S)//2+(i-(S//2)
                    ) else ' ' for j in range(S)] for i in range(S)]


        case'д':
            return [['*' if (S)//2-(i-(S//2)) <= j <= (S)//2+(i-(S//2)
                    ) or (S)//2-(i-(S//2)) >= j >= (S)//2+(i-(S//2)
                    ) else ' ' for j in range(S)] for i in range(S)]


        case'е':
            return [['*' if (S)//2-(i-(S//2)) >= j >= (S)//2+(i-(S//2)
            ) or (S)//2-(i-(S//2)) <= j <= (S)//2+(i-(S//2)
            ) else ' ' for i in range(S)] for j in range(S)]
        

        case'ж':
            return [['*' if (S)//2-(i-(S//2)) >= j >= (S)//2+(i-(S//2)
            ) else ' ' for i in range(S)] for j in range(S)]


        case'з':
            return [['*' if (S)//2-(i-(S//2)) <= j <= (S)//2+(i-(S//2)
            ) else ' ' for i in range(S)] for j in range(S)]
        

        case'и':
            return [['*' if j<S-i else ' ' for j in range(S)
                    ] for i in range(S)]


        case'к':
            return [['*' if j>=S-i-1 else ' ' for j in range(S)
                    ] for i in range(S)]




def main():

    user_input=input('Какую фигуру вы хотите вывести?'
                     + '\n' + '(а,б,в,г,д,е,ж,з,и,к): ')

    for i in shapes(user_input):
        print(*i)


if __name__=='__main__':
    main()

