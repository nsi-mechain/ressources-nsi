def puissance_iter(x, n):
   resultat = 1
   for i in range(n):
       resultat *= x
   return resultat


def puissance_recur(x, n):
   if n == 0:
       return 1
   else:
       return x * puissance_recur(x, n - 1)


print(puissance_iter(5, 3))
print(puissance_recur(5, 3))
