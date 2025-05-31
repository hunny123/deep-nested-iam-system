from fastapi import FastAPI
from app.controllers.health_check import HealthCheckController

class Application:
    def __init__(self):
        self.app = FastAPI()
        self.health_check_controller = HealthCheckController()

    def configure_routes(self):
        self.app.include_router(self.health_check_controller.get_router())

    def run(self):
        self.configure_routes()
        return self.app

app = Application().run()
