from worker.Models.models import Worker


def get_all(worker: dict):
    if not worker:
        return Worker.objects.all()
    else:
        return Worker.objects.filter(**worker)


def delete_id(id: str):
    Worker.objects.filter(id=id).delete()


def update(worker: dict):
    return Worker.objects.filter(id=worker['id']).update(**worker)


def create(worker: dict):
    Worker.objects.create(**worker)


