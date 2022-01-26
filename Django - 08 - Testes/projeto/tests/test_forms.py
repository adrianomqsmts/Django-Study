from django.test import TestCase

class YourTestClass(TestCase):
    def setUp(self):
        # O método é executada antes de cada método de teste.
        pass

    def tearDown(self):
        # O método é executado após cada método de teste.
        pass

    def test_algo_que_vai_passar(self):
        self.assertFalse(False)

    def test_algo_que_vai_falhar(self):
        self.assertTrue(False)