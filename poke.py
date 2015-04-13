from mechanize import Browser
import sys

LOGIN_URL = 'https://m.facebook.com/login.php?next=https%3A%2F%2Fm.facebook.com%2Fpokes%2F&refsrc=https%3A%2F%2Fm.facebook.com%2Fpokes%2F&_rdrk'
EMAIL = sys.argv[1]
PASSWORD = sys.argv[2]


browser = Browser()
browser.set_handle_robots(False)
browser.set_handle_refresh(False)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
browser.open(LOGIN_URL)
browser.select_form(nr=0)
browser.form['email'] = EMAIL
browser.form['pass'] = PASSWORD
browser.submit()
for link in browser.links():
    if link.text == "[IMG]Poke Back":
        browser.click_link(link)
        browser.follow_link(link)
