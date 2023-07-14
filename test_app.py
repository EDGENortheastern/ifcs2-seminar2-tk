import unittest
from app_tree import Application

class TestValidateName(unittest.TestCase):

    def test_validate_name(self):
        app = Application()
        self.assertTrue(app.validate_name("John Doe"))
        self.assertFalse(app.validate_name("John Doe2"))

    def test_validate_name_again(self):
        app = Application()
        self.assertTrue(app.validate_name("86587686"))

if __name__ == "__main__":
    unittest.main()
