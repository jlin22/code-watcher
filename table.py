class Table:
    ''' Table interacts with csv files ''' 
    ''' Design Choice: Use a list of lists '''
    ''' Invariant: The list is already sorted '''

    def read_csv(self, f):
        with open(f) as file_object:
            data = file_object.readlines()
            self.content = {}
            for i in range(len(data)):
                data[i] = data[i].strip('\n').split(', ') 
                # add 0s to beginning of month and day if its one char long
                for j in range(1, 3):
                    if len(data[i][j]) == 1:
                        data[i][j] = '0'+data[i][j]
                for j in range(1+6, 3+6):
                    if len(data[i][j]) == 1:
                        data[i][j] = '0'+data[i][j]
                # separate by days
                if i != 0:
                    try:
                        self.content['-'.join(data[i][:3])].append(data[i][3:])
                    except:
                        self.content['-'.join(data[i][:3])] = [data[i][3:]]
        return self.content
    
    def time_spent(self, date, entry):

        # calculate the differences between the intervals of time
        # [year, month, day, hour, minute, seconds]
        list_date = date.split('-')
        differences = []
        for i in range(3, 6):
            print(i - 3)
            differences.append(int(entry[i]) - int(list_date[i - 3]))
        for i in range(0, 3):
            differences.append(int(entry[i + 6]) - int(entry[i]))
        return differences

    def time_elapsed(self, differences):
        # [year, month, day, hour, minute, seconds] -> time as string
        # time: _ years, _ months, _ days, _ minutes, _ seconds
        
        # if seconds is negative, add 60 seconds, subtract 1 minute
        if differences[5] < 0: 
            differences[5] += 60
            differences[4] -= 1

        # if minutes is negative, subtract 60 minutes and add 1 hour
        if differences[4] < 0:
            differences[4] -= 60
            differences[3] += 1
        # if hours is negative, add 24 hours and subtract 1 day 
        if differences[3] < 0:
            differences[3] += 24
            differences[2] -= 1

        # if days is negative, add number of days in the month and subtract 1 month
        if differences[2] < 0:
            differences[1] -= 1
            differences[2] += 30

        # if months is negative, subtract 1 year and add 12 months
        if differences[1] < 0:
            differences[1] += 12
            differences[0] -= 1
        
        # create a list that represents the string
        lens_of_time = ['year', 'month', 'day', 'hour', 'minute', 'second']
        for i in range(len(lens_of_time)):
            lens_of_time[i] = str(differences[i]) + " " + lens_of_time[i] 
            if differences[i] != 1:
                lens_of_time[i] += 's'

        final_str = []
        for e in lens_of_time:
            if e[0] != '0':
                final_str.append(e)

        return ' '.join(final_str)

    def search_day(self, date):
        ''' Searches for all entries with date
        date is of the form: 'yyyy-mm-dd' 
        print it nicely'''
        # our string with nice formatting
        s = ''
        s += 'Time spent coding on '
        s += date

        '''
        print(self.content[date])
        print(date)
        print(self.time_spent(date, self.content[date][0]))
        '''
        return s



if __name__ == '__main__':
    t = Table()
    t.read_csv('progress.csv')
#    print('read csv:' ,  t.read_csv('progress.csv'))
    print(t.search_day('2018-12-01'))

    # testing time_elapsed
    print(t.time_elapsed([0, 0, 0, 1, 1, 1]))
    



