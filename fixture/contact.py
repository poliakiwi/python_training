from model.contacts import Contact
import re

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
        # wd.find_element_by_xpath("//tr["+str(index+2)+"]/td[8]").click()
        self.open_edit_by_index(index)
        # changed
        self.fill_form(new_contact_data)
        #click to finish
        wd.find_element_by_name("update").click()
        #return to home page
        self.go_home()
        self.cont_cache = None
        # self.view_by_index(index)

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
                las = element.find_element_by_xpath("td[2]").text
                fir = element.find_element_by_xpath("td[3]").text
                add_1 = element.find_element_by_xpath("td[4]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_mail = element.find_element_by_xpath("td[5]").text
                all_tel = element.find_element_by_xpath("td[6]").text
                self.cont_cache.append(Contact(las=las, fir=fir, id=id, add_1=add_1, all_mail_from_home=all_mail, all_tel_from_home=all_tel))
        return list(self.cont_cache)

    def open_edit_by_index(self, index):
        wd = self.app.wd
        #open home page
        self.go_home()
        #click to edit
        # wd.find_element_by_xpath("//tr["+str(index+2)+"]/td[8]").click()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def view_by_index(self, index):
        wd = self.app.wd
        #open home page
        self.go_home()
        #click to view details
        # wd.find_element_by_xpath("//tr["+str(index+2)+"]/td[7]").click()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_info_from_edit(self, index):
        wd = self.app.wd
        #open home page
        self.go_home()
        #click to edit
        self.open_edit_by_index(index)
        fir = wd.find_element_by_name("firstname").get_attribute("value")
        las = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        tel_1 = wd.find_element_by_name("home").get_attribute("value")
        tel_2 = wd.find_element_by_name("mobile").get_attribute("value")
        tel_3 = wd.find_element_by_name("work").get_attribute("value")
        hom_2 = wd.find_element_by_name("phone2").get_attribute("value")
        add_1 = wd.find_element_by_name("address").get_attribute("value")
        mail_1 = wd.find_element_by_name("email").get_attribute("value")
        mail_2 = wd.find_element_by_name("email2").get_attribute("value")
        mail_3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(las=las, fir=fir, id=id, tel_1=tel_1, tel_2=tel_2, tel_3=tel_3, hom_2=hom_2, add_1=add_1,
                       mail_1=mail_1, mail_2=mail_2, mail_3=mail_3)

    def get_info_from_view(self, index):
        wd = self.app.wd
        #open home page
        self.go_home()
        #click to edit
        self.view_by_index(index)
        text = wd.find_element_by_id("content").text
        tel_1 = re.search("H: (.*)", text).group(1)
        tel_2 = re.search("M: (.*)", text).group(1)
        tel_3 = re.search("W: (.*)", text).group(1)
        hom_2 = re.search("P: (.*)", text).group(1)
        return Contact(tel_1=tel_1, tel_2=tel_2, tel_3=tel_3, hom_2=hom_2)


