from django.http import HttpResponse
from worker.worker_service import worker_service
from worker.worker_service.Logger import Logger, LoggerMethod


def index(request):
    return HttpResponse("its work")


def get(request):
    worker = request.GET.dict()
    return HttpResponse(worker_service.get_all(worker))


@Logger(LoggerMethod.UPDATE, "update database")
def update(request):
    worker = request.GET.dict()
    return HttpResponse(str(worker_service.update(worker)))


@Logger(LoggerMethod.DELETE, "delete worker")
def delete(request):
    id = request.GET.dict()
    worker_service.delete_id(id[id])
    return HttpResponse("Worker deleted")


# @Logger(LoggerMethod.CREATE, "Added worker")
def create(request):
    worker = request.GET.dict()
    worker_service.create(worker)
    return HttpResponse("Created", str(worker))

