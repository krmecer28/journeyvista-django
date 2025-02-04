from django.db import models

class Tour(models.Model):
    name = models.CharField(max_length=255)  # Tur adı
    start_date = models.DateField()  # Başlangıç tarihi
    end_date = models.DateField()  # Bitiş tarihi
    guide = models.CharField(max_length=255)  # Rehber adı
    image = models.ImageField(upload_to='tours/')  # Tur görseli

    def __str__(self):
        return self.name

class DailyCity(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="days")  # İlgili Tur
    day_number = models.PositiveIntegerField()  # Gün Numarası
    city = models.CharField(max_length=255)  # Şehir Adı
    description = models.TextField()  # Günlük Açıklama

    def __str__(self):
        return f"{self.tour.name} - Gün {self.day_number}"

class City(models.Model):
    name = models.CharField(max_length=255)  # Şehir adı
    latitude = models.FloatField()  # Enlem
    longitude = models.FloatField()  # Boylam

    def __str__(self):
        return self.name