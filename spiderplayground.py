from cryptospider import *
import threading
#Starts Crawling on CryptoWeb
#Shows information from the Crypto Web Class
cryptling = CryptoSpider()
Cryptling_Web = CryptlingWeb()
web_ground = threading.Thread(target=cryptling.start_web)
web_ground.start()
XMR_Crawler = threading.Thread(target=cryptling.get_XMR_position)
XMR_Crawler.start()
XMR_Web = threading.Thread(target=Cryptling_Web.show_graph_XMR)
XMR_Web.start()
