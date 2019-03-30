DENTIST_URL = "http://0.0.0.0:5000/v1"
url = DENTIST_URL+"/dentists?offset={}&limit={}&location={}&name={}".format(0,10,"jakarta","tio")

print(url)