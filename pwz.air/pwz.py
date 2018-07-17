# -*- encoding=utf8 -*-
__author__ = "linchengxiang"

from airtest.core.api import *
from airtest.core.android.adb import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import sys
sys.path.append('Z:\py\Airtest')
print('python path',sys.path)
from channel.bilibili import *
poco = AndroidUiautomationPoco()
auto_setup(__file__)

s = ADB()

sno = s.devices()
print('deviceslist',sno[0][0])
s = ADB(sno[0][0])
#install('C:/Users/linchengxiang/Downloads/100015-1.0.7-25-bilibili-1.8.2_20180711_213719.apk')

package_name = "com.baitian.yakj.pwz.bilibili"
start_app(package_name)
sleep(2)
if s.sdk_version > 23:
    touch(Template(r"tpl1531453986973.png", record_pos=(0.076, 0.095), resolution=(1920.0, 1080.0)))
    touch(Template(r"tpl1531453991848.png", record_pos=(0.09, 0.074), resolution=(1920.0, 1080.0)))
    touch(Template(r"tpl1531453995010.png", record_pos=(0.1, 0.08), resolution=(1920.0, 1080.0)))
    touch(Template(r"tpl1531453997683.png", record_pos=(0.104, 0.081), resolution=(1920.0, 1080.0)))
    touch(Template(r"tpl1531454000674.png", record_pos=(0.105, 0.098), resolution=(1920.0, 1080.0)))
sleep(100)

touch(Template(r"tpl1531819016213.png", record_pos=(0.0, 0.587), resolution=(1152, 1920)))


sleep(3)

'''
def login(name,password,pkname=package_name):
    #控件定位改为 包名：控件id
    poco("%s:id/bsgamesdk_edit_username_login" %pkname).click()
    poco("%s:id/bsgamesdk_edit_username_login" %pkname).set_text(name)
    poco("%s:id/bsgamesdk_edit_password_login" %pkname).click()
    poco("%s:id/bsgamesdk_edit_password_login" %pkname).set_text(password)
    if s.getDisplayOrientation() == 1:
        touch(Template(r"tpl1531453575697.png", record_pos=(0.355, -0.161), resolution=(1920.0, 1080.0)))
    poco("%s:id/bsgamesdk_buttonLogin" %pkname).click()
    
#login fail
def login_fail(name,password):
    login(name,password)
    sleep(2)
    assert_not_exists(Template(r"tpl1531453644692.png", record_pos=(0.115, 0.077), resolution=(1920, 1080)), "登录失败，账号或密码错误")

def login_success(name,password):
    login(name,password)
    sleep(2)
    assert_exists(Template(r"tpl1531453644692.png", record_pos=(0.115, 0.077), resolution=(1920, 1080)), "登录成功")
   '''
login_fail("handsomeduck2019","000000",package_name,s.getDisplayOrientation())
#login success
#login_success("handsomeduck2019","121212")
#sleep(2)

assert_exists(Template(r"tpl1531826621463.png", record_pos=(-0.328, 0.605), resolution=(1152, 1920)), "请填写测试点")

stop_app(package_name)
clear_app(package_name)

