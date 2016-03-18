#coding:utf-8
'''
Created on 2016年3月18日
@author: panda
用例集合
'''
import unittest ,requests,time
import duaidi,jd,telematics,weather
from HTMLTestRunner import HTMLTestRunner

testunit = unittest.TestSuite()

testunit.addTest(jd.TestJd('testJdSearchPrice'))
testunit.addTest(duaidi.TestKuaidi('testKuaidiSearch'))
testunit.addTest(weather.TestWea('testWeather'))
testunit.addTest(telematics.TestTel('testTelematics'))

runner = unittest.TextTestRunner()

now = time.strftime('%y%m%d_%H%M%S')

filename = "D:\\testResult\\"+ now + 'report.html'
print filename
fp = open(filename,'wb')

runner = HTMLTestRunner(
                        stream= fp,
                        title= u'接口测试报告',
                        description = u'测试执行情况'
                        )

runner.run(testunit)

fp.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    