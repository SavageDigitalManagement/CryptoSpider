from cryptospider import *
#Shows Information from Queen Cryptling
Cryptling_Web = CryptlingWeb
target = threading.Thread(target=cryptling.calculate_value)
graph = threading.Thread(target=Cryptling_Web.show_graph)
target.start()
graph.start()
