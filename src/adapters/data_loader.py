from core.employee_growth import EmployeeGrowth
from core.employee_growth_by_role import EmployeeGrowthByRole
from core.top_next_employers import TopNextEmployers
from core.yoy_growth import YoYGrowth
from adapters.s3_loader import S3Loader
import pandas as pd

class DataLoader:
    def __init__(self, bucket_name: str, file_key: str):
        # Initialize S3 loader for loading data from S3
        self.s3_loader = S3Loader(bucket_name, file_key)
        self.raw_data = self.s3_loader.load_data_from_s3()
    
    def load_and_process_employee_growth(self):
        """Loads data and processes employee growth by quarter."""
        if self.raw_data is not None:
            employee_growth = EmployeeGrowth(self.raw_data)
            return employee_growth.process_employee_growth()
        else:
            return None

    def load_and_process_employee_growth_by_role(self):
        """Loads data and processes employee growth by role."""
        if self.raw_data is not None:
            employee_growth_by_role = EmployeeGrowthByRole(self.raw_data)
            return employee_growth_by_role.process_employee_growth_by_role()
        else:
            return None

    def load_and_process_top_next_employers(self):
        """Loads data and processes top next employers."""
        if self.raw_data is not None:
            top_next_employers = TopNextEmployers(self.raw_data)
            return top_next_employers.calculate_top_next_employers()
        else:
            return None

    def load_and_process_yoy_growth(self):
        """Loads data and processes Year-over-Year (YoY) growth."""
        if self.raw_data is not None:
            yoy_growth = YoYGrowth(self.raw_data)
            return yoy_growth.calculate_yoy_growth()
        else:
            return None
