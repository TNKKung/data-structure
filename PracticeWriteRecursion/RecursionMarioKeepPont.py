ans=0
map=[]
def dfs(row,colume,sum):
    global ans
    sum=int(sum)+int(map[row][colume])
    print(sum)
    if(row == n-1 and colume ==n-1):
        print('++>>',sum)
        if(ans<int(sum)):
            print('++>>',sum)
            ans=int(sum)
        return 0
    if(row<n-1):
        dfs(row+1,colume,sum)
    
    if(colume<n-1):
        dfs(row,colume+1,sum)
    return 0
n = int(input('Enter Integer : '))
for i in range(0,n):  
 map.append([int(j) for j in input().split()]) 


dfs(0,0,0)
print(ans)