import unittest
from src.common.character import BaseAttribute, DerivedAttribute, Character

class CharacterTest(unittest.TestCase):

    def test_init(self):
        my_char = Character([12,13,15,17,10,12,14,12])
        self.assertEqual(my_char.base_attributes, [12,13,15,17,10,12,14,12])


if __name__ == '__main__':
    unittest.main()
