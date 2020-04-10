import psutil

def killproc(name):
    i = 0
    for proc in psutil.process_iter():
        if proc.name() == name:
            proc.kill()
            i +=1
    return print('killed',i)

#killproc('chromedriver.exe')