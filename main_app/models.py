from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse

# Create your models here.
STYLES = (
    ('C', 'Combo'),
    ('S', 'Stack')
)

class Amp(models.Model):
    brand = models.CharField(max_length=50)
    amp_model = models.CharField(max_length=50)
    style = models.CharField(
        'Stack or Combo',
        max_length=1,
        choices=STYLES,
        default=STYLES[0][0]
    )
    def get_absolute_url(self):
        return reverse("amps_detail", kwargs={"pk": self.id})

class Guitar(models.Model):
    brand = models.CharField(max_length=100)
    gtrmodel = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=100)

    amps = models.ManyToManyField(Amp)

    def __str__(self):
        return self.gtrmodel
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"guitar_id": self.id})
    
class Modification(models.Model):
    mod = models.CharField(max_length=100)
    brand = models.CharField(max_length=50, default='stock')
    mod_model = models.CharField(max_length=100, default='N/A')
    
    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)

    def __str__(self):
        return self.mod
    
    