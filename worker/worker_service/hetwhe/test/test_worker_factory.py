from worker.wsgi import *
from worker.worker_service.hetwhe.models import Worker
from worker.worker_service.hetwhe.models import Project


class TestWorkerFactory:
    def __init__(self):
        Project.objects.all().delete()
        Worker.objects.all().delete()  # Чтобы удалить данные с теста
        self.worker1 = Worker.objects.create(first_name="Olga", second_name="Byrania", age=30, man=False)
        self.worker2 = Worker.objects.create(first_name="Kolyan", second_name="Bolgow", age=140, man=True)
        self.worker3 = Worker.objects.create(first_name="Dodick", second_name="Dick", age=11, man=False)
