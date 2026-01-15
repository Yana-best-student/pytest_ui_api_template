from page.AuthPage import AuthPage
from page.MainPage import MainPage


def test_auth(browser):
    email = "y29753004@gmail.com"
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, "Artem270920@")

    main_page = MainPage(browser)
    main_page.open_menu()

    info = main_page.get_account_info()
    
    assert main_page.get_current_url().endswith("/y29753004/boards")
    assert info[0] == "Yana"
    assert info[1] == email
    