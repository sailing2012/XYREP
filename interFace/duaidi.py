#coding:utf-8
'''
Created on 2016-3-17
@author: panda 
http://www.kuaidiapi.cn/rest/?uid=10002&key=123123123&order=6108241734&id=dtwl
http://apis.haoservice.com/sms/send?mobile=手机号&tpl_id=2&tpl_value=%23code%23%3d20140713121717%26%23company%23%3d好服务&key=您申请的APPKEY

'''
import unittest,requests

class TestKuaidi(unittest.TestCase):
    
    def setUp(self):
        self.url = 'http://www.kuaidiapi.cn/rest1/'
        
    def tearDown(self):
        pass
        
    def testKuaidiSearch(self):
        u''' 快递查询'''
        params ={'uid':'10002','key':'123123123','order':'6108241734','id':'dtwl'}  
        
        req = requests.get(self.url,params)
        print req.url
        code = req.status_code
        self.assertEqual(code, 200  )
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()