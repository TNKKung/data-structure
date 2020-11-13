string = input('Enter String : ')
a,ans = [],[]
for x in string :
    if x not in a:
        a.append(x)
    ans.append(a.index(x))
print(ans)

