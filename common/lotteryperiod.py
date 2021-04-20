import requests
from common.app_login import getAppToken
from common.tojsonstr import getJsonStr


class getPeriod:
    def __init__(self):
        self.url = 'http://192.168.0.202:9999/bet/lotteryperiods/getCurrentInfo?lotteryId=ffssc'
        self.token = getAppToken().get_token()
        self.headers = {
            'Authorization': self.token,
            'Content-Type': 'application/json'
        }

    def get_lottery_period(self):
        try:
            res = requests.get(self.url).json()['data']
            resp = getJsonStr(res).get_json_str()
            return resp['data']['period']
        except Exception as e:
            print('请求错误{}'.format(e))


if __name__ == '__main__':
    res = getPeriod().get_lottery_period()
    print(res)