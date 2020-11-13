def generate(n, l):
    if n == 0:
        if len(l) == 0:
            print(0)
        else:
            print('\n'.join(l))
    else:
        if len(l) == 0:
            return generate(n - 1, ['0', '1'])
        else:
            return generate(n - 1, ['0' + i for i in l] + ['1' + i for i in l])


inp = int(input('Enter Number : '))
if inp < 0:
    print('Only Positive & Zero Number ! ! !')
else:
    generate(inp, [])
