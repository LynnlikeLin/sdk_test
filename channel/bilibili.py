# -*- encoding=utf8 -*-
__author__ = "linchengxiang"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco()
auto_setup(__file__)


def login(name,password,pkname,orientation):
    poco("%s:id/bsgamesdk_edit_username_login" %pkname).click()
    poco("%s:id/bsgamesdk_edit_username_login" %pkname).set_text(name)
    poco("%s:id/bsgamesdk_edit_password_login" %pkname).click()
    poco("%s:id/bsgamesdk_edit_password_login" %pkname).set_text(password)
	#竖屏游戏输入密码时不会进入键盘界面，没有完成按钮？
    #横屏时需点击键盘界面的完成按钮
    if orientation == 1:
        touch(Template(r"tpl1531453575697.png", record_pos=(0.355, -0.161), resolution=(1920.0, 1080.0)))
    poco("%s:id/bsgamesdk_buttonLogin" %pkname).click()
#需要传3个参数，目前先把第3个参数template去掉
def login_fail(name,password,pkname,orientation=1):
    login(name,password,pkname,orientation)
    sleep(2)
    assert_not_exists(Template(r"tpl1531453644692.png", record_pos=(0.115, 0.077), resolution=(1920, 1080)), "登录失败，账号或密码错误")

def login_success(name,password,package_name,orientation=1):
    login(name,password,pkname,orientation)
    sleep(2)
    assert_exists(Template(r"tpl1531453644692.png", record_pos=(0.115, 0.077), resolution=(1920, 1080)), "登录成功")



