[TOC]
# centos 7�´shadowsocks #

## 1.��װpip ##

���ڰ�װ����python �汾�� shadowsocks���������Ȱ�װpip

	# curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
	# python get-pip.py

## 2.��װshadowsocks ##

	# pip install --upgrade pip
	# pip install shadowsocks

## 3.���������ļ� ##


�����ļ�����

	# vim /etc/shadowsocks.json

�����ļ����ݣ�


���˿ڰ棺

	 {
	 "server":"0.0.0.0",            --������IP��ֱ����0.0.0.0Ҳ��
	 "server_port":8888,            --�˿ڶ˿�
	 "local_address": "127.0.0.1",  --���ص�ַ����ʡ��
	 "local_port":1080,             --���ض˿ڣ���ʡ��
	 "password":"password",         --����
	 "timeout":300,                 --��ʱʱ�䣬��ʡ��
	 "method":"aes-256-cfb",        --���ܲ��ԣ��ж��ز��ԣ������Բ�
	}

��˿ڰ棺

	{
	    "server":"0.0.0.0",
	    "local_address":"127.0.0.1",
	    "local_port":1080,
	    "port_password":{           --ÿ���˿ڶ�Ӧһ������
	        "1111":"password1",
	        "1112":"password2",
	        "1113":"password3"
	    },
	    "timeout":300,
	    "method":"aes-256-cfb",
	    "fast_open":false
	}

## 4.����shadowsocks ##

- ����

	ssserver -c /etc/shadowsocks.json -d start

- ֹͣ

	ssserver -c /etc/shadowsocks.json -d stop
- ����

	ssserver -c /etc/shadowsocks.json -d restart

�����ɹ�����ͨ��ss�ͻ���ʹ��

���ص�ַ [shadowsocks-windows](https://github.com/shadowsocks/shadowsocks-windows/releases)

��window�˿����ڿ���̨ͨ����������鿴�˿��Ƿ��

	telnet {ip} {potr}

## 5.���������� ##

�½������ű��ļ�/etc/systemd/system/shadowsocks.service���������£�

	[Unit]
	Description=Shadowsocks
	
	[Service]
	TimeoutStartSec=0
	ExecStart=/usr/bin/ssserver -c /etc/shadowsocks.json
	
	[Install]
	WantedBy=multi-user.target

ͨ����������ע�ᣬ��������

	# systemctl enable shadowsocks
	# systemctl start shadowsocks

��������Բ鿴����״̬

	# systemctl status shadowsocks -l

�������ɹ���

	shadowsocks.service - Shadowsocks
	   Loaded: loaded (/etc/systemd/system/shadowsocks.service; enabled; vendor preset: disabled)
	   Active: active (running) since Sun 2017-08-13 18:03:41 CST; 1h 29min ago
	 Main PID: 9567 (ssserver)
	   CGroup: /system.slice/shadowsocks.service
	           ����9567 /usr/bin/python2 /usr/bin/ssserver -c /etc/shadowsocks.json

## 6.firewalld����ǽ ##

centos7�õ�firewalld�������������ã����ܻᵼ��SS�޷�ʹ��

�ⲿ�ֹ������ͨ�������ư�ȫ����ӣ�Ҳ����ֱ��ͨ��������ӣ��������ֱ����ӹ��򷽷�

## ���Ŷ˿� ##

	# firewall-cmd --permanent --add-port=18381-18385/tcp 

## �޸Ĺ������Ҫ���� ##

	# firewall-cmd --reload 

## �ر�selinux ##

	#vim /etc/selinux/config

		SELINUX=disabled

	#setenforce 0
