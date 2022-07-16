from django.db import models
import django_filters


# Create your models here.
class sign_up(models.Model):
    name = models.CharField(verbose_name='Username', max_length=100)
    password = models.CharField(verbose_name='Password', max_length=60)
    email = models.EmailField(verbose_name='Email', max_length=60)

    class Meta:
        verbose_name = 'Sign Up'
        verbose_name_plural = 'Sign Up'
        db_table = 'sign_up'

    def __str__(self):
        return "%s" % (self.email)

# for filtering out in admin section
class SignUpFilter(django_filters.FilterSet):
    class Meta:
        model = sign_up
        fields = ['email', 'name']

# class Upload_File(models.Model):
#     existingPath = models.CharField(max_length=100)
#     name = models.CharField(max_length=50)
#     eof = models.BooleanField()
#
#     def __str__(self):
#         return "%s" % (self.name)

