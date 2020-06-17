cd D:
cd cd D:\Documents\GitHub\Selenium\UnitTests\For_Lessons
pytest --alluredir=allure-results TestStringMethod.py
allure generate ./allure-results
allure open
