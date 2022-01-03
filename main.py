import zipfile
import os, time, shutil


class Copy2OtherDir:

    def __init__(self, filename, result_path):
        # Нормализуем пути
        self.filename = os.path.normpath(filename)
        self.result_path = os.path.normpath(result_path)

    def __enter__(self):
        print('Начал работу!')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Завершил работу!')

    # Метод который вызывается если на вход даётся архив .zip
    def unzip(self):
        """Method for unpacking .zip archives"""
        zfile = zipfile.ZipFile(self.filename, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.filename = filename

    # Метод обработки
    def collect_meta(self):
        """A method of collecting data and data about files, and then sorting into another directory"""
        if self.filename.endswith('.zip'):
            self.unzip()
        for dirpath, dirnames, filenames in os.walk(
                self.filename):  # В переменные записываются путь, имя директории и имя файла соответственно
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                secs = os.path.getmtime(full_file_path)  # Получаем секунды с начала эпохи
                file_time = time.gmtime(secs)  # Конвертируем в привычный формат

                for year in range(2000, 2022):
                    for month in range(1, 13):
                        if file_time[0] == year and file_time[1] == month:
                            # Если директория существует, то запишем в неё файл
                            if os.path.exists(f'{self.result_path}\\{year}\\{month}'):
                                shutil.copy2(full_file_path, f'{self.result_path}\\{year}\\{month}')
                            # Иначе создадим директорию и запишем файл
                            else:
                                os.makedirs(f'{self.result_path}\\{year}\\{month}')
                                shutil.copy2(full_file_path, f'{self.result_path}\\{year}\\{month}')


copy = Copy2OtherDir(filename='Z:\PHOTO_VIDEO', result_path='Z:\PHOTO_VIDEO\Отсортированные фотки')
copy.collect_meta()
