import requests

res = requests.post('http://65.20.89.184/api/login/')

print(res.status_code)