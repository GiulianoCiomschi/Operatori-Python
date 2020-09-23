n=1364
print("Dă un număr natural n (n<10000) =",n)
print("Ultima cifră a acestui număr =",n % 10)
print("Penultima cifră a acestui număr=",(n//10)%10)
print("Restul şi câtul împărţirii acestui număr la 9:",n % 9,"și", n//9)
print("Suma cifrelor acestui număr=",n//100%10 + n//10%10 + n%10+ n//1000)
print("Răsturnatul acestui număr=",n%10,n//10%10,n//100%10,n//1000)