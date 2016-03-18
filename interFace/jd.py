#-*-coding:utf-8-*-
'''
Created on  2016-3-17
@author: panda
http://p.3.cn/prices/mgets?skuIds=J_��ƷID&typ
'''
import unittest,requests 
class TestJd(unittest.TestCase):
    
    def setUp(self):
        self.url =  'http://p.3.cn/prices/mgets'
    def tearDown(self):
        pass
    
    def testJdSearchPrice(self):
        u''' 京东查询物品'''
        url = 'http://p.3.cn/prices/mgets'
        params = {'skuIds':'J_10124147160','type':'1'}
        req = requests.get(self.url,params)
        
        code = req.status_code
        self.assertEqual(code, 200 )
        
if __name__ == "__main__":
    unittest.main()     


    


