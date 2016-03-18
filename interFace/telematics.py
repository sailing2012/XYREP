#coding:utf-8
'''
Created on 2016年3月18日
@author: panda
功能： 将地址转成坐标的api
http://developer.baidu.com/map/wiki/index.php?title=car/api/geocoding
'''
import unittest,requests


class TestTel(unittest.TestCase):

    def setUp(self):
        self.url =  'http://api.map.baidu.com/telematics/v3/geocoding'
        
    def tearDown(self):
        pass

    def testTelematics(self):
        u''' 地址坐标转换接口'''
        params ={'keyWord':u'北京市上地十街十号百度大厦',
        'cityName':u'北京',
        'out_coord_type':'gcj02',
        'ak':'E4805d16520de693a3fe707cdc962045'
        }
        
        req = requests.get(self.url, params)
        code = req.status_code
        text = req.text
        print  text
        self.assertEqual(code , 200 )
        self.assertIn('message', text )
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    