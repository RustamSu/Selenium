cd D:
cd d:\Documents\GitHub\Selenium\Allure
pytest --alluredir=allure-results Allure_Unittest.py
allure generate ./allure-results
allure open
