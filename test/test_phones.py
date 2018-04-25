import re


def test_phones_on_home(app):
    contact_from_home = app.contacts.get_list()[0]
    contact_from_edit = app.contacts.get_info_from_edit(0)
    assert contact_from_home.all_tel_from_home == merge_tel(contact_from_edit)


# def test_phones_on_view(app):
#     contact_from_view = app.contacts.get_info_from_view(0)
#     contact_from_edit = app.contacts.get_info_from_edit(0)
#     assert contact_from_view.tel_1 == contact_from_edit.tel_1
#     assert contact_from_view.tel_2 == contact_from_edit.tel_2
#     assert contact_from_view.tel_3 == contact_from_edit.tel_3
#     assert contact_from_view.hom_2 == contact_from_edit.hom_2


def clear(s):
    return re.sub("[() -]", "", s)


def merge_tel(cont):
    return clear("\n".join(filter(lambda x: x != "", [cont.tel_1, cont.tel_2, cont.tel_3, cont.hom_2])))
