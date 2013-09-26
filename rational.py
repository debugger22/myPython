class Rational:
	"""
	This class allows operations of rational number on its objects
	"""
	def __init__(self,num, den=1):
		self.num = num
		self.den = den
		self.simplify()
	
	def __str__(self):
		return `self.num`+"/"+`self.den`	
	
	def __add__(self,other):
		if not isinstance(other, Rational):
			other = Rational(other)
		new = Rational((self.num*other.den+self.den*other.num),self.den*other.den)
		new.simplify()
		return new

	def __sub__(self,other):
		if not isinstance(other, Rational):
			other = Rational(other)
		new = Rational((self.num*other.den-self.den*other.num),self.den*other.den)
		new.simplify()
		return new

	def __mul__(self,other):
		if not isinstance(other, Rational):
			other = Rational(other)
		new = Rational((self.num*other.num),self.den*other.den)
		new.simplify()
		return new

	def __div__(self, other):
		if not isinstance(other, Rational):
			other = Rational(other)
		new = Rational(self.num*other.den,self.den*other.num)
		new.simplify()
		return new

	def simplify(self):
		while(True):
			gcd = self.getGCD(self.num, self.den)
			if gcd == self.num or gcd == self.den or gcd ==1:
				break
			else:
				if gcd==self.num:
					self.num = gcd
				elif gcd==self.den:
					self.den = gcd
				else:
					self.num /= gcd
					self.den /= gcd		

	def getGCD(self,a,b):
		maxm = max(a,b)
		minm  = min(a,b)
		if maxm%minm == 0:	
			return minm
		else:
			rem = maxm%minm
			return self.getGCD(minm,rem)