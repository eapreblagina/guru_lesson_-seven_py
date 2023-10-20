import os
import shutil
import zipfile
from os.path import basename
import pytest

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
RESOURCES_FOLDER = os.path.join(PROJECT_ROOT_PATH, 'resources')
TMP_FOLDER = os.path.join(PROJECT_ROOT_PATH, 'tmp')

archive_name = 'archive.zip'

txt_file = os.path.join(RESOURCES_FOLDER, 'file.txt')
xls_file = os.path.join(RESOURCES_FOLDER, 'book.xls')
xlsx_file = os.path.join(RESOURCES_FOLDER, 'тест-кейс пример.xlsx')
pdf_file = os.path.join(RESOURCES_FOLDER, 'Екатерина Преблагина.pdf')


@pytest.fixture(scope='session', autouse=True)
def test_zip_files():
    if not os.path.exists(TMP_FOLDER):
        os.mkdir(TMP_FOLDER)

    path_to_archive = f'{TMP_FOLDER}/{archive_name}'

    with zipfile.ZipFile(path_to_archive, 'w') as file:
        file.write(txt_file, basename(txt_file))
        file.write(xls_file, basename(xls_file))
        file.write(xlsx_file, basename(xlsx_file))
        file.write(pdf_file, basename(pdf_file))
    yield
    shutil.rmtree(TMP_FOLDER)
