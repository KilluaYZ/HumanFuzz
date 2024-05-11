import base64
import os
"""
fileCategory:
text
directory
binary
image
"""
class SourceCodeReader:
    def __init__(self, ROOT_PATH: str):
        self.ROOT_PATH = ROOT_PATH
        self.PICTURE_TYPES = ('jpeg', 'jpg', 'png', 'tif', 'gif', 'bmp', 'svg')

    def read_img(self, path: str) -> str:
        """
        读取图片
        base64编码后的图片
        """
        content = ''
        with open(os.path.join(self.ROOT_PATH, path), 'rb') as f:
            content = f.read()
        return str(base64.b64encode(content))

    def read_text(self, path: str) -> list:
        """
        读入文本内容，
        [
            {
                "content":"zxczxczxczxczxczxc",
                "lineNo": 123,
                "problem":{}
            },
        ]
        """
        lines = []
        with open(path) as f:
            lines = f.readlines()

        result = []
        line_no = 1
        for line in lines:
            result.append({"content":line.replace('\n',''), "id": line_no})
            line_no += 1

        return result

    def check_file_is_text_exact(self, path: str):
        try:
            with open(path) as file:
                lines = file.readlines()
            return True
        except Exception:
            # 解码出错，说明该文件是二进制文件，而非文本
            return False

    def read_dir(self, path: str) -> dict:
        """
        读入目录内容
        {
            root: xxxxx,
            children:[
                [
                    {
                        fileCategory: text,
                        fileName: file1.txt,
                        fileType: txt
                    },
                    {
                        fileCategory: directory,
                        fileName: dir1
                    }
                ]
            ]
        }
        """
        result = {}
        for root, dirs, files in os.walk(path):
            result['root'] = root
            children_list = []
            for dir in dirs:
                children_list.append({
                    "fileCategory": "directory",
                    "fileName": dir
                })

            for file in files:
                file_category, file_suffix = self.get_file_suffix_and_category(f'{root}/{file}')
                children_list.append({
                    "fileCategory": file_category,
                    "fileName": file,
                    "fileType": file_suffix
                })
            result['children'] = children_list
            break
        return result


    def get_file_category_type(self, path: str) -> tuple:
        if os.path.isdir(path):
            # 如果是目录
            return ('directory', None)
        elif os.path.isfile(path):
            # 如果是普通文件
            if path.endswith(self.PICTURE_TYPES):
                return ('file','image')
            else:
                # return ('file', 'text')
                if self.check_file_is_text_exact(path):
                    return ('file','text')
                else:
                    return ('file','binary')
        else:
            # 如果是特殊文件
            return ('special', None)

    def get_file_suffix(self, path: str):
        return os.path.splitext(path)[-1][1:]

    def get_file_suffix_and_category(self, path: str):
        category1, category2 = self.get_file_category_type(path)
        if category1 == 'directory':
            return 'directory', None
        elif category1 == 'file':
            suffix = self.get_file_suffix(path)
            return category2, suffix
        elif category1 == 'special':
            return 'special', None

    def read(self, relative_path: str):
        abs_path = f"{self.ROOT_PATH}/{relative_path}"

        response = {}
        file_category, file_type = self.get_file_category_type(abs_path)
        # print(f'[DEBUG] file_category = {file_category}, file_type = {file_type}')
        if file_category == 'directory':
            response['content'] = self.read_dir(abs_path)
            response['fileCategory'] = 'directory'
        elif file_category == 'file' and file_type == 'image':
            response['content'] = self.read_img(abs_path)
            response['fileCategory'] = 'image'
            response['fileType'] = self.get_file_suffix(abs_path)
        elif file_category == 'file' and file_type == 'text':
            response['fileCategory'] = 'text'
            response['content'] = self.read_text(abs_path)
            response['fileType'] = self.get_file_suffix(abs_path)
        elif file_category == 'file' and file_type == 'binary':
            response['fileCategory'] = 'binary'
            response['fileType'] = self.get_file_suffix(abs_path)
        else:
            raise Exception(f"SourceCodeReader::read，打开文件{abs_path}失败，不支持的文件类型")

        return response

# scr = SourceCodeReader("C:/Users/killuayz/Desktop/导向型模糊测试/lpng1639")
# print(json.dumps(scr.read(''), indent=4))