import ctypes

def resolucion():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    res=int
    if ancho==3840 and alto==2160:
        res=0
    if ancho==1920 and alto==1080:
        res=1
    if ancho==1680 and alto==1050:
        res=2
    if ancho==1600:
        if alto==1024:
            res=3
        else:
            res=4
    if ancho==1440:
        if alto==1080:
            res=5
        else:
            res=6
    if ancho==1366 and alto==768:
        res=7
    if ancho==1360 and alto==768:
        res=8
    if ancho==1280:
        if alto==1024:
            res=9
        if alto==960:
            res=10
        if alto==800:
            res=11
        if alto==768:
            res=12
        if alto==720:
            res=13
    if ancho==1176 and alto==664:
        res=14
    if ancho==1152 and alto==864:
        res=15
    if ancho==1024 and alto==768:
       res=16
    if ancho==800 and alto==600:
        res=17
    return res