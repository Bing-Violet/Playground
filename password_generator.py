import random
import re


def rand_password(length=4):
	password = []
	while len(password) < length:
		num = random.randint(0, 9)
		if check_prev_num(password, num):
			continue
		else:
			password.append(num)
	password_str = ''.join([str(elem) for elem in password]) 

	return password_str


def check_prev_num(password, num):

    if len(password) == 0:
        return False
    else:
        prev_num = password[-1]
        if prev_num == num:
            return True
        else:
            return False

print(rand_password(4))

def password_generator(num=100): 
	password_collection = []
	while len(password_collection) < 100: 
		password = rand_password(4)
		if re.search(r"123|234|345|456|567|678|789", password):
			continue
		else:
			password_collection.append(password)

	else:
		return password_collection

print(password_generator(100))



