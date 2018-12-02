class Table:
    ''' Table interacts with csv files ''' 
    ''' Design Choice: Use a list of lists '''

    def read_csv(self, f):
        with open(f) as file_object:
            self.data = file_object.readlines()
            for i in range(len(self.data)):
                self.data[i] = self.data[i].strip('\n').split(', ') 
        return self.data

if __name__ == '__main__':
    t = Table()
    print(t.read_csv('progress.csv'))



