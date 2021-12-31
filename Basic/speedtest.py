import speedtest  

wifi = speedtest.Speedtest()

option = int(input('''Neyin Hızını Ölçmek İstersiniz? :  

1) Download Hızı

2) Upload Hızı

3) Ping 

seçiminizi yapınız: '''))


if option == 1:  

    print(wifi.download())  

elif option == 2: 

    print(wifi.upload())  

elif option == 3:  

    servernames =[]  

    wifi.get_servers(servernames)  

    print(wifi.results.ping)  

else:

    print("lütfen doğru seçim yapınız !") 