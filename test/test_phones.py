import re
from random import randrange
from model.contacts import Contact


def test_phones_and_other_info_on_home(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contact(fir="Test"))
    cont_list = app.contacts.get_list()
    index = randrange(len(cont_list))
    contact_from_home = cont_list[index]
    contact_from_edit = app.contacts.get_info_from_edit(index)
    assert contact_from_home.all_tel_from_home == merge_tel(contact_from_edit)
    assert contact_from_home.fir == clear_blank(contact_from_edit.fir)
    assert contact_from_home.las == clear_blank(contact_from_edit.las)
    assert contact_from_home.add_1 == clear_blank(contact_from_edit.add_1)
    assert contact_from_home.all_mail_from_home == merge_mail(contact_from_edit)


# def test_phones_on_view(app):
#     contact_from_view = app.contacts.get_info_from_view(0)
#     contact_from_edit = app.contacts.get_info_from_edit(0)
#     assert contact_from_view.tel_1 == contact_from_edit.tel_1
#     assert contact_from_view.tel_2 == contact_from_edit.tel_2
#     assert contact_from_view.tel_3 == contact_from_edit.tel_3
#     assert contact_from_view.hom_2 == contact_from_edit.hom_2


def clear(s):
    return re.sub("[() -]", "", s)


def clear_blank(s):
    s1 = re.sub(" +", " ", s)
    s1 = re.sub(" $", "", s1)
    return s1


def merge_tel(cont):
    # return clear("\n".join(filter(lambda x: x != "", [cont.tel_1, cont.tel_2, cont.tel_3, cont.hom_2])))
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [cont.tel_1, cont.tel_2, cont.tel_3, cont.hom_2]))))


def merge_mail(cont):
    return "\n".join(filter(lambda x: x != "", [cont.mail_1, cont.mail_2, cont.mail_3]))
