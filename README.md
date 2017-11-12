# Join Poster E2e Tests
## Requirements
1. python ver 2.7 should be installed
2. python pip should be installed
3. install requirements with pip install requirements.txt

Chromedriver added to project folder is temp solution, it should be in system PATH

example of execute command: 
> export MYURL="https://auto-qa-kur1.joinposter.com/manage/login" && export chromedriver_url="/media/accountant/682EC94264CD9EA9/data/test_qa/chromedriver" && python -m unittest finance_test_suite.FinanceTestSuite