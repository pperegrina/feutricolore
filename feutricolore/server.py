import wiringpi
import time
import pathlib
import syslog
import sequences

RELAY_J5 = 37
RELAY_J4 = 31
RELAY_J3 = 15
RELAY_J2 = 7

wiringpi.wiringPiSetupPhys()
wiringpi.pinMode(RELAY_J5,1)
wiringpi.pinMode(RELAY_J4,1)
wiringpi.pinMode(RELAY_J3,1)
wiringpi.pinMode(RELAY_J2,1)

wiringpi.digitalWrite(RELAY_J5,0)
wiringpi.digitalWrite(RELAY_J4,0)
wiringpi.digitalWrite(RELAY_J3,0)
wiringpi.digitalWrite(RELAY_J2,0)

syslog.openlog(logoption=syslog.LOG_PID, facility=syslog.LOG_DAEMON)
syslog.syslog(syslog.LOG_INFO, 'Feutricolore server started')

current_sequence = 1
file_t = 0
try:
    fname = pathlib.Path('/data/sequence_id.txt')
    file_t = fname.stat().st_mtime
    f = open('/data/sequence_id.txt','r')
    current_sequence = int(f.read())
    f.close()
except:
    pass

reset = True
seq_index = 0
next_t = 0
blink_t = 0
blink_state = True

while True:

    try:
        fname = pathlib.Path('/data/sequence_id.txt')
        t = fname.stat().st_mtime
        if t > file_t: 
            file_t = t
            f = open('/data/sequence_id.txt','r')
            current_sequence = int(f.read())
            f.close()
            reset = True
    except:
        pass

    seq = sequences.SEQUENCES[current_sequence]
    now = time.time()

    state_change = False
    
    if reset:
        msg = 'switching to %s sequence' % seq['name']
        syslog.syslog(syslog.LOG_INFO, 'Feutricolore %s' % msg)
        print(msg)
        seq_index = 0
        if seq['data'][seq_index][1] != -1:
            next_t = now + seq['data'][seq_index][1]
        else:
            next_t = -1
        blink_t = now + 1
        blink_state = True
        reset = False
        state_change = True

    elif next_t != -1:
        if now > next_t:
            seq_index = seq_index + 1
            if seq_index == len(seq['data']):
                seq_index = 0
            if seq['data'][seq_index][1] != -1:
                next_t = now + seq['data'][seq_index][1]
            else:
                next_t = -1
            state_change = True

    values = seq['data'][seq_index][0]

    if now > blink_t:
        blink_t = now + 1
        blink_state = not blink_state
        if 'G' in values or 'Y' in values or 'R' in values:
            state_change = True

    if state_change:

        msg = ''

        if 'g' in values:
            wiringpi.digitalWrite(RELAY_J2,1)
            msg = msg + 'G'
        elif 'G' in values:
            g = blink_state and 1 or 0
            wiringpi.digitalWrite(RELAY_J2,g)
            if g:
                msg = msg + 'G'
        else:
            wiringpi.digitalWrite(RELAY_J2,0)

        if 'y' in values:
            wiringpi.digitalWrite(RELAY_J3,1)
            msg = msg + 'Y'
        elif 'Y' in values:
            y = blink_state and 1 or 0
            wiringpi.digitalWrite(RELAY_J3,y)
            if y:
                msg = msg + 'Y'        
        else:
            wiringpi.digitalWrite(RELAY_J3,0)

        if 'r' in values:
            wiringpi.digitalWrite(RELAY_J4,1)
            msg = msg + 'R'
        elif 'R' in values:
            r = blink_state and 1 or 0
            wiringpi.digitalWrite(RELAY_J4,r)
            if r:
                msg = msg + 'R'
        else:
            wiringpi.digitalWrite(RELAY_J4,0)            

        print(msg)

    time.sleep(0.25)

