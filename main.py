import eel
from whois import whois

@eel.expose
def get_whois(zone):
    print(f"Whois {zone}")
    w = whois(zone)
    w_str = '\n'.join([f"{k}:\t{v}" for k, v in w.items()])
    print(w_str)
    return w_str


eel.init('web')
eel.start('slide.html')
