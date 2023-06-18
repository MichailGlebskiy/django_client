import uuid

from django.db import models


class Worker(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    age = models.IntegerField()
    man = models.BooleanField()

    objects = models.Manager()

    def __str__(self):
        return str(self.id) + " " + str(self.first_name) + " " + str(self.second_name) + " " + str(self.man)

    class Meta:
        app_label = 'worker.Models.models.'
        db_table = "test\".\"worker"


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, db_column='worker')

    project_name = models.CharField(db_column="workers_project", max_length=200)
    salary = models.IntegerField(null=False)

    class Meta:
        app_label = 'worker.Models.models.'
        db_table = "test\".\"projects"


class Log(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    project_id = models.ForeignKey('Project', on_delete=models.DO_NOTHING, db_column='project_id')
    action_type = models.CharField(max_length=15)
    time = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'worker.Models.models'
        db_table = "test\".\"log"