n1,n2= map( int,input().split())
s1=n1;s2=n2       
if s1<s2:
    while s1<=n2:
        print(s1,s2, end= '')
        s1= s1+1;s2= s2-1
        if s1<n2+1:
            print(end=' - ')
        elif s2>n2+1:
            print(end=' - ')
elif s1>s2:
    while s1>=n2:
        print(s1,s2, end=' ')
        s1=s1-1; s2=s2+1
        if s1>n2-1:
            print(end=' - ')
        
        
        