from django.db import models


class DivisionLevel(models.IntegerChoices):
    LEVEL_1 = 1
    LEVEL_2 = 2
    LEVEL_3 = 3
    LEVEL_4 = 4
    LEVEL_5 = 5


class Division(models.Model):
    name = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField(choices=DivisionLevel.choices)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Division"


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Position"


class Employer(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    acceptance_date = models.DateTimeField(auto_now_add=True)
    salary = models.DecimalField(max_digits=9, decimal_places=2)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "Employer"
