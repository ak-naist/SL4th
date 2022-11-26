import unittest
from speciallecture.CSVPrinter import CSVPrinter

class TestCSVPrinter(unittest.TestCase):
    def test_read1(self):
        printer = CSVPrinter("sample.csv")
        print(printer)
        l = printer.read()
        self.assertEqual(3, len(l))

    def test_read2(self):
        printer = CSVPrinter("sample.csv")
        l = printer.read()
        self.assertEqual(['value1A', 'value1B', 'value1C'], l[0])
        self.assertEqual(['value2A', 'value2B', 'value2C'], l[1])
        self.assertEqual(['value3A', 'value3B', 'value3C'], l[2])

    def test_read3(self):
        try:
            printer = CSVPrinter("noexist.csv")
            printer.read()
            unittest.TestCase.fail("Normal exe")
        except FileNotFoundError as e:
            print(e)

if __name__ == "__main__":
    unittest.main()

