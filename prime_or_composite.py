from readchar import readkey
print('Prime or Composite?')

wrong = True


def write_children():
    wrong = False
    n = input('write your number(from 2 to 50000): ')
    try:
        n = int(n)
        if n < 2 or n > 50000:
            wrong = True
            print('adade vaared shode khaarej az renge tarif shode ast!')
        else:
            n = int(n)
            m = int(n/2)

            def is_prime(n):
                avval = True
                for i in range(2, n):
                    if n % i == 0:
                        avval = False
                        break
                return avval
            t = []
            for i in range(2, m+1):
                if is_prime(i):
                    t.append(i)

            def bakhshpaziri(n, t):
                l = []
                for i in t:
                    if n % i == 0:
                        l.append(i)
                return l
            l = bakhshpaziri(n, t)
            if len(l) != 0:
                s = 'bar adaade avale '
                c = 0
                for i in l:
                    s += str(i)
                    if c < len(l)-1:
                        s += ', '
                    c += 1
                print(s, 'bakhsh pazir ast.')
            else:
                print(n, 'yek adade aval ast.')

            edame = input(
                'do you want continue?(please write "yes(y)" or "no(n)"): ')
            akbar = True
            while akbar:
                if edame == 'yes' or edame == 'y':
                    wrong = True
                    break
                if edame == 'no' or edame == 'n':
                    print('Finish!')
                    print('Programmed by M_ZRK\nPlease press any key to exit ...')
                    readkey()
                    break
                else:
                    print('your answer is not valid!')
                    edame = input(
                        'do you want continue?(please write "yes" or "no"): ')

    except ValueError:
        print('wrong input!')
        wrong = True
    return wrong


while wrong:
    wrong = write_children()
