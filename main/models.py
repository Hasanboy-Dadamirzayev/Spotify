from django.db import models

class Singer(models.Model):
    name = models.CharField(max_length=255)
    birthdate = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Songs(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255, null=True, blank=True)
    duration = models.DurationField()
    file = models.FileField(upload_to='files/', blank=True, null=True)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

