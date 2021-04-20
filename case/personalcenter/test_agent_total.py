
import unittest
import json
import requests
from ddt import data, ddt
from common.logger import Log
from common.tojsonstr import getJsonStr
from common.base import get_host


@ddt
class testAgenttotal(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.log = Log()
        cls.url = get_host('test') + '/admin/agent/prizeTotal'
        cls.data = "{\n \"startTime\": \"\",\n \"endTime\": \"\",\n \"bizType\": \"ALL\"\n}"
        cls.headers = {'Content-Type': 'application/json', 'authorization': 'bearer 4cb6a59d-3e16-493f-922e-5146ca58f87d'}
        cls.method = 'post'
    
    @data(*([0, '']))
    def test_agent_total(self, test_data):
        '''
        测试获取获取佣金汇总接口
        :param:
        :return:
        '''
        # 判断是否需要转换传参的数据类型
        if self.method == 'post':
            if self.headers.get('Content-Type') == 'application/json;charset=UTF-8' and self.data != 'nan':
                results = requests.post(self.url, data=self.data, headers=self.headers).json()
                results_str = getJsonStr(results['data']).get_json_str()
                results['data'] = results_str['data']
                response = [results['code'], results['msg']]
            elif self.data == 'nan':
                results = requests.post(self.url, headers=self.headers).json()
                results_str = getJsonStr(results['data']).get_json_str()
                results['data'] = results_str['data']
                response = [results['code'], results['msg']]
            else:
                results = requests.post(self.url, data=self.data, headers=self.headers).json()
                results_str = getJsonStr(results['data']).get_json_str()
                results['data'] = results_str['data']
                response = [results['code'], results['msg']]
            self.log.info('----------测试开始----------')
            self.log.info('测试场景：[获取佣金汇总]')
            self.log.info("测试断言-->期望值/校验值[[0, '']]")
            self.log.info('测试断言-->实际值[%s]' % response)
            self.log.info('请求参数:"{\n \"startTime\": \"\",\n \"endTime\": \"\",\n \"bizType\": \"ALL\"\n}"')
            self.log.info('请求接口:%s' % self.url)
            self.log.info('请求方法:post')
            self.log.info('响应结果:%s' % results)
            self.assertIn(test_data, response, msg='测试不通过，失败原因：%s not in %s' %
                                                      (test_data, response))
            self.log.info('测试断言[%s]通过' % test_data)
            self.log.info('----------测试通过----------')
            self.log.info('----------测试结束----------')
            self.log.info('=======================================================')
        elif self.method == 'get':
            if self.headers.get('Content-Type') == 'application/json;charset=UTF-8' and self.data != 'nan':
                results = requests.get(self.url, data=json.dumps(self.data), headers=self.headers).json()
                results_str = getJsonStr(results['data']).get_json_str()
                results['data'] = results_str['data']
                response = [results['code'], results['msg']]
            elif self.data == 'nan':
                results = requests.get(self.url, headers=self.headers).json()
                results_str = getJsonStr(results['data']).get_json_str()
                results['data'] = results_str['data']
                response = [results['code'], results['msg']]
            else:
                results = requests.get(self.url, data=self.data, headers=self.headers).json()
                results_str = getJsonStr(results['data']).get_json_str()
                results['data'] = results_str['data']
                response = [results['code'], results['msg']]
            self.log.info('----------测试开始----------')
            self.log.info('测试场景：[获取佣金汇总]')
            self.log.info("测试断言-->期望值/校验值[[0, '']]")
            self.log.info('测试断言-->实际值[%s]' % response)
            self.log.info('请求参数:"{\n \"startTime\": \"\",\n \"endTime\": \"\",\n \"bizType\": \"ALL\"\n}"')
            self.log.info('请求接口:%s' % self.url)
            self.log.info('请求方法:post')
            self.log.info('响应结果:%s' % results)
            self.assertIn(test_data, response, msg='测试不通过，失败原因：%s not in %s' %
                                                      (test_data, response))
            self.log.info('测试断言[%s]通过' % test_data)
            self.log.info('----------测试通过----------')
            self.log.info('----------测试结束----------')
            self.log.info('=======================================================')

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
