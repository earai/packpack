from dataclasses import dataclass

@dataclass
class CampItem:
    name: str


class RequiredItem(object):

    def __init__(self, camp_item):
        self.camp_item = camp_item

    def get_mass(self):
        #total mass of all dependences
        pass

    def get_deployer(self):
        #does this call a packing algorithm?
        pass

    def get_volume(self):
        pass



    #things like tent, camp stove (this can have variations and added requirements like white gas, matches, whatever)