import unittest
from controller import OptionsParser

class TestController(unittest.TestCase):
    def test_pars(self):
        a=OptionsParser.parse("fbr")
        self.assertEqual(str(a), '[<MoveDirection.FORWARD: 1>, <MoveDirection.BACKWARD: 2>, <MoveDirection.RIGHT: 4>]')
    def test_run(self):
        a=OptionsParser.parse("fbr")
        self.assertEqual(OptionsParser.run(a),['Zwierzak idzie do przodu', 'Zwierzak idzie do tyłu', 'Zwierzak skręca w prawo'])


if __name__ == '__main__':
    unittest.main()