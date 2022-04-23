from fastapi import APIRouter, File, UploadFile
from fastapi.params import Form
from fastapi.responses import FileResponse


from app.services.iso_keyword.iso_keyword import (
    create_iso_file_handler,
    download_iso_template,
)


router = APIRouter(tags=["Iso Keyword"], prefix="/utility/iso_keyword")


@router.post("/")
def upload_file(file: bytes = File(...), account: str = Form(...)):
    print("hello")
    return create_iso_file_handler(account, file)


@router.get("/template")
def download_template():
    return download_iso_template()
