#!/bin/bash

pytest --browser_name=firefox -v --alluredir=allure_test_results
pytest --browser_name=chrome -v --alluredir=allure_test_results

#Select suits
##pytest --browser_name=chrome -v -k AddToBasket
#pytest --browser_name=chrome -v -s --alluredir=allure_test_results -k test_success_msg


# Prompt:
# pytest -rxXs  # show extra info on xfailed, xpassed, and skipped tests
# Run test with mark -m login_guest
# Run test --tb=line - only one line per failure
#pytest --browser_name=chrome -rxXs -v -s ./Tests/test_product_page.py
#pytest --browser_name=firefox -rxXs -v -s ./Tests/test_product_page.py

# Commands with allure attribute:
#pytest --browser_name=chrome -v -s --alluredir=allure_test_results ./Tests/test_basket_page.py
#pytest --browser_name=chrome -v -s --alluredir=allure_test_results ./Tests/test_product_page.py
#pytest --browser_name=firefox -v -s --alluredir=allure_test_results ./Tests/test_product_page.py
#pytest --browser_name=chrome -v --alluredir=allure_test_results ./Tests/test_login_page.py
#pytest --browser_name=firefox -v --alluredir=allure_test_results ./Tests/test_login_page.py
