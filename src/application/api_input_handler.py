from fastapi import APIRouter, Request
from application.agent_facade import AgentFacade
import json

router = APIRouter(
    prefix="/process",
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
        bucket_name = "nv-tenant-dataset-models"
        file_key = "202/pdl_raw_company_info/pdl_raw_company_info_1732559219.335818.csv"
    
        facade = AgentFacade(bucket_name, file_key)
        result = facade.process_request({"operations": operations})

        return result

    except Exception as e:
        return {"error": str(e)}

