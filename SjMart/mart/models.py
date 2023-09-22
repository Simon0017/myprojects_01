from django.db import models

class Acquisition(models.Model):
    brand_id = models.AutoField(primary_key=True)
    name = models.ForeignKey("name",on_delete=models.CASCADE,null=True)
    distr = models.ForeignKey('suppliers',null=True,on_delete=models.CASCADE)
    brand = models.CharField(max_length=45, null=True)
    price = models.IntegerField(null=True)
    quantity = models.IntegerField(null = True)
    


    def __str__(self):
        return self.brand 

class staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=255,null=True)
    job_cat = models.ForeignKey("job_categories",on_delete=models.CASCADE)
    email = models.EmailField(max_length=255,unique=True)
    phone_no = models.IntegerField()
    
    def __str__(self):
        return self.first_name


class job_categories(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=255)

    def __str__(self):
        return self.cat_name

class shifts(models.Model):
    period = models.CharField(max_length=255)
    
    def __str__(self):
        return self.period
    

class suppliers(models.Model):
    supp_id = models.AutoField(primary_key=True)
    supp_name = models.CharField(max_length=30)
    email = models.EmailField()
    cell_one=models.CharField(max_length=20)
    cell_two=models.CharField(max_length=20)

    def __str__(self):
        return self.supp_name
    
    
class name(models.Model):
    name = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.name

class staff_in_shift(models.Model):
    shift=models.ForeignKey("shifts",on_delete=models.CASCADE,null=True)
    name=models.ForeignKey("staff",on_delete=models.CASCADE,null=True)
    Report_status=models.CharField(max_length=20)
    comments = models.CharField(max_length=100,null=True)

    # def __str__(self):
    #     return self.name