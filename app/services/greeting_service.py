from app.schemas.greeting_schemas import GreetingResponse
from datetime import datetime

class GreetingService:
    def get_greeting(self,message,status):
        # Simulate some processing
        response = GreetingResponse(
            status=status,
            message=message,
            timestamp=datetime.utcnow().isoformat()
            
        )
        return response
