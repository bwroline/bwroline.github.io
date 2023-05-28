from productivity import ProductivitySystem
from hr import PayrollSystem
from contacts import AddressBook


class EmployeeDatabase:
    def __init__(self):
        self._employees = [
            {
                'id': 1,
                'name': 'Dakoyi Clinton',
                'role': 'manager',
                # 'profession': 'Websites application programming'
            },
            {
                'id': 2,
                'name': 'Ndakoyi Afaga Juliet',
                'role': 'secretary',
                # 'profession': ''
            },
            {
                'id': 3,
                'name': 'Yahaya I Joyce',
                'role': 'sales',
                # 'profession': ''
            },
            {
                'id': 4,
                'name': 'Pros-o-line',
                'role': 'factory',
                # 'profession': ''
            },
            {
                'id': 5,
                'name': 'Fidelia D Clinton',
                'role': 'secretary',
                # 'profession': ''
            },
        ]
        self.productivity = ProductivitySystem()
        self.payroll = PayrollSystem()
        self.employee_addresses = AddressBook()

    @property
    def employees(self):
        return [self._create_employee(**data) for data in self._employees]

    def _create_employee(self, id, name, role):
        address = self.employee_addresses.get_employee_address(id)
        employee_role = self.productivity.get_role(role)
        payroll_policy = self.payroll.get_policy(id)
        return Employee(id, name, address, employee_role, payroll_policy)


class Employee:
    def __init__(self, id, name, address, role, payroll):
        self.id = id
        self.name = name
        self.address = address
        self.role = role
        self.payroll = payroll

    def work(self, hours):
        duties = self.role.perform_duties(hours)
        print(f'Employee {self.id} - {self.name}:')
        print(f'- {duties}')
        print('')
        self.payroll.track_work(hours)

    def calculate_payroll(self):
        return self.payroll.calculate_payroll()
