from core.employee_growth import EmployeeGrowth
from core.employee_growth_by_role import EmployeeGrowthByRole
from core.top_next_employers import TopNextEmployers
from core.yoy_growth import YoYGrowth
from adapters.s3_loader import S3Loader
from ports.data_repository import DataRepository
import pandas as pd

class DataLoader(DataRepository):
    def __init__(self, bucket_name: str, file_key: str):
        # Initialize S3 loader for loading data from S3
        self.s3_loader = S3Loader(bucket_name)
        self.file_key = file_key  # File key to fetch specific file from S3

    def get_data(self) -> pd.DataFrame:
        """Fetch data from S3."""
        return self.s3_loader.load_csv(self.file_key)  # Using S3Loader to load CSV

    def load_and_process_employee_growth(self):
        """Loads data and processes employee growth by quarter."""
        raw_data = self.get_data()
        if raw_data is not None:
            employee_growth = EmployeeGrowth(raw_data)
            return employee_growth.process_employee_growth()
        return None

    def load_and_process_employee_growth_by_role(self):
        """Loads data and processes employee growth by role."""
        raw_data = self.get_data()
        if raw_data is not None:
            employee_growth_by_role = EmployeeGrowthByRole(raw_data)
            return employee_growth_by_role.process_employee_growth_by_role()
        return None

    def load_and_process_top_next_employers(self):
        """Loads data and processes top next employers."""
        raw_data = self.get_data()
        if raw_data is not None:
            top_next_employers = TopNextEmployers(raw_data)
            return top_next_employers.calculate_top_next_employers()
        return None

    def load_and_process_yoy_growth(self):
        """Loads data and processes Year-over-Year (YoY) growth."""
        raw_data = self.get_data()
        if raw_data is not None:
            yoy_growth = YoYGrowth(raw_data)
            return yoy_growth.calculate_yoy_growth()
        return None
