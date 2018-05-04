from sys import maxsize

class Contact:
    def __init__(self, fir=None, mid=None, las=None, nic=None, tit=None, com=None, add_1=None, tel_1=None,
                     tel_2=None, tel_3=None, tel_4=None, mail_1=None, mail_2=None, mail_3=None, hom=None, add_2=None,
                     hom_2=None, not_2=None, id=None, all_tel_from_home=None, all_mail_from_home=None):
        self.fir = fir
        self.mid = mid
        self.las = las
        self.nic = nic
        self.tit = tit
        self.com = com
        self.add_1 = add_1
        self.tel_1 = tel_1
        self.tel_2 = tel_2
        self.tel_3 = tel_3
        self.tel_4 = tel_4
        self.mail_1 = mail_1
        self.mail_2 = mail_2
        self.mail_3 = mail_3
        self.hom = hom
        self.add_2 = add_2
        self.hom_2 = hom_2
        self.not_2 = not_2
        self.id = id
        self.all_tel_from_home = all_tel_from_home
        self.all_mail_from_home = all_mail_from_home

    def __repr__(self):
        return "%s:%s,%s,%s" % (self.id, self.las, self.fir, self.add_1)

    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) and self.las == other.las and self.fir == other.fir and self.add_1 == other.add_1

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
