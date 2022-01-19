from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from project.managers.score_manager import ScoreManager


class persons(models.Model):
    recorder = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10)
    email = models.EmailField()

    class Meta:
        unique_together = ['email']
        verbose_name = 'person'
        verbose_name_plural = 'persons'

    def __str__(self):
        return f'{self.recorder}'


class sites(models.Model):

    daterecord = models.DateField(auto_now=False, auto_now_add=False)
    schedule = models.DateTimeField()
    ubicacion = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=10)
    site = models.CharField(max_length=20)

    class Meta:
        unique_together = ['site']
        verbose_name = 'site'
        verbose_name_plural = 'sites'

    def __str__(self):
        return u'sites#%s' % self.id


class score(models.Model):
    recorder = models.ForeignKey(to='project.persons', on_delete=models.CASCADE, related_name='+')
    score = models.FloatField(default='0.0')

    site = models.ForeignKey(to='project.sites', on_delete=models.CASCADE, related_name='+')
    objects = ScoreManager()

    class Meta:
        unique_together = [['site', 'recorder']]
        verbose_name = 'score'
        verbose_name_plural = 'scores'

    def __str__(self):
        return f'{self.id}'


@receiver(post_save, sender=score)
def range(sender, instance, **kwargs):
    aux = 0.0
    scores = score.objects.filter(id=instance.place.recorder).first()
    site = sites.objects.filter(place_id=instance.place.recorder)

    for i in scores:
        print(scores)
    # Create your models here.
