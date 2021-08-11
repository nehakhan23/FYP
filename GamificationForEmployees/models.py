from django.db import models


class Monthly(models.Model):
    id = models.AutoField(primary_key=True)
    e_no = models.CharField(max_length=20)
    e_name = models.CharField(max_length=20)
    grade = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    month = models.CharField(max_length=20)
    no_roaster_deviation = models.CharField(max_length=20)
    roaster_deviation = models.CharField(max_length=20)
    training_session = models.CharField(max_length=20)
    absent = models.CharField(max_length=20)
    offday = models.CharField(max_length=20)
    present = models.CharField(max_length=20)
    overtime_hours = models.CharField(max_length=20)
    safety_risk_rating = models.CharField(max_length=20)
    leaves = models.CharField(max_length=20)
    bonus= models.CharField(max_length=20,null=True)
    bonus_score= models.CharField(max_length=20,null=True)
    class Meta:
        db_table = 'monthly'

class Yearly(models.Model):
    id = models.AutoField(primary_key=True)
    e_no = models.CharField(max_length=20)
    e_name = models.CharField(max_length=20)
    grade = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    # month = models.CharField(max_length=20)
    no_roaster_deviation = models.CharField(max_length=20)
    roaster_deviation = models.CharField(max_length=20)
    training_session = models.CharField(max_length=20)
    absent = models.CharField(max_length=20)
    offday = models.CharField(max_length=20)
    present = models.CharField(max_length=20)
    overtime_hours = models.CharField(max_length=20)
    safety_risk_rating = models.CharField(max_length=20)
    leaves = models.CharField(max_length=20)
    class Meta:
        db_table = 'yearly'


class predResults(models.Model):
    id = models.AutoField(primary_key=True)
    e_no = models.CharField(max_length=20)
    month = models.CharField(max_length=20)
    grade = models.CharField(max_length=20)
    score = models.CharField(max_length=20)
    bonus_score = models.CharField(max_length=20)
    result = models.CharField(max_length=20)
    
    
    class Meta:
        db_table = 'prediction_results'

