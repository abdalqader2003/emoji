import speedtest
from pystyle import *

print(Box.Lines('[+] speed tests'))
Write.Print('[-] speed tests \n ',Colors.purple_to_red, interval=0.1)
print(Box.Lines("<Program test>"))

st = speedtest.Speedtest()
dst = st.download()
d   = round(dst/ (10**6),2)
ust = st.upload()
u   = round(ust / (10**6),2)
Write.Print('[-] net speed is : \n', Colors.green,interval=0.1)
print('Your Download speed is : ', d , 'MB')
print('Your Download speed is : ', u , 'MB')
input('\n press any key to exit')