from django.db import models
from django.forms.models import ModelForm

class Provider(models.Model):
    name = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='uploads/%Y/%m/%d')

    def __unicode__(self):
        return self.name

class ProviderForm(ModelForm):
    class Meta:
        model = Provider