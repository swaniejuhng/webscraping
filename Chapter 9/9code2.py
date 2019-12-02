
import requests

params = {'email_addr':'lulahpink@gmail.com'}
url = "http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi"
r = requests.post(url, data = params)
print(r.text)
