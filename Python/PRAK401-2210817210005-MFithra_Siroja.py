angka=int(input())
simbol=input()
for a in range(1, 51):
 if a % angka == 0 :
   print( simbol, end=' ')
 else :
   print( a, end= ' ')