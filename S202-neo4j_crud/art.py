class Art(object):

    def __init__(self,name,year,last_inspection,artist):
        self.name = name
        self.year = year
        self.last_inspection = last_inspection
        self.artist
    

class Sculpture(Art):

    def __init__(self,name,year,last_inspection,artist,material):
        super.__init__(name,year,last_inspection,artist)
        self.material = material

class Paiting(Art):

    def __init__(self,name,year,last_inspection,artist,technic):
        super.__init__(name,year,last_inspection,artist)
        self.technic = technic
