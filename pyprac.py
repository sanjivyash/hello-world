import math

# User defined class 
class Point(object):
	# Methods of the class
	def __init__(self,x=0,y=0):
		self.x = x
		self.y = y

	def __str__(self):
		return ("{},{}".format(self.x,self.y))

	def __add__(self,obj):
		x = self.x + obj.x
		y = self.y + obj.y
		p = Point(x,y)
		return p
	
	def print_attributes(self):
		for attr in self.__dict__:
			print(attr, getattr(self, attr))
	
	def distance(self,obj):
		x_diff = self.x - obj.x
		y_diff = self.y - obj.y
		return math.sqrt(x_diff**2 + y_diff**2)

# A function for file path stuff 
def linecount(filename):
	text = open(filename)
	count = 0
	for line in text:
		count += 1
	print(count)

# A function with point as input
def rotate(target,theta):
	answer = Point(0,0)
	answer.x = target.x*math.cos(theta)-target.y*math.sin(theta)
	answer.y = target.y*math.cos(theta)+target.x*math.sin(theta)
	return answer

# Main body to be written
if __name__ == '__main__':	
	# blank1 = Point()
	# blank2 = Point()
	# blank2.x = 3
	# blank2.y = 4
	blank1 = Point()
	blank2 = Point(3,4)
	add = blank1 + blank2 
	dist = blank1.distance(blank2)
	blank = Point(1,0)
	rot_blank = rotate(blank,math.pi/2)
	print(rot_blank.__dict__)
	rot_blank.print_attributes()
	add.print_attributes()
