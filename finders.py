def find(driver, xpath):
    try:
        return driver.find_element_by_xpath(xpath)
    except:
        print("Couldn't find " + xpath)
        return None


def get_text(driver, xpath):
    i = 1
    suffix = ''
    result = ""
    while find(driver, xpath + suffix) is not None:
        if result == "":
            result = find(driver, xpath + suffix).text.strip()
        else:
            result = result + "\n" + find(driver, xpath + suffix).text.strip()
        i = i + 1
        suffix = '[' + str(i) + ']'
    return None if result == "" else result


name = '//*[@id="acalog-page-title"]'
desc = '//*[@id="gateway-page"]/body/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[1]/td/p'
admis_req = '//*[@id="gateway-page"]/body/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div[1]'
deg_req = '//*[@id="gateway-page"]/body/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div[2]'
