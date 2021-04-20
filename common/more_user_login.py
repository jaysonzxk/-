"""
author： mask
filename: more_user_login.py
datetime： 2021/4/1 17:16 
ide： PyCharm
"""
from common.base import get_response, get_host
from test_data.read_data import get_test_data
from databases.database import databaseOperations
from common.logger import Log
import json


class getMoreToken(object):
    def __init__(self):
        self.test_data = get_test_data('app_test_data.xlsx', 'login', 2)
        self.log = Log()
        self.username_list = databaseOperations().select_username()
        self.url = get_host('test') + self.test_data['url']
        self.method = self.test_data['method']
        self.data = self.test_data['data']
        self.header = json.loads(self.test_data['header'])

    def get_more_token(self):
        """
        获取app登录token
        :return:token.txt
        """
        self.log.info('正在写入用户token,请稍后')
        for i in self.username_list:
            payload = 'username=' + i + self.data
            resp = get_response(self.url, self.method,
                                data=payload, headers=self.header)
            token = resp.json()['token_type'] + ' ' + resp.json()['access_token']
            with open('token.txt', 'a') as f:
                f.writelines(token)
                f.writelines('\n')
        self.log.info('写入用户token完成')


if __name__ == '__main__':
    getMoreToken().get_more_token()