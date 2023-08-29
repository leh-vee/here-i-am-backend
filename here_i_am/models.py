from django.contrib.gis.db import models

class Intersection(models.Model):
    description = models.CharField()
    classification = models.CharField()
    geom = models.PointField()

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'intersection'

class StreetSegment(models.Model):
    description = models.CharField()
    from_intersection = models.ForeignKey(Intersection, on_delete=models.PROTECT, related_name='street_segments_from', null=True)
    to_intersection = models.ForeignKey(Intersection, on_delete=models.PROTECT, related_name='street_segments_to', null=True)
    geom = models.MultiLineStringField()

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'street_segment'