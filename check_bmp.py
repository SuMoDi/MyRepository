import struct

def judgebmp(file_name):
    with open(file_name,'rb') as f:
        line = f.read(30)
        line = struct.unpack('<ccIIIIIIHH',line)
        if line[0] == b'B' and line[1] == b'M':
            print (('%s 是bmp文件,文件大小为%s*%s,颜色数为%s') % (file_name,line[-4],line[-3],line[-1]))
        else:
            print (('%s 不是bmp文件') % file_name)
judgebmp(r'D:\亚信工作\办公规范\VPN\Array SSLVPN Client\WIN\SSLVPNSetup_win64\logo.bmp')
