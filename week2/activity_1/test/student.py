class Student:
    def __init__(self, name, student_id, address, units):
        self.name = name
        self.id = student_id
        self.address = address
        self.units = units

    def get_id(self):
        return self.id

    def _set_id(self, new_id):
        self.id = new_id

    def get_name(self):
        return self.name

    def _set_name(self, new_name):
        self.name = new_name

    def get_address(self):
        return self.address

    def _set_address(self, new_address):
        self.address = new_address

    def get_units_list(self):
        return self.units

    def get_units(self):
        for _ in self.units:
            print(_)

    def _set_units(self, new_units):
        self.units = new_units

