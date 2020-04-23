from time import sleep
from python_rucaptcha import ReCaptchaV2

#command_exec ='https://aleksandrkuzhele1:sxi8y58EkWTvHGNboy33@hub-cloud.browserstack.com/wd/hub'
command_exec = 'http://178.128.127.131:4444/wd/hub'

form_url = 'http://www.123formbuilder.com/form-5012215/online-order-form'

######## XPATHs ###############
XNameForm = "//h1[text()='Order Form']"
XFirstName = "//input[@placeholder='First']"
XLastName = "//input[@placeholder='Last']"
XEmail = "//input[@type='email']"
XPhone = "//input[@placeholder='### ### #### ']"
XQuantity = "//input[@type='number']"
XCalendar = "//body/form[@id='form']/div/div/div/div/div/div/div[2]"
XStreet1 = "//input[@placeholder='Street Address']"
XStreet2 = "//input[@placeholder='Street Address Line 2']"
XCity = "//input[@placeholder='City']"
XRegion = "//input[@placeholder='Region']"
XZipCode = "//input[@placeholder='Postal / Zip Code']"
XCountry = "//input[@placeholder='Country']"
XSelCountry = "//*[contains(text(), 'Zambia')]"
XExtText = "//input[@type='text'][@data-role='other']"

def SolveCapcha():
    # Введите ключ от сервиса RuCaptcha, из своего аккаунта
    RUCAPTCHA_KEY = "53da620a6ac51a8ad6adc5bc9bac7822"
    # G-ReCaptcha ключ сайта
    SITE_KEY = "6LdMNiMTAAAAAGr0ibqKRZc3e5Z6wfLBraX9NuOY"
    # Ссылка на страницу с капчёй
    PAGE_URL = "http://www.123formbuilder.com/form-5012215/online-order-form"
    # Возвращается JSON содержащий информацию для решения капчи
    user_answer = ReCaptchaV2.ReCaptchaV2(rucaptcha_key=RUCAPTCHA_KEY).captcha_handler(site_key=SITE_KEY, page_url=PAGE_URL)
    #if not user_answer['error']:
    # решение капчи
    #    print('captchaSolve: ', user_answer['captchaSolve'])
    #    print('taskId ', user_answer['taskId'])
    #elif user_answer['error']:
    # Тело ошибки, если есть
    #    print(user_answer['errorBody']['text'])
    #    print(user_answer['errorBody']['id'])
    sleep(2)
    #driver.execute_script("document.getElementById('text_field').value+='{0}'".format(foo))
    capt = user_answer['captchaSolve']
    #вставляем в скрытое поле
    return str("javascript:document.getElementById('g-recaptcha-response').value = '{0}';".format(capt))





