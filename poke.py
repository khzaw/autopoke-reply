import requests
import mechanize
import sys

LOGIN_URL = 'https://m.facebook.com/login.php?next=https%3A%2F%2Fm.facebook.com%2Fpokes%2F&refsrc=https%3A%2F%2Fm.facebook.com%2Fpokes%2F&_rdrk'
EMAIL = sys.argv[1]
PASSWORD = sys.argv[2]


response = mechanize.urlopen(LOGIN_URL)
forms = mechanize.ParseResponse(response, backwards_compat=False)
login_form = forms[0]
email_control = login_form.find_control('email')
login_form.find_control('email').value = EMAIL
login_form.find_control('pass').value = PASSWORD
request = login_form.click()
try:
    response = mechanize.urlopen(request)
except mechanize.HTTPError, response:
    pass

print response.geturl()
