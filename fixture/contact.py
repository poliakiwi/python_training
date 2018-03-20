

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def click_to_create_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def create(self, cont):
        wd = self.app.wd
        self.open_page_add_new_contact()
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
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(cont.add_2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(cont.hom_2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(cont.not_2)
        self.click_to_create_contact()
        self.app.click_to_home_page()

    def open_page_add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def del_first(self):
        wd = self.app.wd
        #open home page
        self.app.click_to_home_page()
        #click on check-box
        wd.find_element_by_name("selected[]").click()
        #click on delete
        wd.find_element_by_xpath("//input[@onclick='DeleteSel()']").click()
        # wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        #click to agree
        wd.switch_to_alert().accept()
        #return to home page
        self.app.click_to_home_page()

    def edit_first(self):
        wd = self.app.wd
        #open home page
        self.app.click_to_home_page()
        #click to edit
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        # changed name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("changed firstname")
        #click to finish
        wd.find_element_by_name("update").click()
        #return to home page
        self.app.click_to_home_page()