from django.db import models


class ScoreManager(models.Manager):
    def filtrador(self, id):
        return self.filter(recorder_id=id)