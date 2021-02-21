SEQUENCES = {
    0: {
        'name': 'off',
        'data': [('',-1)]
    },        
    1: {
        'name': 'standard',
        'data': [('g',15), ('y',3), ('r',15)]
    },
    2: {
        'name': 'yellow blink',
        'data': [('Y',-1),]
    },
    3: {
        'name': 'green blink',
        'data': [('G',-1),]
    },
    4: {
        'name': 'red blink',
        'data': [('R',-1),]
    },    
    5: {
        'name': 'green/yellow/red chaser',
        'data': [('g',3), ('y',3), ('r',3)]
    },
    6: {
        'name': 'green/yellow/red/yellow/green chaser',
        'data': [('g',3), ('y',3), ('r',3), ('y',3)]
    },    
    7: {
        'name': 'red/yellow/green chaser',
        'data': [('r',3), ('y',3), ('g',3)]
    },
    8: {
        'name': 'fast green/yellow/red/yellow/green chaser',
        'data': [('g',0.5), ('y',0.5), ('r',0.5), ('y',0.5)]
    },
    9: {
        'name': 'all blink',
        'data': [('GYR',-1),]
    },    
}
