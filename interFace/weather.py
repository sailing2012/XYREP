#coding:utf-8
'''
Created on 2016年3月18日
@author: panda
'''
import unittest,requests


class TestWea(unittest.TestCase):

    def setUp(self):
        self.url = 'http://wthrcdn.etouch.cn/weather_mini'

    def tearDown(self):
        pass

    def testWeather(self):
        ''' '''     
        par ={'citykey':'101090301'}
        req = requests.get(self.url,par)
        print req.url
        
        code = req.status_code
        self.assertEqual(code, 200)
        text = req.text
        #print text
        self.assertEquals(code, 200 )
        #self.assertIn('desc', text) 
        self.assertIn(u'张家口', text) 
        #self.assertIsInstance(obj, cls, msg)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    