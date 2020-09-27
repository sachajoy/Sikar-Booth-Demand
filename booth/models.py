from django.db import models


class Contractor(models.Model):
    xname = models.CharField(max_length=64)

    def __str__(self):
        return self.xname


class Route(models.Model):
    route_no = models.SmallIntegerField(default=0)
    xname = models.CharField(max_length=40)
    contractor_id = models.ForeignKey(Contractor,
                                      on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{} {}".format(self.route_no, self.xname)


class Booth(models.Model):
    booth_no = models.SmallIntegerField(default=0)
    route_no = models.ForeignKey(Route, on_delete=models.CASCADE)
    xname = models.CharField(max_length=64, default='')
    contractor_id = models.ForeignKey(Contractor,
                                             on_delete=models.CASCADE)
    add1 = models.CharField(max_length=32, default='')
    add2 = models.CharField(max_length=32, default='')
    add3 = models.CharField(max_length=32, default='')
    add4 = models.CharField(max_length=32, default='')
    mobile = models.CharField(max_length=11, default='')
    pan = models.CharField(max_length=32, default='')
    wef = models.DateField(default='0100-01-01')
    active = models.BooleanField(default=True)
    remarks = models.CharField(max_length=64, default='')
    uid = models.CharField(max_length=5, default='')
    upwd = models.CharField(max_length=64, default='')
    tran_next_id = models.BigIntegerField(default=0)
    _userdet = models.SmallIntegerField(default=0)
    auth_userdet = models.SmallIntegerField(default=0)

    def __str__(self):
        return "{} {} {}".format(self.booth_no, self.xname, self.route_no)
