# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string
import re


def random_str(prefix, maxlen):
    sym = string.ascii_letters + string.digits + " "*10 #+ string.punctuation
    return prefix + "".join([random.choice(sym) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_str("NN",10), header=random_str("HH",20), footer=random_str("FF",20))
    for i in range(5)
]


@pytest.mark.parametrize("gr", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, gr):
    old_groups = app.groups.get_groups_list()
    app.groups.create(gr)
    new_groups = app.groups.get_groups_list()
    assert len(old_groups) + 1 == len(new_groups)
    gr.name = clear_blank(gr.name)
    old_groups.append(gr)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def clear_blank(s):
    s1 = re.sub(" +", " ", s)
    s1 = re.sub(" $", "", s1)
    return s1
