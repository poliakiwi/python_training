from model.group import Group
import re
from timeit import timeit

def test_group_list(app, db):
    ui_list = app.groups.get_groups_list()
    def clean(group):
        group.name = re.sub(" +", " ", group.name)
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

# def clear_blank(s):
#     s1 = re.sub(" +", " ", s)
#     s1 = re.sub(" $", "", s1)
#     return s1