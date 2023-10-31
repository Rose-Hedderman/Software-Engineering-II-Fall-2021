import requests
import json



def api1():
	response = requests.get('http://api.open-notify.org/astros.json')
	print(response.status_code)
	print(response.json())

def api2():
	parameters = {
		'lat': 30.2672,
		'lon': -97.7431
	}

	response = requests.get('http://api.open-notify.org/iss-pass.json', params=parameters)

	print(response.status_code)
	print(response.json())

	from datetime import datetime

	times = response.json()['response']
	
	for t in times:
		time = datetime.fromtimestamp(t['risetime'])
		print(time)

def api3():
	response = requests.get('https://gitlab.com/api/v4/users/fareszf/projects')
	print(response.status_code)
	print(response.json())

def api4():
	
	parameters = {
		'private_token': 'kYsSkTp4kNxj8Z6bN4R4',
	}

	project_id = str(11498012)

	url = 'https://gitlab.com/api/v4/projects/' + project_id + '/repository/commits'

	response = requests.get(url, params=parameters)
	print(response.status_code)
	content = response.json()
	
	for c in content:
		print(c, '\n')

def api5():
	
	response = requests.get('http://127.0.0.1:5000/api')
	print(response.status_code)
	print(response.json())


def api6():

	headers = {"Content-type": "application/json",
          "Accept": "text/plain"}

	books = [{'title': 'Software Engineering', 'id': '1'}, \
         {'title':'Algorithm Design', 'id':'2'},       \
         {'title':'Python', 'id':'3'}]

	data = json.dumps(books)
	#headers = json.dumps(headers) # incorrect

	url = "http://google.com"

	response = requests.post(url, data=data, headers=headers)



if __name__ == "__main__":
	# api1()
	# api2()
	# api3()
	# api4()
	# api5()
	api6()