# torproxy
A basic connection type of how to use Tor proxy + Selenium

Download Tor Browser to your OS and then find the Tor.exe
Run below code to open necessary permissions under your OS.

> tor.exe --service install -options ControlPort 9050

> tor.exe --service install -options ControlPort 9051

After all run py file.

#selenium

If you would like to merge Selenium capabilities with TOR connection, after you succesffuly install your webdriver (geckodriver), you can use the below code.

```python
 #add webdriver and other imports
 torexe = os.popen(r'C:\CHANGE HERE\Tor Browser\Browser\TorBrowser\Tor')
 profile = FirefoxProfile(r'C:\CHANGE HERE\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default')
 profile.set_preference('network.proxy.type', 1)
 profile.set_preference('network.proxy.socks', '127.0.0.1')
 profile.set_preference('network.proxy.socks_port', 9050) #9051 up to you.
 profile.set_preference("network.proxy.socks_remote_dns", False)
 profile.update_preferences()
 self._driver = webdriver.Firefox(firefox_profile= profile, executable_path=r'geckodriver.exe')
```

#Dont forget to change "CHANGE HERE" sections
