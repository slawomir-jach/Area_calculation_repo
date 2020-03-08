class Tools:

    def __init__(self, inputlist):
        self.inputlist = inputlist

    def find_highest_number(self):
        # Finding highest number in the list
        highest_number = max(self.inputlist)
        return highest_number

    def find_position_highest_number(self):
        # Finding position of highest number in the list
        findposition = self.inputlist.index(Tools.find_highest_number(self))
        return findposition

    def find_double(self):
        # Check is highest number double
        how_many_highest = self.inputlist.count(Tools.find_highest_number(self))
        if how_many_highest == 1:
            return False
        else:
            if how_many_highest > 1:
                return True

    def list_duplicates_position(self):
        start_at = -1
        dest_list = []
        while True:
            try:

                location = self.inputlist.index(self.find_highest_number(), start_at + 1)
                print(location)
            except ValueError:
                break
            else:
                dest_list.append(location)
                start_at = location
        return dest_list


x = [2,4,7,8,9,8,9]

instance = Tools(x)
print(instance.find_highest_number())
print(instance.find_position_highest_number())
print(instance.find_double())
print(instance.list_duplicates_position())
