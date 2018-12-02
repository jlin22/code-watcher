from stopwatch import Stopwatch
import sys

if __name__ == '__main__':

    # create the stopwatch class to do the work
    sw = Stopwatch()

    # define the messages
    flags_message = '\n'.join(['Please enter a valid flag.', 'Here are a list of the valid flags:',
        '  -b    Begin the stopwatch'])
    start_message = 'The stopwatch has been started.'


    # there is no valid flag
    if len(sys.argv) != 2:
        print(flags_message)
        exit()

    # begin the stopwatch
    if sys.argv[1] == '-b':
        sw.start()

    # end the stopwatch
    if sys.argv[1] == '-e':
        if sw.is_started():
            sw.end()


    
    

