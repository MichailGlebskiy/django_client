from worker.Models.models import Project


def create(project: dict):
    return Project.objects.create(**project)


def delete(project_id):
    Project.objects.filter(id=project_id).delete()


def update(project: dict):
    Project.objects.filter(id=project['id']).update(**project)


def get(project: dict):
    if not project:
        return Project.objects.all()
    else:
        return Project.objects, filter(**project)
