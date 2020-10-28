from django.db import models


class DodatkoweInfo(models.Model):
    GATUNEK = {
        (0, 'Inne'),
        (1, 'Horror'),
        (2, 'Komedia'),
        (3, 'Sci-fi'),
        (4, 'Dramat'),
    }
    czas_trwania = models.PositiveSmallIntegerField(default=0)
    gatunek = models.PositiveSmallIntegerField(default=0, choices=GATUNEK)


class Film(models.Model):
    tytul = models.CharField(max_length=64, blank=False, unique=True, default="")
    rok = models.PositiveSmallIntegerField(default=2000)
    opis = models.TextField(default="")
    premiera = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    plakat = models.ImageField(upload_to="plakaty", null=True, blank=True)
    # One To One relation ☀☀☀☀☀
    dodatkowe = models.OneToOneField(DodatkoweInfo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.tytul_z_rokiem()

    def tytul_z_rokiem(self):
        return f"{self.tytul} ({self.rok})"

    def delete(self, *args, **kwargs):
        self.plakat.delete()
        super().delete(*args, **kwargs)


class Ocena(models.Model):
    recenzja = models.TextField(default="", blank=True)
    gwiazdki = models.PositiveSmallIntegerField(default=5)
    # Many to One
    film = models.ForeignKey(Film, on_delete=models.CASCADE)


class Aktor(models.Model):
    imie = models.CharField(max_length=32)
    nazwisko = models.CharField(max_length=32)
    # ManyToMany
    filmy = models.ManyToManyField(Film)
