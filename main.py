import os
import shutil
import zipfile
from zipfile import ZipFile


def found_file(path: str, pref: str):
    for i in os.listdir(path):
        if pref == i[:len(pref)]:
            archive_zip(path, i)


def archive_zip(path:str, name: str):
    with ZipFile(f'{path}/{name}.zip', 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=3) as new_zip:
        new_zip.write(f'{path}/{name}')
    shutil.move(f'{path}/{name}.zip', 'etc/bck')


if __name__ == '__main__':
    if not os.path.exists('etc/bck'):
        os.mkdir('etc/bck')
    found_file('etc', 'cron.')
