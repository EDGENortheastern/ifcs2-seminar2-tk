import unittest
from app_tree import Application

class TestValidateName(unittest.TestCase):
    
    def test_validate_name(self):
        app = Application()
        self.assertTrue(app.validate_name("John Doe"))
        self.assertFalse(app.validate_name("John Doe2"))

if __name__ == "__main__":
    unittest.main()
