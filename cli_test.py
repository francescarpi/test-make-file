#!/usr/bin/python3
import json
import sys
import time


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

    def test_action_6(self):
        sys.stdout.write("Stdout 1: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n\n")
        sys.stdout.flush()
        time.sleep(2)
        sys.stdout.write("Stdout 2: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n\n")
        sys.stdout.flush()
        time.sleep(2)
        sys.stderr.write("Stderr 1: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n\n")
        sys.stderr.flush()
        time.sleep(2)
        sys.stderr.write("Stderr 2: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n\n")
        sys.stderr.flush()

        return 'Finish'


if __name__ == '__main__':
    action = sys.argv[1]

    try:
        json_raw = sys.argv[2]
    except IndexError:
        json_raw = None

    client = Client(action, json_raw)
    print(client.run())
