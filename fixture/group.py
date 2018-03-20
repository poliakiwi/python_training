
class GroupHelper:

    def __init__(self, app):
        self.app = app

    # def return_to_groups_page(self):
    #     wd = self.app.wd
    #     wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups()
        # init gpoup
        wd.find_element_by_name("new").click()
        # fill form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group
        wd.find_element_by_name("submit").click()
        self.open_groups()

    def open_groups(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def del_first(self):
        wd = self.app.wd
        self.open_groups()
        #click on check-box
        wd.find_element_by_name("selected[]").click()
        #click on delete
        wd.find_element_by_name("delete").click()
        self.open_groups()

    def edit_first(self):
        wd = self.app.wd
        self.open_groups()
        #click on check-box
        wd.find_element_by_name("selected[]").click()
        #click to edit
        wd.find_element_by_name("edit").click()
        # changed name
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("changed name")
        #click to finish
        wd.find_element_by_name("update").click()
        self.open_groups()