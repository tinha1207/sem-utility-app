from fastapi import File
from fastapi.params import Form
from fastapi.responses import FileResponse
import os

from .classes.file_readers import IsoFileHandler


def create_iso_file_handler(
    account: str = Form(...),
    file: bytes = File(...),
):
    path = f"{os.getcwd()}//app//services//utility//iso_keyword//static//iso_bulksheet.xlsx"
    fh = IsoFileHandler(account=account, file=file)
    fh.build_good_df()
    fh.build_bad_df()
    fh.export_bulksheet(path)
    return FileResponse(path, headers={"Content-Type": "multipart/form-data"})


def download_iso_template():
    path = (
        f"{os.getcwd()}//app//services//utility//iso_keyword//static//iso_template.xlsx"
    )
    return FileResponse(path, headers={"Content-Type": "multipart/form-data"})
