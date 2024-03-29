import unittest
from models.base import Base

class TestBase(unittest.TestCase):
        def test_constructor_with_id(self):
            base = Base(1)
            self.assertEqual(base.id, 1)
            
        def test_constructor_without_id(self):
            base1 = Base()
            base2 = Base()
            self.assertEqual(base1.id, 1)
            self.assertEqual(base2.id, 2)
            
        if __name__ == '__main__':
            unittest.main()
                                                                            
