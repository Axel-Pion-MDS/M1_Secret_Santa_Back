from django.db import models


# Create your models here.
class Member(models.Model):
    email = models.CharField(max_length=255)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    promo = models.ForeignKey('promotions.promotion', on_delete=models.CASCADE, null=False)
    role = models.ForeignKey('roles.role', on_delete=models.CASCADE, default=1, blank=True, null=True)

    def __str__(self):
        return '{} - {} {} {} {}'.format(self.pk, self.lastname, self.firstname, self.email, self.promo)
