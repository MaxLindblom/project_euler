# Helper class to write results to file

import fileinput

def update_results(content, n):
    updated = False
    for line in fileinput.input('results.txt', inplace=True):
        if line.startswith('ID {}'.format(n)):
            print('ID {}: {}'.format(n, content), end='\n')
            updated = True
        else:
            print(line, end='')
    if not updated:
        with open('results.txt', 'a') as result:
            result.write('ID {}: {}\n'.format(n, content))
        print('Added result for ID {}: {}'.format(n, content))
    else: 
        print('Replaced result for ID {}: {}'.format(n, content))