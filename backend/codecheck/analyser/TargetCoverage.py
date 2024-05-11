import os
from codecheck.container.DockerManager import DockerContainer
import subprocess
import linecache
import math

class TargetCoverageChecker:
    def __init__(self, target_file_path: str, cov_text_root: str):
        self.target_file_path = target_file_path
        self.cov_text_root = cov_text_root
        self.targets_list = self.init_targets(self.target_file_path)

    def get_coverage_result(self) -> list:
        result = []

        text_report_root_path = f"{self.cov_text_root}/coverage"
        for target_file in self.targets_list:
            for root, dirs, files in os.walk(text_report_root_path, topdown=True):
                for _file in files:
                    if f"{target_file['file']}.txt" == _file:
                        # 找到了对应的file
                        single_file_path = f"{root}/{_file}"
                        begin_line_no = target_file["begin"]
                        end_line_no = target_file["end"]
                        cover_num = self.get_single_file_cover_num_by_text_reports(
                            single_file_path, begin_line_no, end_line_no
                        )
                        result.append(
                            {
                                "file": _file,
                                "begin": begin_line_no,
                                "end": end_line_no,
                                "freq": cover_num,
                            }
                        )
        return result

    def init_targets(self, target_path) -> list:
        result = []
        try:
            with open(target_path, "r") as f:
                lines = f.readlines()
                for idx, line in enumerate(lines):
                    if line == "" or line.isspace():
                        continue
                    splited_str1 = line.split(":")
                    if len(splited_str1) != 2:
                        raise Exception("Invalid Grammar")
                    # 解析得到文件名
                    file_name = splited_str1[0].strip()

                    # 解析得到对应的行数  支持两种语法：
                    # valid.c: 2001
                    # valid.c: 3000 - 4000
                    target_line_number = splited_str1[1]
                    if target_line_number.find("-") != -1:
                        start_number, end_number = tuple(target_line_number.split("-"))
                        start_number = int(start_number)
                        end_number = int(end_number)

                    else:
                        # target_line_number_list.append(int(target_line_number))
                        start_number = int(target_line_number)
                        end_number = int(target_line_number)

                    result.append(
                        {"file": file_name, "begin": start_number, "end": end_number}
                    )

        except Exception as e:
            print(e)
            print(f"解析target文件时出现错误，出错行号： {idx + 1}")

        return result

    def get_single_file_cover_num_by_text_reports(
        self, single_file_path: str, begin_line_no: int, end_line_no: int
    ) -> int:
        cnt = 0
        target_lines_list = list(range(begin_line_no, end_line_no + 1))
        for line_no in target_lines_list:
            line_content = linecache.getline(single_file_path, line_no + 3)
            splited_lines = line_content.split("|")
            cover_num = splited_lines[1].strip()
            if cover_num.isdigit():
                cnt += int(cover_num)
        return cnt


def cal_target_coverage(project_obj: dict, case_obj: dict, container_obj: DockerContainer) -> int:
    try:
        binary_cov_path = project_obj['binary_cov_path']
        file_path_in_container = case_obj['fname']
        binary_args = project_obj['binary_args'].replace('@@', file_path_in_container)
        profraw_file_path_in_container = f"/share/codecheck.profraw"
        profdata_file_path_in_container = f"/share/codecheck.profdata"
        container_obj.execute(f'LLVM_PROFILE_FILE={profraw_file_path_in_container} {binary_cov_path} {binary_args} ')
        container_obj.execute(f'/root/llvm-tools/llvm-profdata merge -sparse {profraw_file_path_in_container} -o {profdata_file_path_in_container} ')
        container_obj.execute(f'/root/llvm-tools/llvm-cov show {binary_cov_path} -instr-profile={profdata_file_path_in_container} -format=text -output-dir=/share/cov_text/ ')

        text_root_path = f'{container_obj.share_dir}/share/cov_text/'
        if not os.path.exists(f"{text_root_path}/index.txt"):
            return -1

        target_file_path = f"{container_obj.share_dir}/{project_obj['target_path']}"
        tcc = TargetCoverageChecker(target_file_path, text_root_path)
        result = tcc.get_coverage_result()
        score = 0
        for i in range(len(result)):
            coefficient = 0
            freq = result[i]['freq']
            if freq > 0:
                coefficient = math.log2(float(freq))
            score = score + min(freq, 9)*(10**i) + coefficient
        return score

    except Exception as e:
        print(e)
        return -1