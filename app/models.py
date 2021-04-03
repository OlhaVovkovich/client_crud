from django.db import models
from django.urls import reverse


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    date_of_birth = models.DateField()

    @property
    def zodiac(self):
        month = self.date_of_birth.month
        day = self.date_of_birth.day

        if month == 12:
            astro_sign = 'Sagittarius, \u2650' if (day < 22) else 'Capricorn, \u2651'
        elif month == 1:
            astro_sign = 'Capricorn, \u2651' if (day < 20) else 'Aquarius, \u2652'
        elif month == 2:
            astro_sign = 'Aquarius, \u2652' if (day < 19) else 'Pisces, \u2653'
        elif month == 3:
            astro_sign = 'Pisces, \u2653' if (day < 21) else 'Aries, \u2648'
        elif month == 4:
            astro_sign = 'Aries, \u2648' if (day < 20) else 'Taurus, \u2649'
        elif month == 5:
            astro_sign = 'Taurus, \u2649' if (day < 21) else 'Gemini, \u264A'
        elif month == 6:
            astro_sign = 'Gemini, \u264A' if (day < 21) else 'Cancer, \u264B'
        elif month == 7:
            astro_sign = 'Cancer, \u264B' if (day < 23) else 'Leo, \u264C'
        elif month == 8:
            astro_sign = 'Leo, \u264C' if (day < 23) else 'Virgo, \u264D'
        elif month == 9:
            astro_sign = 'Virgo, \u264D' if (day < 23) else 'libra, \u264E'
        elif month == 10:
            astro_sign = 'Libra, \u264E' if (day < 23) else 'Scorpio, \u264F'
        elif month == 11:
            astro_sign = 'Scorpio, \u264F' if (day < 22) else 'Sagittarius, \u2650'

        return astro_sign

    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'pk': self.pk})
