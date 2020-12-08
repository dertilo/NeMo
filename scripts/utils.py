
import tarfile

from zipfile import ZipFile

ZIP_SUFFIXES = [".zip", ".ZIP"]
TAR_GZ_SUFFIXES = [".tar.gz", ".TAR.GZ",".tgz"]
COMPRESSION_SUFFIXES = ZIP_SUFFIXES + TAR_GZ_SUFFIXES

def unzip(zipfile: str, dest_dir: str) -> None:

    if any([zipfile.endswith(s) for s in ZIP_SUFFIXES ]):
        with ZipFile(zipfile, "r") as zipObj:
            zipObj.extractall(dest_dir)
    elif any([zipfile.endswith(s) for s in TAR_GZ_SUFFIXES]):
        with tarfile.open(zipfile, mode="r:gz") as tar:
            tar.extractall(dest_dir)
    else:
        raise NotImplementedError
