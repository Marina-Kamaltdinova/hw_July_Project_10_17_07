import allure
from selene import browser, be, by


def test_steps():
    open_main_page()
    search_for_repository('Marina-Kamaltdinova/hw_July_Project_10_17_07')
    go_to_repository('Marina-Kamaltdinova/hw_July_Project_10_17_07')
    open_issue_tab()
    should_see_issue_with_name("С Новым Годом (2022)")


@allure.step('Открыть страницу')
def open_main_page():
    browser.open('/')


@allure.step('Найти репозиторий {repo}')
def search_for_repository(repo):
    browser.element('[data-target="qbsearch-input.inputButton"]').click()
    browser.element('#query-builder-test').send_keys(repo).press_enter()


@allure.step('Перейти в репозиторий {repo}')
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Открыть tab Issues')
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step("Проверяем Issue с названием {name}")
def should_see_issue_with_name(name):
    browser.element(by.partial_text(name)).click()
