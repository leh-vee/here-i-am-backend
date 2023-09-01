from django.contrib.gis.db import models
from django.db.models import Case, Value, When

class IntersectionQuerySet(models.QuerySet):
    def sefirot_ordered_by_intersection_id_index(self, intersection_ids):
        when_clauses = []
        for index, intersection_id in enumerate(intersection_ids):
            when_clauses.append(When(id=intersection_id, then=Value(index)))

        order_statement = Case(*when_clauses)

        return self.filter(id__in=intersection_ids).alias(order=order_statement).order_by("order")

class Intersection(models.Model):
    description = models.CharField()
    classification = models.CharField()
    geom = models.PointField()

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'intersection'

    objects = IntersectionQuerySet.as_manager()

class StreetSegment(models.Model):
    description = models.CharField()
    from_intersection = models.ForeignKey(Intersection, on_delete=models.PROTECT, related_name='street_segments_from', null=True)
    to_intersection = models.ForeignKey(Intersection, on_delete=models.PROTECT, related_name='street_segments_to', null=True)
    geom = models.MultiLineStringField()

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'street_segment'