import turtle as ttl

def kochCurve(x, m):

	if x < m:	#true
		ttl.forward(x)
	else:
		kochCurve(x/3, m)
		ttl.left(60)

		kochCurve(x/3, m)
		ttl.right(120)

		kochCurve(x/3, m)
		ttl.left(60)

		kochCurve(x/3, m)

def kochSnowflake(x, m):
	kochCurve(x,m)
	ttl.right(120)
	ttl.fillcolor("blue")
	kochSnowflake(x+2,m)

ttl.fillcolor("red")
ttl.speed(0)
kochSnowflake(100, 200)
ttl.exitonclick()