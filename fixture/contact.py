

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, cont):
        wd = self.app.wd
        self.open_page_add_new_contact()
        self.fill_form(cont)
        self.click_to_create_contact()
        self.app.click_to_home_page()

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

    def edit_first(self, new_contact_data):
        wd = self.app.wd
        #open home page
        self.app.click_to_home_page()
        #click to edit
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        # changed
        self.fill_form(new_contact_data)
        # self.change_field("firstname", text)
        #click to finish
        wd.find_element_by_name("update").click()
        #return to home page
        self.app.click_to_home_page()

    def click_to_create_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_page_add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def count(self):
        wd = self.app.wd
        #open home page
        self.app.click_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def fill_form(self, cont):
        wd = self.app.wd
        self.change_field("firstname", cont.fir)
        self.change_field("middlename", cont.mid)
        self.change_field("lastname", cont.las)
        self.change_field("nickname", cont.nic)
        self.change_field("title", cont.tit)
        self.change_field("company", cont.com)
        self.change_field("address", cont.add_1)
        self.change_field("home", cont.tel_1)
        self.change_field("mobile", cont.tel_2)
        self.change_field("work", cont.tel_3)
        self.change_field("fax", cont.tel_4)
        self.change_field("email", cont.mail_1)
        self.change_field("email2", cont.mail_2)
        self.change_field("email3", cont.mail_3)
        self.change_field("homepage", cont.hom)
        self.change_field("address2", cont.add_2)
        self.change_field("phone2", cont.hom_2)
        self.change_field("notes", cont.not_2)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)