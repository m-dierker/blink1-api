from django.http import HttpResponse
from blink import Blink

def process_command(request, cmd):
    # Must be an absolute path (ex: no ~/bin/)

    blink = Blink()

    # Map these directly to --<string> with no interference. Ex: on should map to --on
    direct_map = ['on', 'off', 'red', 'blue', 'green']

    if cmd == 'random' and 'numtimes' in request.GET:
        blink.random(request.GET['numtimes'])
    elif cmd == 'rgb' and 'r' in request.GET and 'g' in request.GET and 'b' in request.GET:
        blink.rgb(request.GET['r'], request.GET['g'], request.GET['b'])
    elif cmd in direct_map:
        blink.cmd('--' + cmd)
    else:
        return HttpResponse('Invalid Command')

    return HttpResponse(0)
