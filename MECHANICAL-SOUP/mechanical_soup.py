import mechanicalsoup

browser = mechanicalsoup.Browser(soup_config={"features":"lxml"})
login_page = browser.get("https://github.com/login")
login_form = login_page.soup.select("#login")[0].select("form")[0]
login_form.select("#login_field")[0]['value'] = 'mananpal1997'
login_form.select("#password")[0]['value'] = '**********'
page2 = browser.submit(login_form, login_page.url)
print(page2.soup.title.text)
