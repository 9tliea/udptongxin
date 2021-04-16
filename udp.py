import socket #新建连接
iu = input("输入对方ip:")
while True:
    data = input("输入英文:")    #输入，接受数据
    addr=(iu,3000)   #配置端口 ip
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  #创建套接字
    s.sendto(data.encode('utf-8'), addr)   #使用套接字发送消息（data）用encode 通过已经配置好的ip 端口
    po = '已发送:'+' '+data
    print(po)


