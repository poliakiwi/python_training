

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def click_to_create_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_field(self, field_name, text):
        wd = self.app.wd
        wd.find_element_by_name(field_name).click()
        wd.find_element_by_name(field_name).clear()
        wd.find_element_by_name(field_name).send_keys(text)

    def create(self, cont):
        wd = self.app.wd
        self.open_page_add_new_contact()
        self.fill_field("firstname", cont.fir)
        self.fill_field("middlename", cont.mid)
        self.fill_field("lastname", cont.las)
        self.fill_field("nickname", cont.nic)
        self.fill_field("title", cont.tit)
        self.fill_field("company", cont.com)
        self.fill_field("address", cont.add_1)
        self.fill_field("home", cont.tel_1)
        self.fill_field("mobile", cont.tel_2)
        self.fill_field("work", cont.tel_3)
        self.fill_field("fax", cont.tel_4)
        self.fill_field("email", cont.mail_1)
        self.fill_field("email2", cont.mail_2)
        self.fill_field("email3", cont.mail_3)
        self.fill_field("homepage", cont.hom)
        self.fill_field("address2", cont.add_2)
        self.fill_field("phone2", cont.hom_2)
        self.fill_field("notes", cont.not_2)
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

    def edit_first(self, text):
        wd = self.app.wd
        #open home page
        self.app.click_to_home_page()
        #click to edit
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        # changed name
        self.fill_field("firstname", text)
        #click to finish
        wd.find_element_by_name("update").click()
        #return to home page
        self.app.click_to_home_page()