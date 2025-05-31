from pydantic import BaseModel
class GreetingResponse(BaseModel):
    status: str
    message: str
    timestamp: str
    