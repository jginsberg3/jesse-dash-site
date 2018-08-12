# read in login info from the password file

def return_login_info(password_file_name):
	'''
	read in login info
	'''
	with open(password_file_name) as f:
		logins = f.readlines()

	login_list = []

	for line in logins:
		line = line.split(',')

		clean_line = []
		for i in line:
			clean_line.append(i.rstrip())

		login_list.append(clean_line)

	return login_list