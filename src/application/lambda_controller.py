import json
from adapters.data_loader import DataLoader
from utils.logger import logger

# Initialize DataLoader (Assume bucket_name & file_key are defined elsewhere)
data_loader = DataLoader(bucket_name="nv-tenant-dataset-models", file_key="202/pdl_raw_company_info/pdl_raw_company_info_1732559219.335818.csv")

def lambda_handler(event, context):
    """
    AWS Lambda handler for processing data.
    Expects 'operations' in the event payload to determine which functions to execute.
    """
    try:
        requested_operations = event.get("operations", [])

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
                logger.error(f"Invalid operation: {operation}")
                return {
                    "statusCode": 400,
                    "body": json.dumps({"error": f"Invalid operation: {operation}"})
                }

        return {
            "statusCode": 200,
            "body": json.dumps({"success": True, "results": results})
        }

    except Exception as e:
        logger.error(f"Error processing Lambda event: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Internal Server Error"})
        }
