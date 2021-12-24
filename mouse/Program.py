from Teste import AutoClick
from threading import Thread

AutoClick.Start()
p2 = Thread(target = AutoClick.Close)
p1 = Thread(target = AutoClick.AutoClickDef)
p2.start()
p1.start()
