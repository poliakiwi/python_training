# -*- coding: utf-8 -*-
import pytest
from contacts import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.fill_contact(Contact(fir="fir1", mid="mid1", las="las1", nic="nic1", tit="tit1", com="com1", add_1="add1",
                 tel_1="111", tel_2="222", tel_3="333", tel_4="444", mail_1="a1@a.ru", mail_2="a2@a.ru",
                 mail_3="a3@a.ru", hom="hom1.ru", add_2="add2", hom_2="hom2", not_2="not2"))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.fill_contact(Contact(fir="", mid="", las="", nic="", tit="", com="", add_1="",
                 tel_1="", tel_2="", tel_3="", tel_4="", mail_1="", mail_2="",
                 mail_3="", hom="", add_2="", hom_2="", not_2=""))
    app.logout()


