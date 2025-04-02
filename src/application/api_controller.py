import json
from fastapi import APIRouter, HTTPException
from adapters.data_loader import DataLoader
from utils.logger import logger

router = APIRouter(prefix="/process")

# Initialize DataLoader (Assume bucket_name & file_key are defined elsewhere)
data_loader = DataLoader(bucket_name="nv-tenant-dataset-models", file_key="202/pdl_raw_company_info/pdl_raw_company_info_1732559219.335818.csv")
    
@router.post("/")
async def process_data(request: dict):
    """
    API Endpoint to process data based on user input.
    Expects a JSON payload with the list of operations to perform.
    """
    try:
        requested_operations = request.get("operations", [])

        # Mapping operation names to functions
        operations_map = {
            "employee_growth": data_loader.load_and_process_employee_growth,
            "employee_growth_by_role": data_loader.load_and_process_employee_growth_by_role,
            "top_next_employers": data_loader.load_and_process_top_next_employers,
            "yoy_growth": data_loader.load_and_process_yoy_growth,
        }

        results = {}

        for operation in requested_operations:
            if operation in operations_map:
                results[operation] = operations_map[operation]()
            else:
                raise HTTPException(status_code=400, detail=f"Invalid operation: {operation}")

        return {"success": True, "results": results}

    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
