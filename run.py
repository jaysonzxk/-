import sys
import unittest
import os
import time
from HwTestReport import HTMLTestReport
from tqdm import tqdm

# 当前脚本所在文件真实路径
cur_path = os.path.dirname(os.path.abspath(__file__))
abs_path = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))
sys.path.append(abs_path)


def add_case(rule):
    """
    第一步：加载所有的测试用例
    :param rule:测试用例文件命令规则
    :return:
    """
    f_path = os.path.dirname(os.path.abspath(__file__))
    # 动态获取被测项目
    # for root, dirs, files in os.walk(f_path):
    #     if product in root and root.endswith(module):
    #         case_path = root  # 需要执行用例文件夹
    discover = unittest.defaultTestLoader.discover(f_path,
                                                   pattern=rule,
                                                   top_level_dir=None)
    return discover


def run_case(allCase, reportName="report"):
    """
    第二步：执行所有的用例，并把结果写入HTML测试报告
    :param allCase:
    :param reportName:
    :return:
    """
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    reportPath = os.path.join(cur_path, reportName)  # 报告文件夹
    # 如果不存在就创建
    if not os.path.exists(reportPath):
        os.mkdir(reportPath)

    report_abspath = os.path.join(reportPath, now + "result.html")
    with open(report_abspath, 'wb') as f:
        runner = HTMLTestReport(stream=f,
                                verbosity=2,
                                title='app接口测试报告',
                                description='接口测试执行情况',
                                tester='mask')

        # 调用add_case返回值
        runner.run(allCase)  # discover
    # fp.close()


def get_report_file(reportPath):
    """
    第三步：获取最新的测试报告
    :param reportPath:
    :return:
    """
    lists = os.listdir(reportPath)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(reportPath, fn)))
    print("最新测试报告: " + lists[-1])
    # 找到最新生成的测试报告
    reportfile = os.path.join(report_path, lists[-1])
    return reportfile


if __name__ == "__main__":
    from original_script import CreateTestCase

    CreateTestCase().create_test_case()

    all_case = add_case('test*')  # 1 加载用例
    # 生成测试报告路径
    case_count = all_case.countTestCases()
    run_case(all_case)  # 2 执行用例
    for i in tqdm(range(0, case_count)):
        time.sleep(0.01)
    report_path = os.path.join(cur_path, "report")  # 用例文件
    report_list = os.listdir(report_path)
    report_file = get_report_file(report_path)  # 3 获取最新测试报告
