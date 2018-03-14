# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contacts import Contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_add_contact(self):
        wd = self.wd
        self.open_site(wd)
        self.login(wd, user="admin", password="secret")
        self.open_page_add_new_contact(wd)
        self.fill_contact(wd, Contact(fir="fir1", mid="mid1", las="las1", nic="nic1", tit="tit1", com="com1", add_1="add1",
                     tel_1="111", tel_2="222", tel_3="333", tel_4="444", mail_1="a1@a.ru", mail_2="a2@a.ru",
                     mail_3="a3@a.ru", hom="hom1.ru", dat_1="21_11", yea_1="82", dat_2="27_11", yea_2="81", add_2="add2", hom_2="hom2", not_2="not2"))
        self.click_to_create_contact(wd)
        self.home_page(wd)
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_site(wd)
        self.login(wd, user="admin", password="secret")
        self.open_page_add_new_contact(wd)
        self.fill_contact(wd, Contact(fir="", mid="", las="", nic="", tit="", com="", add_1="",
                     tel_1="", tel_2="", tel_3="", tel_4="", mail_1="", mail_2="",
                     mail_3="", hom="", dat_1="", yea_1="", dat_2="", yea_2="", add_2="", hom_2="", not_2=""))
        self.click_to_create_contact(wd)
        self.home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def click_to_create_contact(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_contact(self, wd, cont):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(cont.fir)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(cont.mid)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(cont.las)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(cont.nic)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(cont.tit)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(cont.com)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(cont.add_1)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(cont.tel_1)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(cont.tel_2)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(cont.tel_3)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(cont.tel_4)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(cont.mail_1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(cont.mail_2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(cont.mail_3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(cont.hom)
        if cont.dat_1 == "21_11":
            if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[23]").is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[23]").click()
            if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[12]").is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[12]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(cont.yea_1)
        if cont.dat_2 == "27_11":
            if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[29]").is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[29]").click()
            if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[12]").is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[12]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(cont.yea_2)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(cont.add_2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(cont.hom_2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(cont.not_2)

    def open_page_add_new_contact(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, user, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_site(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
