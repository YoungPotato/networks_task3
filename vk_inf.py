from handler import Handler


class Information:
    def __init__(self, user_id, requests):
        self.user_id = user_id
        self.requests = requests.split(',')
        self.token = self.read("token.txt")
        self.handler = Handler(self.token)

    def run(self):
        for request in self.requests:
            a = self.handler.requests_handler(request, self.user_id)
            print(a)

    def read(self, path):
        with open(path) as f:
            return f.read()
