cd D:
cd d:\Documents\GitHub\Selenium\Allure
pytest --alluredir=allure-results Allure_Unittest.py
rem тут просто количество тестов, в каждом файле по три теста
pytest --alluredir=allure-results Allure_Unittest.py
rem pytest --alluredir=allure-results Allure_Unittest.py
allure serve ./allure-results