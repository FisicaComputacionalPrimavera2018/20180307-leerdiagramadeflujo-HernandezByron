Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print "la suma de los numeros pares"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("la suma de los numeros pares")?
>>> #suma de los numeros pares del 1 al 10
>>> n= 0
>>> s = 0
>>> while n<10:
	s+=n
	if n%2==0:
		print n
		
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(t n)?
>>> while n<10:
	s+=n
	if n%2==0:
		print (n)
		n+=1
		print ("la suma es:")
		
