from worker.wsgi import *
from django.test import TestCase

from test_worker_factory import TestWorkerFactory
from worker.worker_service.hetwhe.models import Worker
from worker.worker_service import worker_service


class TestService(TestCase):
    def setUp(self):
        self.test_structure = TestWorkerFactory()  # Создает объекты класса

    def test_get_object(self):
        result = worker_service.get_all({})
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].first_name, self.test_structure.worker1.first_name)

    def test_delete_object(self):
        before = Worker.objects.count()
        worker_service.delete_id(str(self.test_structure.worker3.id))
        after = Worker.objects.count()
        self.assertEqual(before, after + 1)

    def test_update_objects(self):
        dict = {'id':str(self.test_structure.worker3.id),
                'first_name':'Kostya_the_king',
                'age':666}

        worker_service.update(dict)
        self.assertEqual(Worker.objects.get(id=str(self.test_structure.worker3.id)).first_name, 'Kostya_the_king')
        self.assertEqual(self.test_structure.worker3.second_name, 'Dick')

    def test_create_object(self):
        dict = {'first_name': 'Kostya_the_king',
                'second_name': 'Phase',
                'age': 666,
                'man': True}

        count = Worker.objects.count()
        worker_service.create(dict)
        before = Worker.objects.count()

        phase = Worker.objects.get(second_name='Phase')
        self.assertEqual(phase.first_name, dict['first_name'])
        self.assertEqual(phase.second_name, dict['second_name'])
        self.assertEqual(phase.age, dict['age'])
        self.assertEqual(phase.man, dict['man'])
        self.assertEqual(count, before - 1)
