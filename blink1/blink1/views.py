from django.http import HttpResponse
import subprocess

def process_command(request, cmd):
    # Must be an absolute path (ex: no ~/bin/)
    params = ['/Users/Matthew/bin/blink1-tool']

    # Map these directly to --<string> with no interference. Ex: on should map to --on
    direct_map = ['on', 'off', 'red', 'blue', 'green']

    if cmd == 'random' and 'numtimes' in request.GET:
        params.append('--random')
        params.append(request.GET['numtimes'])
    elif cmd in direct_map:
        params.append('--' + cmd)
    else:
        return HttpResponse('Invalid Command')

    print 'Executing ' + str(params)

    # Process the command
    output = subprocess.call(params)

    return HttpResponse(output)
