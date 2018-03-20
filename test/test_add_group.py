# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.groups.create(Group(name="grup1", header="h1", footer="f1"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.groups.create(Group(name="", header="", footer=""))
    app.session.logout()


