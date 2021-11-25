import os
import json, time, requests
from stem import Signal
from urllib.request import urlopen
from stem.control import Controller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from time import sleep

#tor --service install -options ControlPort 9051
from selenium import webdriver

proxies = {
    'http': 'socks5://localhost:9050', 'https': 'socks5://localhost:9050'
}

class Connection:

    def __init__(self, url):

        self.url = url

        self.options = Options()
        self.options.add_argument("start-maximized")
        self.options.add_argument("--disable-infobars")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--disable-popup-blocking")
        self.options.add_argument('--log-level=3')
    
        torexe = os.popen(r'C:\CHANGE HERE\Tor Browser\Browser\TorBrowser\Tor')
        profile = FirefoxProfile(r'C:\CHANGE HERE\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default')
        profile.set_preference('network.proxy.type', 1)
        profile.set_preference('network.proxy.socks', '127.0.0.1')
        profile.set_preference('network.proxy.socks_port', 9050) #9051 up to you
        profile.set_preference("network.proxy.socks_remote_dns", False)
        profile.update_preferences()
        self._driver = webdriver.Firefox(firefox_profile= profile, executable_path=r'geckodriver.exe')

        self._load()

    def _load(self):
        #write active connection
        ipAddress = requests.get("http://api.ipify.org", proxies=proxies).text
        response = urlopen(f"http://ipinfo.io/{ipAddress}/json")
        data = json.load(response)
        city = data['city']
        country = data['country']
        region = data['region']
        provider = data['org']
        print(f"IP Address: {ipAddress} \t City: {city} \t Region: {region} \t Country: {country} \t Provider: {provider}")

        self._driver.get(self.url)

Connection('http://www.whatismyip.com')
