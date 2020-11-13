class funString :
    def findLen(string):
         String = len(string)
         return String
    def spread_Shrink(string,word=''):
        b = list(string)
        c = []
        for i in b :
            if (i >= 'A' and i <= 'Z') :
                c.append(chr(ord(i)+32))
            else :
                c.append(chr(ord(i)-32))
        return word.join(c)
    def reverseStr(string) :
        i = string[::-1]
        return i
    def delete_str(string,word='') :
        e = []
        for i in a :
             if i not in e :
                e.append(i)
        return word.join(e)



a,sec = input('Enter String and Number of Function : ').split(' ')

if sec == '1':
    print(funString.findLen(a))
if sec == '2':
    print(funString.spread_Shrink(a))
if sec == '3':
    print(funString.reverseStr(a))
if sec == '4':
    print(funString.delete_str(a))


