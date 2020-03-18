C:\Python\python.exe D:/Documents/GitHub/Selenium/qasvus.wordpress.com_HM6.py
https://qasvus.wordpress.com/
https://qasvus.files.wordpress.com/2019/09/condominium-690086_1920.jpg?w=418
California Real Estate – QA at Silicon Valley Real Estate
Traceback (most recent call last):
  File "D:/Documents/GitHub/Selenium/qasvus.wordpress.com_HM6.py", line 19, in <module>
    driver.find_element_by_class_name("pushbutton-wide").click()  # not click ?????
  File "C:\Python\lib\site-packages\selenium\webdriver\remote\webelement.py", line 80, in click
    self._execute(Command.CLICK_ELEMENT)
  File "C:\Python\lib\site-packages\selenium\webdriver\remote\webelement.py", line 633, in _execute
    return self._parent.execute(command, params)
  File "C:\Python\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "C:\Python\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted: Element <button type="submit" class="pushbutton-wide">...</button> is not clickable at point (444, 682). Other element would receive the click: <div class="hide-on-button ads-active" data-hide-timeout="30" data-consent-expiration="180" id="eu-cookie-law">...</div>
  (Session info: chrome=80.0.3987.132)
