from datetime import datetime as dtime
from time import time

def logger_history(st1, st2, st3):
    time = dtime.now().strftime('%d.%m.%y %H:%M')
#    if st3 != "":
#        st3 = "+ " + st3
    with open('calculator.log', 'a', encoding="utf-8") as lf:
        lf.write('{} {} {} {}\n'
                    .format(time, st1, st2, st3))
