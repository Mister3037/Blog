from django.db import models
from django.contrib.auth.models import User

class Muallif(models.Model):
    ism = models.CharField(max_length=100)
    yosh = models.IntegerField()
    kasb = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.ism

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=100)
    sana = models.DateField()
    mavzu = models.CharField(max_length=100)
    matn = models.TextField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)
    def __str__(self):
        return f"Maqola sarlavhasi -> {self.sarlavha}\n Kim tomonidan - {self.muallif} \n" \
               f"To'liq ma'lumot -> {self.matn}"
