import time

class Stopwatch:
    def __init__():
        ''' Sets time elapsed to 0'''
        self.elapsed = 0

    def start():
        ''' Starts the timer '''
        self.start = time.time()

    def end():
        ''' Ends the timer and adds time to elapsed '''
        # in case someone calls end twice
        if self.start:
            self.elapsed += time.time() - self.start
            self.start = False

