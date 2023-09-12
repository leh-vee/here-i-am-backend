from django.contrib.gis.db import models
from django.db.models import Case, Value, When

class StreetEdge(models.Model):
    description = models.CharField()
    from_street_node_id = models.IntegerField()
    to_street_node_id = models.IntegerField()
    geom = models.LineStringField()

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'street_edge'

class StreetNodeQuerySet(models.QuerySet):
    def ordered_by_ids(self, ids):
        when_clauses = []
        for i, id in enumerate(ids):
            when_clauses.append(When(id=id, then=Value(i)))

        order_statement = Case(*when_clauses)

        return self.filter(id__in=ids).alias(order=order_statement).order_by("order")

class StreetNode(models.Model):
    geom = models.PointField()
    n_street_edges = models.IntegerField()

    class Meta:
        db_table = 'street_node'

    objects = StreetNodeQuerySet.as_manager()