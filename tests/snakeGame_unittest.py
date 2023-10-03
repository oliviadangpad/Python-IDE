from src.snakeGame import SnakeGame    # The code to test
import unittest

class Test_SnakeGame(unittest.TestCase):
    def test_move(self):
        obj = SnakeGame(3,2,[[1,2],[0,1]])
        param_1 = obj.move("R")
        self.assertEqual(param_1, 0)
        self.assertNotEqual(param_1, 3)

if __name__ == '__main__':
    unittest.main()

# https://docs.python.org/3/library/unittest.html#assert-methods
