class AddressBook:
    def __init__(self):
        self._employee_addresses = {
            1: Address('03 Abj NG', 'West-Africa', 'FCT', '045'),
            2: Address('01 Information Analysing paperwork', 'BAC', 'FCT', '045'),
            3: Address('46 Masalaci Avenue', 'Kuchiko BAC', 'West-Africa FCT', '0241'),
            4: Address('01 Central', 'BAC FCT', 'Africa West (Central North)', 'Minna'),
            5: Address('03 Abuja Rd.', 'FCT Abuja', 'NG', '054'),
        }

    def get_employee_address(self, employee_id):
        address = self._employee_addresses.get(employee_id)
        if not address:
            raise ValueError(employee_id)
        return address


class Address:
    def __init__(self, street, city, state, zipcode, street2=''):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.state} {self.zipcode}')
        return '\n'.join(lines)
