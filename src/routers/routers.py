from fastapi import APIRouter, Request
from application.api_input_handler import extract_input_from_api
from adapters.controller import Controller

router = APIRouter()

@router.post("/process")
async def process_data(request: Request):
    try:
        user_input = await extract_input_from_api(request)
        controller = Controller()
        result = controller.route(user_input)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}
