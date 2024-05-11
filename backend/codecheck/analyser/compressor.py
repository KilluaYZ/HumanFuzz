"""
解压，压缩文件类
"""
import os, zipfile, tarfile, gzip
import py7zr, rarfile
class Compressor:
    def __init__(self, file_path: str, output_path: str):
        file_path = file_path.replace("\\", '/')
        output_path = output_path.replace("\\", '/')

        print(f'[DEBUG] file_path = {file_path}')
        print(f'[DEBUG] output_path = {output_path}')

        self.file_path = file_path
        self.origin_file_path = self.file_path
        self.output_path = output_path
        self.COMPRESS_TYPE = ['zip', 'tar', 'gz', 'rar', '7z']
        self.file_to_be_copy_list = []
        self.current_file_name_without_suffix = self.__get_file_name_without_suffix(self.file_path)

    def __path_join(self, path_a: str, path_b: str) -> str:
        """
        /home/sdf/123  /aaa/bbb -> /home/sdf/123/aaa/bbb
        """
        return f'{path_a}/{path_b}'

    def __get_file_suffix(self, _file_path: str) -> str:
        """
        /home/sdf/a.txt -> txt
        """
        return (os.path.splitext(_file_path)[-1][1:]).lower()

    def __get_file_path_without_suffix(self, _file_path: str) -> str:
        """
        /home/sdf/a.txt.zip -> /home/sdf/a.txt
        """
        return _file_path[:_file_path.rindex('.')]

    def __get_file_name_without_suffix(self, _file_path: str) -> str:
        """
        /home/sdf/a.zip -> a
        """
        return self.__get_file_path_without_suffix(self.__get_file_name(_file_path))

    def __get_file_name(self, _file_path):
        """
        /home/sdf/a.zip -> a.zip
        """
        return _file_path[_file_path.rindex('/') + 1:]

    def __update_file_path(self, new_file_name: str):
        self.file_path = self.__path_join(self.output_path, new_file_name)

    # zip解压缩
    def unzip_file(self):
        with zipfile.ZipFile(file=self.file_path, mode='r') as fp:
            file_list = list(map(lambda x: x.filename, fp.filelist))
            if len(file_list) > 1:
                new_file_name = self.__get_file_name_without_suffix(self.file_path)
                output_dir_path = f'{self.output_path}/{new_file_name}'
                # self.__mkdir_if_not_exist(output_dir_path)
            elif len(file_list) == 1:
                new_file_name = self.__get_file_name_without_suffix(self.file_path)
                output_dir_path = self.output_path
            else:
                raise Exception("Compressor::unzip 解压文件为空")
            fp.extractall(output_dir_path)
            self.__update_file_path(new_file_name)
        print('unzip')

    # 7z解压缩
    def un7z_file(self):
        with py7zr.SevenZipFile(self.file_path, 'r') as fp:
            file_list = fp.getnames()
            if len(file_list) > 1:
                new_file_name = self.__get_file_name_without_suffix(self.file_path)
                output_dir_path = f'{self.output_path}/{new_file_name}'
                # self.__mkdir_if_not_exist(output_dir_path)
            elif len(file_list) == 1:
                new_file_name = self.__get_file_name_without_suffix(self.file_path)
                output_dir_path = self.output_path
            else:
                raise Exception("Compressor::un7z 解压文件为空")
            fp.extractall(path=output_dir_path)
            self.__update_file_path(new_file_name)
        print('un7z')


    # tar解压缩
    def untar_file(self):
        with tarfile.open(self.file_path, 'r') as fp:
            file_list = fp.getnames()
            if len(file_list) > 1:
                new_file_name = self.__get_file_name_without_suffix(self.file_path)
                output_dir_path = f'{self.output_path}/{new_file_name}'
                # self.__mkdir_if_not_exist(output_dir_path)
            elif len(file_list) == 1:
                new_file_name = self.__get_file_name_without_suffix(self.file_path)
                output_dir_path = self.output_path
            else:
                raise Exception("Compressor::untar 解压文件为空")
            fp.extractall(path=output_dir_path)
            self.__update_file_path(new_file_name)
        print('untar')


    # RAR解压缩
    def unrar_file(self):
        with rarfile.RarFile(self.file_path, 'r') as fp:
            file_list = fp.getnames()
            if len(file_list) > 1:
                new_file_name = self.__get_file_name_without_suffix(self.file_path)
                output_dir_path = f'{self.output_path}/{new_file_name}'
                # self.__mkdir_if_not_exist(output_dir_path)
            elif len(file_list) == 1:
                new_file_name = self.__get_file_name_without_suffix(self.file_path)
                output_dir_path = self.output_path
            else:
                raise Exception("Compressor::untar 解压文件为空")
            fp.extractall(path=output_dir_path)
            self.__update_file_path(new_file_name)
        print('unrar')


   # gzip解压
    def ungz_file(self):
        file_name = self.__get_file_name(self.file_path)
        file_name = self.__get_file_path_without_suffix(file_name)
        tmp_output_path = self.__path_join(self.output_path, file_name)
        with open(tmp_output_path, "wb") as pw:
            zf = gzip.GzipFile(self.file_path, mode='rb')
            pw.write(zf.read())
            self.__update_file_path(file_name)
            zf.close()
        print('ungz')

    def __mkdir_if_not_exist(self, _dir_path: str):
        if not os.path.exists(_dir_path):
            os.mkdir(_dir_path)

    def __check_file_type_correct(self, file_type: str) -> bool:
        if self.__get_file_suffix(self.file_path) != file_type:
            return False

        if file_type == 'zip' and zipfile.is_zipfile(self.file_path):
            return True
        elif file_type == '7z' and py7zr.is_7zfile(self.file_path):
            return True
        elif file_type == 'rar' and rarfile.is_rarfile(self.file_path):
            return True
        elif file_type == 'gz':
            return True
        elif file_type == 'tar' and tarfile.is_tarfile(self.file_path):
            return True

        return False

    def uncompress(self):
        if not os.path.exists(self.file_path):
            raise Exception(f"Compressor::uncompress出错，文件{self.file_path}不存在")
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
        while True:
            # zip解压缩
            if self.__check_file_type_correct('zip'):
                self.unzip_file()
                continue

            # 7z解压缩
            if self.__check_file_type_correct('7z'):
                self.un7z_file()
                continue

            # RAR解压缩
            if self.__check_file_type_correct('rar'):
                self.unrar_file()
                continue

            # GZIP解压缩
            if self.__check_file_type_correct('gz'):
                self.ungz_file()
                continue

            # tar解压缩
            if self.__check_file_type_correct('tar'):
                self.untar_file()
                continue
            break

# c = Compressor("C:\\Users\\killuayz\\Desktop\\导向型模糊测试\\lpng1639.zip",'C:\\Users\\killuayz\\Desktop\\导向型模糊测试')
# c = Compressor("C:\\Users\\killuayz\\Desktop\\test1.zip.gz", "C:\\Users\\killuayz\\Desktop\\test1_file_output_dir")
# c = Compressor("C:\\Users\\killuayz\\Desktop\\api.7z.gz.gz.tar.zip.gz", "C:\\Users\\killuayz\\Desktop\\api_output_dir")
# c.uncompress()
# print(c.file_path)