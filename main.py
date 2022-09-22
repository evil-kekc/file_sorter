import time
from typing import Iterable, Union
import logging
import os

from config import *

logs_folder.mkdir() if not logs_folder.exists() else None

logging.basicConfig(filename=f"logs/file_sorter.log",
                    level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s - %(message)s',
                    datefmt='%H:%M:%S',
                    encoding='utf-8')


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        logging.info(f'{func.__name__} took {end_time - start_time} seconds')
        print(f'{func.__name__} took {end_time - start_time} seconds')

    return wrapper


class Folder:
    """A class to organize log files. """

    def __init__(self, path: Union[Path, str]) -> None:
        self.path = path

    def _get_file_paths(self) -> Iterable:
        """Getting file paths

        :return: return an iterator of file paths
        """
        return (file.path for file in os.scandir(self.path) if not file.is_dir())

    def _create_subfolder(self, subfolder_name: str) -> None:
        """Creating a subfolder

        :param subfolder_name: name of the subfolder
        :return:
        """
        try:
            subfolder_path = self.path / subfolder_name
            if not subfolder_path.exists():
                subfolder_path.mkdir()
        except OSError:
            logging.error(f'Failed to create subfolder')

    def sort_files_by_extensions(self) -> None:
        """Sorting files by extensions

        :return:
        """
        try:
            file_count = 0
            for filepath in self._get_file_paths():
                path = Path(filepath)
                extension = Path(filepath).suffix.split('.')[-1]

                if extension in extensions:
                    subfolder_name = get_subfolder_name_by_extension(extension)
                    self._create_subfolder(subfolder_name)

                    new_path = Path(self.path, subfolder_name, path.name)
                    logging.info(f'{path.name} ---> {"/".join(new_path.parts[-2:])}')
                    path.rename(new_path)
                    file_count += 1
            logging.info(f'Files sorted: {file_count}')
        except Exception as ex:
            logging.error(f'Failed to sort files -> {repr(ex)}')


@timer
def sorted_files() -> None:
    """Sorting files by extension"""
    folder = Folder(folder_path)
    print('Sorting files by extensions in', folder_path)
    logging.info(f'Sorting files by extensions in {folder_path}')
    folder.sort_files_by_extensions()


if __name__ == "__main__":
    sorted_files()
