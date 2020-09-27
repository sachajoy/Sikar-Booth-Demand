from django.db import models


class Contractor(models.Model):
    xname = models.CharField(max_length=64)

    class Meta:
        db_table = 'contractor'

    def __str__(self):
        return self.xname


class Route(models.Model):
    route_no = models.SmallIntegerField(default=0)
    xname = models.CharField(max_length=40)
    contractor_id = models.ForeignKey(Contractor,
                                      on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'route'

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

    class Meta:
        db_table = 'booth'

    def __str__(self):
        return "{} {} {}".format(self.booth_no,
                                 self.xname,
                                 self.route_no)


class ItemGroup(models.Model):
    xname = models.CharField(max_length=32, default='')
    itype = models.CharField(max_length=1, default='')

    class Meta:
        db_table = 'itemgroup'

    def __str__(self):
        return self.xname


class ItemMST(models.Model):
    xname = models.CharField(max_length=32, default='')
    shortname = models.CharField(max_length=8, default='')
    itemgroup_id = models.ForeignKey(ItemGroup,
                                     on_delete=models.CASCADE)
    itype = models.CharField(max_length=1, default='')
    unit = models.CharField(max_length=8, default='')
    packingtype = models.CharField(max_length=8, default='')
    sale_unit = models.CharField(max_length=8, default='')
    qty_fill = models.DecimalField(max_digits=15, decimal_places=3)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'itemmst'

    def __str__(self):
        return self.shortname


class Shift(models.Model):
    t_from = models.SmallIntegerField(default=0)
    t_upto = models.SmallIntegerField(default=0)
    shift = models.CharField(max_length=1, default='')

    class Meta:
        db_table = 'shift'

    def __str__(self):
        return self.shift



class Tran(models.Model):
    xdatetime = models.DateTimeField(default='0100-01-01 00:00:00')
    xdate = models.DateField(default='0100-01-01')
    shift = models.CharField(max_length=1)
    booth_no = models.ForeignKey(Booth, on_delete=models.CASCADE)
    booth_name = models.CharField(max_length=64, default='')
    route_no = models.ForeignKey(Route, on_delete=models.CASCADE)
    contractor_id = models.ForeignKey(Contractor, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tran'

    def __str__(self):
        return "{} {} {}".format(self.shift,
                                 self.xdate,
                                 self.booth_no)


class TranDet(models.Model):
    tran_id = models.ForeignKey(Tran, on_delete=models.CASCADE)
    xdate = models.DateField(default='0100-01-01')
    shift = models.CharField(max_length=1)
    booth_no = models.ForeignKey(Booth, on_delete=models.CASCADE)
    sno = models.SmallIntegerField(default=0)
    item_id = models.ForeignKey(ItemMST, on_delete=models.CASCADE)
    shortname = models.CharField(max_length=8, default='')
    unit = models.CharField(max_length=8, default='')
    packingtype = models.CharField(max_length=8, default='')
    sale_unit = models.CharField(max_length=8, default='')
    quantity = models.SmallIntegerField(default=0)

    class Meta:
        db_table = 'trandet'

