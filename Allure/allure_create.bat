cd D:
cd d:\Documents\GitHub\Selenium\Allure
pytest --alluredir=reports_unit Allure_pytest_class.py
allure generate --clean ./allure-results  && allure open
rem allure serve ./allure-results