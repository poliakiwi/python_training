from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.open_groups()
        # init gpoup
        wd.find_element_by_name("new").click()
        self.fill_form(group)
        # submit group
        wd.find_element_by_name("submit").click()
        self.open_groups()
        self.group_cache = None

    def del_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups()
        self.select_group_by_index(index)
        #click on delete
        wd.find_element_by_name("delete").click()
        self.open_groups()
        self.group_cache = None

    def del_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups()
        self.select_group_by_id(id)
        #click on delete
        wd.find_element_by_name("delete").click()
        self.open_groups()
        self.group_cache = None

    def del_first(self):
        self.del_group_by_index(0)

    def edit_first(self, new_group_data):
        self.edit_by_index(0, new_group_data)

    def edit_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups()
        self.select_group_by_index(index)
        #click to edit
        wd.find_element_by_name("edit").click()
        # change
        self.fill_form(new_group_data)
        #click to finish
        wd.find_element_by_name("update").click()
        self.open_groups()
        self.group_cache = None

    def edit_by_id(self, id, new_group_data):
        wd = self.app.wd
        self.open_groups()
        self.select_group_by_id(id)
        #click to edit
        wd.find_element_by_name("edit").click()
        # change
        self.fill_form(new_group_data)
        #click to finish
        wd.find_element_by_name("update").click()
        self.open_groups()
        self.group_cache = None

    def fill_form(self, group):
        wd = self.app.wd
        self.change_field("group_name", group.name)
        self.change_field("group_header", group.header)
        self.change_field("group_footer", group.footer)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_groups(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def select_first_group(self):
        self.select_group_by_index(0)

    def count(self):
        wd = self.app.wd
        self.open_groups()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_groups_list(self):
        wd = self.app.wd
        if self.group_cache is None:
            self.open_groups()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

