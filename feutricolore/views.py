from django.http import HttpResponse
from django.template import loader
import wiringpi
import time
from . import modes

RELAY_J5 = 37
RELAY_J4 = 31
RELAY_J3 = 15
RELAY_J2 = 7

wiringpi.wiringPiSetupPhys()
wiringpi.pinMode(RELAY_J5,1)
wiringpi.pinMode(RELAY_J4,1)
wiringpi.pinMode(RELAY_J3,1)
wiringpi.pinMode(RELAY_J2,1)

def J2():
    wiringpi.digitalWrite(RELAY_J2,1)
    time.sleep(0.25)
    wiringpi.digitalWrite(RELAY_J2,0)
    time.sleep(0.25)    

def J3():
    wiringpi.digitalWrite(RELAY_J3,1)
    time.sleep(0.25)
    wiringpi.digitalWrite(RELAY_J3,0)
    time.sleep(0.25)

def render(context, request):
    template = loader.get_template('feutricolore/index.html')
    context['modes'] = modes.MODES
    return HttpResponse(template.render(context, request))

def index(request):
    context = { 
        'selected_mode': 'unknown',
    }
    return render(context, request)

def set_mode(request, mode_id):
    context = {
        'selected_mode': 'unknown',
    }    
    for mode in modes.MODES:
        if mode_id == mode['id']:
            context['selected_mode'] = '%d - %s' % (mode['id'], mode['description'])
            J2()
            time.sleep(0.75)
            cpt=1
            while cpt<mode_id:
                J3()
                cpt+=1
            break
    return render(context, request)

