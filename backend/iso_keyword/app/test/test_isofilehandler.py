from ..services.iso_keyword.classes.file_readers import IsoFileHandler


def test_categorize_keyword_product():
    assert IsoFileHandler._categorize_keyword_product("1234567890") == "product"
    assert IsoFileHandler._categorize_keyword_product("123456789x") == "product"
