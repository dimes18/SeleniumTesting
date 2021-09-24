from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains

if __name__ == "__main__":
    # bin_arg = FirefoxBinary('%PROGRAMFILES%\Mozilla Firefox\firefox.exe')
    capabilities_argument = DesiredCapabilities().FIREFOX
    capabilities_argument["marionette"] = True
    exe_path = 'C:\\Selenium\\SeleniumTesting\\geckodriver.exe'
    webpagedriver = webdriver.Firefox(capabilities=capabilities_argument,
                                      executable_path=exe_path)

    webpagedriver.get('https://www.airnewzealand.co.nz/homepage')

    sign_in = '//*[@id="masthead-nav"]/div/div/div[2]/div/nav/div[2]/div[3]/div[3]/div/a'
    signin_button = '/html/body/form/div/div/div/div/div[2]/div[1]/div/div[4]/div/button'
    user_name = '//*[@id="header-myairnz-username"]'
    pwd = '//*[@id="header-myairnz-password"]'
    signout = '//*[@id="masthead-nav"]/div/div/div/div/nav/div[2]/div[3]/div/div/a'
    book_menu_item = '//*[@id="masthead-nav"]/div/div/div[2]/div/nav/div[2]/div[1]/div[2]/div[1]/div/a/div/span'
    flight_booking_subitem = '//*[@id="pwhm.1784"]/div[1]/div[1]/a/div/span'

    book_search = '//*[@id="search-panel-container"]/div/div/form/div[10]/button'

    onewway_trip = '//*[@id="search-panel-container"]/div/div/form/div[3]/div[2]/div/label'
    from_ap = '//*[@id="depart-from"]'
    to_ap = '//*[@id="depart-to"]'
    leave_date = '//*[@id="leaveDate"]'
    #date format = '02/10'

    destination_ap = '//*[@id="vui-leg-0"]/div/div/vui-si-legheading/div/h2/span[2]/span[3]'

    list_dates = '//*[@id="vui-leg-0"]/vui-scrollcalendar/div/div/div/div/div/ul'
    element_date = '/li[1]'

    right_arrow = '//*[@id="vui-leg-0"]/vui-scrollcalendar/div/div/div/div/a[2]'

    left_arrow = '//*[@id="vui-leg-0"]/vui-scrollcalendar/div/div/div/div/a[1]'

    #click sign in

    #wait for signin form

    #wait dashboard by checking signout link

    #click book item

    #click flight submenu item

    #wait for book_search button

    #select 1 way trip

    #enter details

    #click search

    #wait for destination airport to appear

    #loop each of the list elements if there's entry not showing 'No seats available' or it's showing $

    #click the next right arrow to scrol the dates
    WebDriverWait(webpagedriver, 20).until(lambda webpagedriver: webpagedriver.find_element_by_name(loc))
    obj = webpagedriver.find_element_by_xpath(loc)
    print("Brand: {}".format(obj.text))