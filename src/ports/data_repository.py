from abc import ABC, abstractmethod
import pandas as pd

class DataRepository(ABC):
    @abstractmethod
    def get_data(self) -> pd.DataFrame:
        pass
