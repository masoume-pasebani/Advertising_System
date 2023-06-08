from collections import OrderedDict

from django.db import models

# Create your models here.


class Advertiser(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Ad(models.Model):
    Title = models.CharField(max_length=200)
    Img = models.ImageField(upload_to='img/', default='de.jpg')
    Link = models.URLField()
    Adv = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    # approve = models.BooleanField(default=True)

    def __str__(self):
        return self.Title

    def number_of_clicks(self):
        dict = {}
        for hour in range(0, 24):
            dict[str(hour) + "-" + str(hour+1)] = self.click_set.filter(ad__click__C_date__hour__range=(hour, hour+1)).count()
        return dict

    def number_of_views(self):
        dict = {}
        for hour in range(0, 24):
            dict[str(hour) + "-" + str(hour+1)] = self.view_set.filter(ad__view__V_date__hour__range=(hour, hour+1)).count()
        return dict

    def getAveViewAndClickTimeDif(self):

        sum = 0
        for click in self.click_set.all():
            time = click.C_date - \
                   self.view_set.filter(ip=click.ip).filter(V_date__lt=click.C_date)[0].V_date
            sum += time.seconds

        if self.click_set.exists():
            return sum / self.click_set.count()
        else:
            return "we have no clicks on this ad"


class Click(models.Model):
    C_date = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField(default='000.000.0.0')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    def __str__(self):
        return self.ad.Title+" clicked by "+self.ip


class View(models.Model):
    V_date = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField(default='000.000.0.0')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    def __str__(self):
        return self.ad.Title+" viewed by "+self.ip



