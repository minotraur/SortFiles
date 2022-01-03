import zipfile
import os, time, shutil


class Copy2OtherDir:

    def __init__(self, filename, result_path):
        self.filename = os.path.normpath(filename)
        self.result_path = os.path.normpath(result_path)

    def unzip(self):
        zfile = zipfile.ZipFile(self.filename, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.filename = filename

    def collect_meta(self):
        if self.filename.endswith('.zip'):
            self.unzip()
        for dirpath, dirnames, filenames in os.walk(self.filename):
            # print(dirpath, dirnames, filenames)
            # print(os.path.dirname(dirpath))
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                secs = os.path.getmtime(full_file_path)
                file_time = time.gmtime(secs)


                for year in range(2000, 2022):
                    for month in range(1, 13):
                        if file_time[0] == year and file_time[1] == month:
                            if os.path.exists(f'{self.result_path}\\{year}\\{month}'):
                                shutil.copy2(full_file_path, f'{self.result_path}\\{year}\\{month}')
                            else:
                                os.makedirs(f'{self.result_path}\\{year}\\{month}')
                                shutil.copy2(full_file_path, f'{self.result_path}\\{year}\\{month}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Завершил работу!')

    def __enter__(self):
        print('Начал работу!')


copy = Copy2OtherDir(filename='Z:\PHOTO_VIDEO', result_path='Z:\PHOTO_VIDEO\Отсортированные фотки')
copy.collect_meta()
