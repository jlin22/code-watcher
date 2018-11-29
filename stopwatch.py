import time
''' Using functions time and sleep (for testing) '''

class Stopwatch:
    def __init__(self):
        ''' Sets time elapsed to 0'''
        self.elapsed = 0

    def start(self):
        ''' Starts the timer '''
        self.beg = time.time()

    def end(self):
        ''' Ends the timer and adds time to elapsed '''
        # in case someone calls end twice
        if self.beg:
            self.elapsed += time.time() - self.beg
            self.beg = False

    def reset(self):
        ''' Resets the counter of time '''
        self.elapsed = 0


if __name__ == '__main__':
    sw = Stopwatch()
    
    # testing passing 1 second of time
    sw.start()
    time.sleep(1)
    sw.end()
    print(sw.elapsed)

    # testing that calling end does nothing
    sw.end()
    print(sw.elapsed)

    # adding another interval
    sw.start()
    time.sleep(0.45)
    sw.end()
    print(sw.elapsed)

    # reset
    sw.reset()
    print(sw.elapsed)


