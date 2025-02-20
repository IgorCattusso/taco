# Third-Party Libraries
from flask import Flask
from injector import inject


class TestController:
    @inject
    def __init__(
            self,
            app: Flask
    ) -> None:
        self.app = app

    def start_routes(self):
        self.app.add_url_rule('/taco/controller', view_func=self.process_event, methods=['GET'])

    def process_event(self):
        return "hello world"
