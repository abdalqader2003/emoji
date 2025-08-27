import phonenumbers
from phonenumbers import geocoder
import time, random
def start_phone_tracer(target):
    print(f'[+]phoneTracer v2.1 - onsint')
    print(f'[*]Target: {target}')
    print(f'[*]Initiating trace...')
    p = phonenumber.parse(target,None)
    r = geocoder.description_for_number(p)
    print(f'[+] Location: {r}')
    print(f'[+] Trace complete')
start_phone_tracer('+972-921-28196')