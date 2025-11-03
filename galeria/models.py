from django.db import models
from datetime import datetime
# Create your models here.
CHOICES = [
    ("NEBULOSA", "Nebulosa"),
    ("ESTRELA", "Estrela"),
    ("GALAXIA", "Galáxia"),
    ("PLANETA", "Planeta")
]

class Fotografia(models.Model):
    nome = models.CharField(max_length = 100, null = False, blank = False)
    legenda = models.CharField(max_length = 155, null=False, blank=False)
    categoria = models.CharField(max_length=155, choices=CHOICES, default="")
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.nome
