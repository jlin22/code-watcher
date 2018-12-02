from stopwatch import Stopwatch
import sys

if __name__ == '__main__':

    # create the stopwatch class to do the work
    sw = Stopwatch()

    # define the messages
    flags_message = '\n'.join(['Please enter a valid flag.', 'Here are a list of the valid flags:',
        '  -b    Begin the stopwatch', '  -e    End the stopwatch'])
    start_message = 'The stopwatch has been started.'
    end_message = 'The stopwatch has been ended and data has been logged'
    not_started_message = 'The stopwatch has not been started yet'

    # there is no valid flag
    if len(sys.argv) != 2:
        print(flags_message)

    # begin the stopwatch
    elif sys.argv[1] == '-b' or sys.argv[1] == '-s':
        sw.start()

    # end the stopwatch
    elif sys.argv[1] == '-e':
        if sw.is_started():
            sw.end()
        else:
            print(not_started_message)

    else:
        print(flags_message)




    
    

