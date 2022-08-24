#para cargar la pagina antes de leer el contenido
# %% codecell
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml.html import fromstring
# %% codecell
# Fill forms
# https://iqss.github.io/dss-webscrape/filling-in-web-forms.html

# Free Proxies
# https://www.scrapehero.com/how-to-rotate-proxies-and-ip-addresses-using-python-3/
# %% codecell
def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:30]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            #Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies
# %% codecell
proxies = get_proxies()
print(proxies)
proxies_list = list(proxies)
proxies_list[0]
#proxies = ['121.129.127.209:80', '124.41.215.238:45169', '185.93.3.123:8080', '194.182.64.67:3128', '106.0.38.174:8080', '163.172.175.210:3128', '13.92.196.150:8080']

# PORXIES BY COUNTRY
# %% codecell
def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:100]:
        if i.xpath('.//td[4][contains(text(),"Japan")]'):
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                #Grabbing IP and corresponding PORT
                proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                proxies.add(proxy)
    return proxies
# %% codecell

from itertools import cycle
import traceback
proxy_pool = cycle(proxies)
url = 'https://httpbin.org/ip'
for i in range(1,3):
#Get a proxy from the pool
    proxy = next(proxy_pool)
    print("Request #%d"%i)
    try:
        response = requests.get(url,proxies={"http": proxy, "https": proxy})
        print(response.json())
    except:
    #Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work.
    #We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url
        print("Skipping. Connnection error")

DOWNLOADER_MIDDLEWARES = {
'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
}
ROTATING_PROXY_LIST = [
'125.21.3.41:8080',
'51.250.80.131:80',
# ...
]

# Proxy Chrome
# https://free-proxy-list.net/blog/rotating-proxy-selenium
PROXY = "133.18.195.135:8080" # demo proxy
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)
chrome = webdriver.Chrome(executable_path=r'C:/Users/carol/chromedriver_win32/chromedriver.exe', options=chrome_options)
chrome.get("http://checkip.amazonaws.com")
body_text = chrome.find_element_by_tag_name('body').text
print(body_text)
chrome.quit()

#Proxy Firefox
firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
proxy = "1.2.3.4:2000"
firefox_capabilities['proxy'] = {
    "proxyType": "MANUAL",
    "httpProxy": proxy,
    "ftpProxy": proxy,
    "sslProxy": proxy
}
driver = webdriver.Firefox(capabilities=firefox_capabilities)
driver.get("http://checkip.amazonaws.com")
body_text = driver.find_element_by_tag_name('body').text
print(body_text)
driver.quit()

# invisible IP
from torrequest import TorRequest
import torrequest
with torrequest.TorRequest(password=None) as tr:
    response= requests.get('http://ipecho.net/plain')
    print ("My Original IP Address:",response.text)

    #tr=TorRequest(password='your_unhashed_password here')
    tr.reset_identity() #Reset Tor
    response= tr.get('http://ipecho.net/plain')
    print ("New Ip Address",response.text)

# import unittest
#
# class GoogleTestCase(unittest.TestCase):
#
#     def setUp(self):
#         self.browser = webdriver.Firefox()
#         self.addCleanup(self.browser.quit)
#
#     def test_page_title(self):
#         self.browser.get('http://www.google.com')
#         self.assertIn('Google', self.browser.title)
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)
