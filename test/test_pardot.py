import random
import unittest

from libsaas.executors import test_executor
from libsaas.services.pardot.service import Pardot


class PardotTestCase(unittest.TestCase):

    def setUp(self):
        self.executor = test_executor.use()
        self.executor.set_response(b'{}', 200, {})

        self.service = Pardot(api_key_or_email='api_key',
                              user_key='user_key')

    def expect(self, method=None, uri=None, params=None):
        if method:
            self.assertEqual(method, self.executor.request.method)
        if uri:
            self.assertEqual(self.executor.request.uri,
                              'https://pi.pardot.com/api' + uri)
        if params:
            self.assertEqual(self.executor.request.params, params)

    def test_auth(self):
        self.service.prospects().get()
        params = {'api_key': 'api_key',
                  'user_key': 'user_key',
                  'format': 'json'}
        self.expect('POST', '/prospect/version/3/do/query', params)

        service = Pardot('email@test.com', 'user_key', 'password')
        params = {'email': 'email@test.com',
                  'user_key': 'user_key',
                  'password': 'password',
                  'format': 'json'}
        service.prospects().get()
        self.expect('POST', '/prospect/version/3/do/query', params)

    def test_update_prospects(self):
        prospect_id = random.randint(3, 100)
        data = {'name': 'Test'}
        params = {'api_key': 'api_key',
                  'user_key': 'user_key',
                  'format': 'json',
                  'id': prospect_id}
        params.update(data)

        self.service.prospect().update(id=prospect_id, data=data)
        self.expect('POST', '/prospect/version/3/do/update', params)
