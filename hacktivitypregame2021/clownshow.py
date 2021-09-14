import requests
answer = 'hello'
r = requests.post("http://challenge.ctf.games:31600", data={'name': 'john', 'answer': answer, 'action': 'submit'})
print(r.status_code, r.reason)
