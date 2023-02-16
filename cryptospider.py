import time
from datetime import datetime
import random
import krakenex
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import threading
import sqlite3


x_vals = []
y_vals = []

class CryptoSpider:
    xmr_x = []
    xmr_y = []
    xmr_plot_x = []
    xmr_i = 0
    def __init__(self):
        self.xone = 0
        self.yone = 0
        self.i = 0
        self.coordslist = [0]
        self.second_ago = []
        self.k = krakenex.API()
        self.x_vals = []
        self.y_vals = []
        self.slope = []
        self.conn = sqlite3.connect('cryptlingnest.db')
        self.cursor = self.conn.cursor()
    def get_now_time(self):
        n = time.time()
        time_format = time.strftime('%H:%M:%S', time.gmtime(n))
        return time_format

    def crawl(self):
        while True:
            x_vals.append(cryptling.get_bitcoin_position())
            y_vals.append(cryptling.yone)
            time.sleep(1)

    def get_bitcoin_position(self):
        try:
            self.ticker_info = self.k.query_public('Ticker', {'pair':'XBTUSD'})
            self.position = self.ticker_info['result']['XXBTZUSD']['a'][0]
            return float(self.position)
        except Exception as e:
            print(f'Request Failed: {e}')


    def get_eth_position(self):
        try:
            self.ticker_info = self.k.query_public('Ticker', {'pair':'ETHUSD'})
            self.position = self.ticker_info['result']['XETHZUSD']['a'][0]
            return float(self.position)
        except Exception as e:
            print(f'Request Failed: {e}')


    def get_Litecoin_position(self):
        try:
            self.ticker_info = self.k.query_public('Ticker', {'pair':'XLTCZUSD'})
            self.position = self.ticker_info['result']['XLTCZUSD']['a'][0]
            return float(self.position)
        except Exception as e:
            print(f'Request Failed: {e}')

    def get_XMR_position(self):
        name = 'XMR Crawler'
        while True:
            print(f'{name}')
            self.xmr_query = self.ticker_info = self.k.query_public('Ticker', {'pair':'XXMRZUSD'})
            self.xmr_data = float(self.ticker_info['result']['XXMRZUSD']['a'][0])
            self.xmr_y.append(self.xmr_data)
            self.xmr_x.append(self.get_now_time())
            print(f'XMR Value: {self.xmr_data} Time: {self.get_now_time()}')
            if len(y_vals) > 2:
                print(f'{name}: Current Value: {self.xmr_y[-1]} {self.xmr_x[-1]} Second Ago: {self.xmr_y[-2]} {self.xmr_x[-2]}')
                print(f'{name}: Average Value: {sum(self.xmr_y)/len(self.xmr_y)}')
            self.xmr_i += 1
            self.xmr_plot_x.append(self.xmr_i)
            time.sleep(1)




    
    def calculate_value(self):
        while True:
            name='Queen Cryptling'
            print(name)
            iminusone = self.i-1
            now_time = self.get_now_time()
            #print(f'X:{self.xone} Y:{self.yone}')
            self.second_ago.append(self.get_now_time())
            if len(self.second_ago)> 1:
                pass
                #print(f'Second one: Time Now: {self.get_now_time()} {self.second_ago[iminusone]}')
                #print(f'Now Position: {self.coordslist[self.i]}')
            self.coordslist.append((float(self.get_bitcoin_position()),now_time))
            print(f'Coords List: {self.coordslist}')
            self.xone+=1
            self.yone+=1
            self.i+=1
            print(f'{name} Second Ago: {self.coordslist[iminusone]}')
            #print(iminusone)
            time.sleep(1)

    def get_ticker_pos(self):
        return self.position
    
    def start_web(self):
        while True:
            name ='Crypto Web:'
            iminusone = self.i-1            
            print(self.i)
            print(name)

            intConinPosition= float(self.get_bitcoin_position())
            #now_pos = self.coordslist[self.i]
            #second_ago = self.coordslist[self.i-1]
            print(f'{name} Current Average Value: {CryptlingWeb.sum_coin()}')
            if len(x_vals)>2:
                deltay = x_vals[-1]-x_vals[-2]
                deltax = y_vals[-1]-y_vals[-2] + .01
                slope = deltay/deltax
                print(f'{name} Slope: {slope}')
                if slope != 0:
                    self.slope.append(slope)
                    print(f'Slope List: {self.slope}')
                    if len(self.slope)>2:
                        average_slope = sum(self.slope)/len(self.slope)
                        print(f'Average Slope: {average_slope}')
                        dealtas = self.slope[-1]-self.slope[-2]
                        deltat = deltax
                        slope_roc = dealtas/deltat

                        print(f'Slope Average Rate of Change: {slope_roc}')


                print(f'{name} Cryptling: Now: {x_vals[-1]}, Second Ago: {x_vals[-2]}')
            current_average_value = [CryptlingWeb.sum_coin()]
            self.i+=1
            #print(self.i)
            #print(f'Difference Average from Current: {intConinPosition-current_average_value[0]}')
            time.sleep(1)



cryptling = CryptoSpider()
crawl = threading.Thread(target=cryptling.crawl)
crawl.start()


def animate(i):
    #x_vals.append(cryptling.get_bitcoin_position())
    #y_vals.append(cryptling.yone)
    plt.plot(y_vals,x_vals)

def animate_XMR(i):
    plt.plot(cryptling.xmr_plot_x,cryptling.xmr_y)

class CryptlingWeb:
    #This class contains math functions to be performed on the data
    #Obtained from the CryptoSpider instance
    def sum_coin():
        coin_value = []
    
        if x_vals != []:
            for value in x_vals:
                if value != 0:
                    coin_value.append(x_vals[cryptling.i])
        #print(cryptling.coordslist[cryptling.i])
            if coin_value != []:
                return sum(coin_value)/len(coin_value)
#class CryptoGraphWeb:
    def show_graph_XMR(self):
        ani = FuncAnimation(plt.gcf(),animate_XMR,interval=1000)
        plt.tight_layout()
        graph= threading.Thread(target=plt.show())

    def show_graph():
        ani = FuncAnimation(plt.gcf(),animate,interval=1000)
        plt.tight_layout()
        graph= threading.Thread(target=plt.show())



class CryptoWeb:
    def start_web(self):
        while True:
            global cryptling
            name ='Crypto Web:'
            print(name)
            intConinPosition= cryptling.get_bitcoin_position()
            now_pos = cryptling.coordslist[cryptling.i]
            second_ago = cryptling.coordslist[cryptling.i-1]
            print(f'{name} Slope: {x_vals}')
            print(f'{name} Current Average Value: {CryptlingWeb.sum_coin()}')
            print(f'{name} Cryptling: Now: {now_pos}, Second Ago: {second_ago}')
            current_average_value = [CryptlingWeb.sum_coin()]

            print(f'Difference Average from Current: {intConinPosition-current_average_value[0]}')
            time.sleep(1)

#cryptoWeb = CryptoWeb()
#threading.Thread(cryptoWeb.start_web())
    #position = cryptling.get_bitcon_position()
    #print(position)
    #print(float(position['result']['XXBTZUSD']['a'][0]))