from time import sleep
import datetime

def outer(funk):
    def inter(*args,**kwargs):
        start = datetime.datetime.now()
        funk()
        finish = datetime.datetime.now()
        return finish - start
    return inter()

@outer
def funkt():
    sleep(5)

print(funkt)