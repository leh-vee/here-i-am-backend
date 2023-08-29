from django.contrib.gis.db import models

class Intersection(models.Model):
    description = models.CharField()
    classification = models.CharField()
    geom = models.PointField()

    def __str__(self):
      return self.description

    class Meta:
      db_table = 'intersection'