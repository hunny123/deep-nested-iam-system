from fastapi import APIRouter , Depends, Request
from app.services.greeting_service import GreetingService
from app.schemas.greeting_schemas import GreetingResponse


class HealthCheckController:
    def __init__(self):
        self._router = APIRouter(prefix="/health", tags=["Health"])
        self._register_routes()

    def _register_routes(self):
        self._router.add_api_route("/", self.health_check, methods=["GET"], response_model=GreetingResponse)

    async def health_check(self,request:Request, service: GreetingService = Depends(GreetingService)):
       
        greeting = request.query_params.get("greeting", "Hello world")
        status = request.query_params.get("code", "200")
        return service.get_greeting(greeting, status)

    def get_router(self) -> APIRouter:
        return self._router
    
