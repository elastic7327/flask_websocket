from src.tests.base import BaseTestCase
from src.flaskr import app, socketio
import json


class TestBasicSocket(BaseTestCase):

    def test_connect(self):
        received = self.socket_client.get_received()

        self.assertEqual(len(received), 3)
        self.assertEqual(received[0]['args'], 'connected')
        self.assertEqual(received[1]['args'], '{}')
        self.assertEqual(received[2]['args'], '{}')

        res = self.socket_client.disconnect()
        assert res == None

    def test_connect_query_string_and_headers(self):
        client = socketio.test_client(
            app, query_string='?foo=bar&foo=baz',
            headers={'Authorization': 'Bearer foobar'}
        )

        received = client.get_received()
        self.assertEqual(len(received), 3)
        self.assertEqual(received[0]['args'], 'connected')
        self.assertEqual(received[1]['args'], '{"foo": ["bar", "baz"]}')
        self.assertEqual(received[2]['args'],
                         '{"Authorization": "Bearer foobar"}')

        client.disconnect()
