from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class BookAd(models.Model):
    class AdStatus(models.TextChoices):
        PENDING = "PENDING",
        ACCEPTED = "ACCEPTED",
        REJECTED = "REJECTED",

        @classmethod
        def choices(cls):
            print(tuple((i.name, i.value) for i in cls))
            return tuple((i.name, i.value) for i in cls)

    owner = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)
    poster = models.ImageField("تصویر", upload_to='ad_posters/', null=True, blank=True)
    title = models.CharField("نام کتاب", max_length=30)
    author = models.CharField("نام نویسنده", max_length=30)
    description = models.TextField("توضیحات", max_length=500)
    sell = models.BooleanField("فروشی")
    suggested_money = models.IntegerField(default=0, null=False)
    status = models.CharField(max_length=255, choices=AdStatus.choices, verbose_name='status', default=AdStatus.PENDING)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('BookAdvertisement:ad', kwargs={'pk': self.pk})

    def clean(self):
        if self.poster and not self.sell:
            raise ValidationError("posters are not allowed for buy advertisements")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(BookAd, self).save(*args, **kwargs)
