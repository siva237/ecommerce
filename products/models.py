from django.db import models

# Create your models here.
Return_policy_fields = (('YES','Y'),
                        ('NO','N'))
class Stores(models.Model):

    name = models.CharField(max_length=30,primary_key='True')
    address = models.TextField(max_length=50)
    contact_no = models.BigIntegerField()
    landmark = models.CharField(max_length=30)
    email = models.EmailField()
    location = models.CharField(max_length=30)

    def __str__(self):
        return "-".join([self.name,self.location])


class Products(models.Model):
    store_id = models.ForeignKey(Stores, related_name='store_prod', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    # price = models.FloatField()
    quantity = models.IntegerField()
    # category = models.CharField(max_length=50, choices=CATEGORY, default='EL')
    exp_date = models.DateField()
    reviews = models.CharField(max_length=255)
    ratings = models.CharField(max_length=10)
    return_policy = models.CharField(max_length=5, choices=Return_policy_fields, default='Y')

    def __str__(self):
        return '-'.join([self.store_id.name, self.store_id.location])