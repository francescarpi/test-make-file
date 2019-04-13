#!/usr/bin/python3
import json
import sys


class Client:

    def __init__(self, action: str, json_raw: str):
        self._action = action
        self._json = None

        if json_raw:
            self._json = json.loads(json_raw)

    def run(self):
        method = getattr(self, self._action)
        return method()

    def test_action_1(self):
        response = {'output': {'key': self._json['common']['organization_slug']}}
        return json.dumps(response)

    def test_action_2(self):
        return json.dumps(self._json)

    def test_action_3(self):
        response = {'key_action_3': 'value_action_3'}
        return json.dumps(response)

    def test_action_4(self):
        return 'action 4 result'

    def test_action_5(self):
        response = {'status': 'success_at_retry_{}'.format(self._json['common']['retries'])}
        return json.dumps(response)


if __name__ == '__main__':
    action = sys.argv[1]

    try:
        json_raw = sys.argv[2]
    except IndexError:
        json_raw = None

    client = Client(action, json_raw)
    print(client.run())
