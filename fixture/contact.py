from model.contacts import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, cont):
        wd = self.app.wd
        self.open_page_add_new_contact()
        self.fill_form(cont)
        self.click_to_create_contact()
        self.go_home()
        self.cont_cache = None

    def del_first(self):
        self.del_by_index(0)

    def del_by_index(self, index):
        wd = self.app.wd
        #open home page
        self.go_home()
        #click on check-box
        wd.find_elements_by_name("selected[]")[index].click()
        #click on delete
        wd.find_element_by_xpath("//input[@onclick='DeleteSel()']").click()
        # wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        #click to agree
        wd.switch_to_alert().accept()
        self.go_home()
        self.cont_cache = None

    def edit_first(self, new_contact_data):
        self.edit_by_index(0, new_contact_data)

    def edit_by_index(self, index, new_contact_data):
        wd = self.app.wd
        #open home page
        self.go_home()
        #click to edit
        wd.find_element_by_xpath("//tr["+str(index+2)+"]/td[8]").click()
        # wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
        # changed
        self.fill_form(new_contact_data)
        #click to finish
        wd.find_element_by_name("update").click()
        #return to home page
        self.go_home()
        self.cont_cache = None
        self.view_by_index(index)

    def click_to_create_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_page_add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def count(self):
        wd = self.app.wd
        #open home page
        self.go_home()
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

    def go_home(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_xpath("//input[@onclick='MailSelection()']")) > 0):
            wd.find_element_by_link_text("home").click()

    cont_cache = None

    def get_list(self):
        wd = self.app.wd
        if self.cont_cache is None:
            self.go_home()
            self.cont_cache = []
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                lastN = element.find_element_by_xpath("td[2]").text
                firsN = element.find_element_by_xpath("td[3]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.cont_cache.append(Contact(las=lastN, fir=firsN, id=id))
        # for element in wd.find_elements_by_name("entry"):
        #     lastN = wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[2]")
        #     firsN = wd.find_element_by_xpath("/td[3]")
        #     id = element.find_element_by_name("selected[]").get_attribute("value")
        #     listC.append(Contact(las=lastN, fir=firsN, id=id))
        return list(self.cont_cache)

    def view_by_index(self, index):
        wd = self.app.wd
        #open home page
        self.go_home()
        #click to view details
        # wd.find_element_by_xpath("//tr["+str(index+2)+"]/td[7]").click()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

