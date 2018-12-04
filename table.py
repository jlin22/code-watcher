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
            print('-'.join(data[1][:3])) 
        return self.content
    
    def time_spent(self, date, entry):

        # calculate the differences between the intervals of time
        # [year, month, day, hour, minute, day]
        list_date = date.split('-')
        differences = []
        for i in range(3, 6):
            print(i - 3)
            differences.append(int(entry[i]) - int(list_date[i - 3]))
        for i in range(0, 3):
            differences.append(int(entry[i + 6]) - int(entry[i]))
        return differences

    def search_day(self, date):
        ''' Searches for all entries with date
        date is of the form: 'yyyy-mm-dd' '''
        print(self.content[date])
        print(date)
        print(self.time_spent(date, self.content[date][0]))
        '''
        except:
            print('That date is not in the data')
            '''



if __name__ == '__main__':
    t = Table()
    print(t.read_csv('progress.csv'))
    print(t.search_day('2018-12-01'))
    



