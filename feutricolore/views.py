from django.http import HttpResponse
from django.template import loader
from . import sequences

def render(context, request):
    seq = dict(sequences.SEQUENCES) 
    for k in seq:
        seq[k]['info'] = []
        for data in seq[k]['data']:
            info = {
                't': 'forever',
                'green' : False,
                'green_blink': False,
                'yellow': False,
                'yellow_blink': False,
                'red': False,
                'red_blink': False,
            }
            values = data[0]
            t = data[1]
            if t != -1:
                info['t'] = '%s s'%t
            if 'g' in values:
                info['green'] = True
            elif 'G' in values:
                 info['green'] = True
                 info['green_blink'] = True
            if 'y' in values:
                info['yellow'] = True
            elif 'Y' in values:
                 info['yellow'] = True
                 info['yellow_blink'] = True
            if 'r' in values:
                info['red'] = True
            elif 'R' in values:
                 info['red'] = True
                 info['red_blink'] = True                 
            seq[k]['info'].append(info)
    template = loader.get_template('feutricolore/index.html')
    context['sequences'] = seq
    return HttpResponse(template.render(context, request))

def index(request):
    context = { 
        'selected_mode': 'unknown',
    }
    try:
        f = open('/data/sequence_id.txt','r')
        sequence_id = int(f.read())
        f.close()
        if sequence_id in sequences.SEQUENCES:
            context['selected_mode'] = '%d - %s' % (sequence_id, sequences.SEQUENCES[sequence_id]['name'])
    except:
        pass    
    return render(context, request)

def set_sequence(request, sequence_id):
    context = {
        'selected_mode': 'unknown',
    }    
    if sequence_id in sequences.SEQUENCES:
        context['selected_mode'] = '%d - %s' % (sequence_id, sequences.SEQUENCES[sequence_id]['name'])
        f = open('/data/sequence_id.txt','w')
        f.write(str(sequence_id))
        f.flush()
        f.close()
    return render(context, request)


