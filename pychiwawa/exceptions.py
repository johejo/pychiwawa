import json


class ChiwawaResponseError(Exception):
    def __init__(self, error_resp):
        super().__init__()
        self.error_resp = error_resp

    def __str__(self):
        return json.dumps(self.error_resp, indent=4)
