import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
        def test_constructor(self):
            rectangle = Rectangle(5, 10)
            self.assertEqual(rectangle.width, 5)
            self.assertEqual(rectangle.height, 10)
            self.assertEqual(rectangle.x, 0)
            self.assertEqual(rectangle.y, 0)
            self.assertIsNone(rectangle.id)
            
        def test_setters(self):
            rectangle = Rectangle(5, 10)
            rectangle.width = 8
            rectangle.height = 12
            rectangle.x = 2
            rectangle.y = 3
            rectangle.id = 1
            
            self.assertEqual(rectangle.width, 8)
            self.assertEqual(rectangle.height, 12)
            self.assertEqual(rectangle.x, 2)
            self.assertEqual(rectangle.y, 3)
            self.assertEqual(rectangle.id, 1)
            
        def test_getters(self):
            rectangle = Rectangle(5, 10, 2, 3, 1)
            self.assertEqual(rectangle.get_width(), 5)
            self.assertEqual(rectangle.get_height(), 10)
            self.assertEqual(rectangle.get_x(), 2)
            self.assertEqual(rectangle.get_y(), 3)
            self.assertEqual(rectangle.get_id(), 1)
            
        if __name__ == '__main__':
            unittest.main()
                                                                                                                                                                                                                            
