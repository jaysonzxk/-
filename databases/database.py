"""
author： mask
filename: databases.py
datetime： 2021/3/26 10:35 
ide： PyCharm
"""
import pymysql
import datetime
from interfaces.user_info import userInfo


class databaseOperations:
    def __init__(self):
        self.db = pymysql.connect('192.168.0.201', 'root', '123456', 'dev')
        self.cursor = self.db.cursor()
        self.date_today_start = datetime.datetime.today().strftime('%Y-%m-%d 00:00:00')
        self.date_today_end = datetime.datetime.today().strftime('%Y-%m-%d 23:59:59')
        self.user_id = userInfo().get_user_info()['data']['userId']

    def select_userid(self):
        """
        查询用户id
        :return:
        """
        sql = "SELECT username FROM sys_user WHERE user_id = '1780' LIMIT 500"
        self.cursor.execute(sql)
        username = self.cursor.fetchall()[0][0]
        return username

    def select_username(self):
        """
        查询用户name
        :return:
        """
        sql = "SELECT username FROM sys_user WHERE user_id BETWEEN 10001 AND 10500"
        self.cursor.execute(sql)
        username = self.cursor.fetchall()
        user_list = []
        for i in username:
            for name in i:
                user_list.append(name)
        return user_list

    def select_plan_detail(self):
        """
        查询计划id
        :return:
        """
        sql = "SELECT id FROM zx_aid_plan_detail WHERE lottery_id = 'sfks'"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        plan_id = []
        for i in data:
            plan_id.append(i[0])
        return plan_id

    def select_user_income(self):
        """
        查询当日充值
        :return:
        """
        sql = "SELECT SUM(pay_money) FROM zx_finance_income WHERE update_time BETWEEN '{}' AND '{}' AND user_id = '{}'".format(
            self.date_today_start, self.date_today_end, self.user_id
        )
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        if data[0][0] is None:
            return 0
        else:
            return int(data[0][0])

    def select_user_rewards(self):
        """
        获取当日彩金
        :return:
        """
        sql = "SELECT rewards_amount FROM zx_rewards WHERE user_id = '{}'".format(self.user_id)
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        if data[0][0] is None:
            return 0
        else:
            return int(data[0][0])

    def select_agent_total(self):
        sql = "SELECT all_balance FROM zx_prize WHERE user_id = '{}'".format(self.user_id)
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        if data[0][0] is None:
            return 0
        else:
            return int(data[0][0])


if __name__ == '__main__':
    res = databaseOperations().select_username()
    print(res)