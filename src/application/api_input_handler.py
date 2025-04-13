from fastapi import APIRouter, Request
from application.agent_facade import AgentFacade
import json

router = APIRouter(
    prefix="/myapp/v1/process",
)

@router.post("/")
async def process_data(request: Request):
    """
    FastAPI route to handle processing requests.

    Args:
        request (Request): The incoming API request.

    Returns:
        dict: The response from AgentFacade.
    """
    try:
        body = await request.json()
        operations = body.get("operations", [])

        # Define bucket & file key
        bucket_name = config.S3_BUCKET_NAME
        file_key = config.S3_FILE_KEY

        facade = AgentFacade(bucket_name, file_key)
        result = facade.process_request({"operations": operations})

        return result

    except Exception as e:
        return {"error": str(e)}

