def my_abs(x):
	if x > 0 :
		return x
	else :
		return -x

def power(x, n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L

# 
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n
	return sum
# print(calc(*nums))

def person(name, age, **kw):
	print('name: ', name, 'age: ', 'other:', kw)

# person('billpoon', 27, city='zhongshan')

extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('Jack', 24, city=extra['city'], job=extra['job'])
# person('Jack', 24, **extra)

nums = [1, 2, 3, 4]

def person_check(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person_check('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

# print(my_abs(-9))

# print (power(2))

# print(add_end())

