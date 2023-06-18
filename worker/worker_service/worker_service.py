from django.http import HttpResponse
from worker.worker_service.hetwhe.models import Worker


def get_all(worker: dict):
    if not worker:
        data = Worker.objects.all()
    else:
        data = Worker.objects.filter(**worker)
    return data


def delete_id(id: str):
    Worker.objects.filter(id=id).delete()


def update(worker: dict):
    return Worker.objects.filter(id=worker['id']).update(**worker)


def create(worker: dict):
    Worker.objects.create(**worker)


