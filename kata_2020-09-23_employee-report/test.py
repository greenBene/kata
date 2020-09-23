import unittest
from report import get_adult_employees


employees = [
  { 'name': 'Max', 'age': 17 },
  { 'name': 'Sepp', 'age': 18 },
  { 'name': 'Nina', 'age': 15 },
  { 'name': 'Mike', 'age': 51 },
]

class TestEmpolyeeReport(unittest.TestCase):

    def test_story_one(self):
        adult_employees = get_adult_employees(employees)

        self.assertTrue(all([a['age'] >= 18 for a in adult_employees]))
        self.assertTrue(len(adult_employees) == 2)

    def test_story_two(self):
        adult_employees = get_adult_employees(employees)
        adult_employees_sorted = sorted(adult_employees, key = lambda i: i['name'], reverse = True)

        self.assertEqual(adult_employees, adult_employees_sorted)

    def test_story_three(self):
        adult_employees = get_adult_employees(employees)

        for employee in adult_employees:
            self.assertEqual(employee['name'], employee['name'].upper())



if __name__ == '__main__':
    unittest.main()
