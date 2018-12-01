import os
import sys
import shelve
import time
from datetime import date
from datetime import datetime

''' Using functions time and sleep (for testing) '''

class Stopwatch:

    def start(self):
        ''' Begins the timer '''
        with shelve.open('.data') as s:
            s['beg'] = time.time()

    def end(self):
        ''' Ends the timer and writes the data '''
        with shelve.open('.data') as s:
            # check if beginning is valid (i.e. not 0)
            if s['beg']:
                with open('progress.csv', 'a') as fo:
                    today = datetime.today()
                    fo.write(', '.join([str(today.year), str(today.month), str(today.day), 
                        str(s['beg']), str(time.time())]) + "\n")
                    s['beg'] = 0
            else: 
                raise Exception('You pressed end twice in a row')

            
if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception('Please pass a flag')
    elif sys.argv[1] == '-t': #test if stopwatch works
        sw = Stopwatch()

        sw.start()
        time.sleep(1)
        sw.end()
        sw.start()
        time.sleep(2)
        sw.end()
        with open('progress.csv') as f:
            lines = f.read()
        print(lines)
        os.unlink('progress.csv')

    elif sys.argv[1] == '-c': # create a test file
        sw = Stopwatch()

        sw.start()
        time.sleep(0.1)
        sw.end()
        sw.start()
        time.sleep(0.0001)
        sw.end()
        sw.start()
        time.sleep(0.25)

    elif sys.argv[1] == '-d': # delete the progress file
        try:
            os.unlink('progress.csv')
        except:
            raise Exception("File progress.csv doesn't exist")

    else: 
        raise Exception('Please pass a valid flag')
