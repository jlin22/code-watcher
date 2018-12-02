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
            today = datetime.today()
            s['cur_time'] = [str(today.year), str(today.month), str(today.day), 
                    str(today.hour), str(today.minute), str(today.second)]

    def is_started(self):
        ''' Check if the stopwatch was started '''
        with shelve.open('.data') as s:
            return s['beg']
    def end(self):
        ''' Ends the timer and writes the data '''
        with shelve.open('.data') as s:
            # check if beginning is valid (i.e. not 0)
            if s['beg']:
                exists = True
                if not os.path.exists('progress.csv'):
                    exists = False

                # add the data_entry to progress.csv
                with open('progress.csv', 'a') as fo:
                    # add a beginning column if progress.csv doesn't exist
                    if not exists:
                        measures_of_time = ['year', 'month', 'day', 'hour', 'minute', 'second']
                        beg_time = list(map(lambda x: 'beg_' + x, measures_of_time))
                        end_time = list(map(lambda x: 'end_' + x, measures_of_time))
                        indices = ', '.join(beg_time) + ', '.join(end_time) + '\n'
                        fo.write(indices)

                    today = datetime.today()
                    end_time = [str(today.year), str(today.month), str(today.day), 
                            str(today.hour), str(today.minute), str(today.second)]
                    data_entry = ''
                    for e in s['cur_time']:
                        data_entry += e + ', '
                    for i in range(len(end_time)):
                        data_entry += end_time[i]
                        if i != len(end_time) - 1: data_entry += ", "
                        else: data_entry += "\n"
                    fo.write(data_entry) 
                    s['beg'] = 0
                    s['cur_time'] = 0
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
        # does is_started work?
        print('is started:', sw.is_started())
        sw.start()
        print('is started:', sw.is_started())
        time.sleep(2)
        sw.end()
        # did it actually write it?
        with open('progress.csv') as f:
            lines = f.read()
        print(lines)
        os.unlink('progress.csv')

    elif sys.argv[1] == '-c': # create a test file for today
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
