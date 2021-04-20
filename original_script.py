"""
author： mask
filename: original_script.py
datetime： 2021/4/12 13:29 
ide： PyCharm
"""
import os
import pandas as pd
from common.logger import Log
from common.app_login import getAppToken
from config.baseCase import test_case
import json

cur_path = os.path.dirname(os.path.abspath(__file__))

# 创建case目录
case_path = os.path.join(cur_path, 'case')
if not os.path.exists(case_path):
    os.mkdir(case_path)
    with open(case_path + '\__init__.py', 'a+') as f:
        pass

interfaces_path = os.path.join(cur_path, 'interfaces')
if not os.path.exists(case_path):
    os.mkdir(interfaces_path)
    with open(interfaces_path + '\__init__.py', 'a+') as f:
        pass


class CreateTestCase:
    def __init__(self, file_name='app_test_data.xlsx'):
        self.file_name = file_name
        self.file_path = os.path.join(cur_path, 'test_data', self.file_name)
        self.s = pd.ExcelFile(self.file_path)
        self.log = Log()

    def create_test_module(self):
        """
        1.动态获取表格中配置的测试模块即sheet名称
        2.在case目录下面动态生成测试模块
        3.如果测试模块下存在test开头的文件,先删除,因为每一次动态生成测试,防止某个城市接口修改后和之前的接口重复
        :return: sheet名称
        """
        self.log.info('正在创建测试模块，请稍后。。。 。。。')
        test_case_modules = []
        sheet_mame = self.s.sheet_names
        # 动态创建测试模块，根据测试数据表格里的sheet名称
        for sheetname in sheet_mame:
            if sheetname != 'login' and sheetname != 'common'\
                    and sheetname != 'register':
                test_case_path = os.path.join(case_path, sheetname)
                if not os.path.exists(test_case_path):
                    os.makedirs(os.path.join(case_path, sheetname))
                    with open(os.path.join(case_path, sheetname) + '\__init__.py', 'a+') as f:
                        pass
                test_case_module = os.path.join(case_path, sheetname)  # 测试模块路径
                test_case_modules.append(test_case_module)
                test_case_module_list = os.listdir(test_case_module)  # 获取每个测试模块里面的文件数, 存在一个list
                # 删除原有的测试用例，防止改名后重复
                if len(test_case_module_list) > 1:
                    for root, dirs, files in os.walk('./case'):
                        for name in files:
                            if name.startswith("test"):
                                os.remove(os.path.join(root, name))

        return sheet_mame

    def create_test_case(self):
        """
        自动创建测试用例
        :return:
        """
        sheet_mame = self.create_test_module()
        self.log.info('正在生成最新测试用例，请稍后。。。 。。。')
        # 动态创建测试模块，根据测试数据表格里的sheet名称
        for sheetname in sheet_mame:
            data = pd.read_excel(self.file_path, sheet_name=sheetname)
            cases = data.values.tolist()
            for i in cases:
                case_dict = {sheetname: i}
                # 创建测试模块
                if sheetname != 'login' and sheetname != 'common' \
                        and sheetname != 'register':
                    test_case_path = os.path.join(case_path, sheetname)
                    # 创建测试用例
                    for k, v in case_dict.items():
                        case_file = 'test_' + v[1] + '.py'
                        case_file = os.path.join(test_case_path, case_file)
                        class_name = v[1].replace('_', '').capitalize()  # 测试类名
                        test_scenario = v[-1]  # 测试场景
                        req_method = v[2]  # 请求方法
                        headers = v[6]  # 请求头部
                        # 注册不用加token
                        if sheetname != 'register':
                            headers = json.loads(headers)
                            headers['authorization'] = getAppToken().get_token()
                        expect_res = v[8]  # 期望值
                        expect_res = json.loads(expect_res)
                        expect_res = [expect_res['code'], expect_res['message']]
                        req_data = v[5]  # 请求参数
                        if isinstance(req_data, float):
                            req_data = None
                        else:
                            req_data = json.dumps(req_data)
                        req_api = v[3]  # 请求接口
                        req_module = v[1]  # 请求方法
                        if case_file.endswith('.py'):
                            with open(case_file, 'w+', encoding='utf-8') as f:
                                f.write(
                                    test_case.format(
                                        class_name, req_api, req_data, headers, req_method, expect_res, req_module,
                                        # post
                                        test_scenario, test_scenario, expect_res, req_data,
                                        req_method,
                                        # get
                                        test_scenario, expect_res, req_data,
                                        req_method
                                    )
                                )
        self.log.info('生成最新测试用例完成。。。 。。。')


if __name__ == '__main__':
    CreateTestCase().create_test_case()