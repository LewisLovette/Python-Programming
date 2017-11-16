class Fraction:

	def __init__(self, n, d):
		self.n = n
		self.d = d
		if self.n.isdigit() == False or self.d.isdigit() == False:
			raise ValueError("Input integers only.")

		if self.d == 0:
			raise ValueError("Denominator cannot be 0.")

		if self.d < 0:
			if self.n >= 0:
				negN = self.n - self.n*2
			else:
				negN = self.n
			negD = self.d
			negativeD = Fraction(negN, negD)

	def __str__(self):
		print(self.n+"/"+self.d)


misc = Fraction(5, 4)
negMisc = Fraction(4, -6)

print(str(misc))
print(str(negMisc))
