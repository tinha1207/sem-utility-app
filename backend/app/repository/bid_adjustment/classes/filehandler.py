import pandas as pd
from fastapi import File
from fastapi.params import Form


class BidAdjustmentFileHandler:
    def __init__(self, file: bytes = File(...), data: str = Form(...)):
        self.input_df = pd.read_excel(file)
        self.params = data.dict()
