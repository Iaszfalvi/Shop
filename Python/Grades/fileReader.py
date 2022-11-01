from pathlib import Path

class Reader(object):

    def readFile(self, filename):
        
        #Filepath        
        self.myfile = Path(__file__).with_name(filename)
        self.results = []

        # Read a file and return word count
        with open(filename) as f:

            for line in f.readlines():    
                self.results.append(line.split())

        return self.results