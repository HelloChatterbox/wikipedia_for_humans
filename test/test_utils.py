import unittest
from wikipedia_for_humans.util import *


class TestUtils(unittest.TestCase):

    def test_split(self):
        self.assertEqual(split_sentences("hello. He said"),
                         ['hello.', 'He said'])
        self.assertEqual(split_sentences("hello . He said"),
                         ['hello .', 'He said'])
        self.assertEqual(split_sentences("hello.com"),
                         ["hello.com"])
        self.assertEqual(split_sentences("A.E:I.O.U"),
                         [ "A.E:I.O.U"])

        # ambiguous, no split
        # could be "Jones Jr. thinks ..."
        self.assertEqual(split_sentences("hello. he said"),
                         ['hello. he said'])
        # could be  "www.hello.com"
        self.assertEqual(split_sentences("hello.he said"),
                         ['hello.he said'])
        self.assertEqual(split_sentences("hello.He said"),
                         ['hello.He said'])
        # TODO maybe split this one?
        self.assertEqual(split_sentences("hello . he said"),
                         ['hello . he said'])

    def test_remove_parentheses(self):
        self.assertEqual(
            remove_parentheses("hello (ignored) world"), "hello world")
        self.assertEqual(
            remove_parentheses("hello [ignored ] world"), "hello world")
        self.assertEqual(
            remove_parentheses("hello { ignored } world"), "hello world")

    def test_normalize(self):
        s = "this is {remove me}     the first sentence "
        self.assertEqual(normalize(s), "this is the first sentence")
        s = "       this is (remove me) second. and the 3rd"
        self.assertEqual(normalize(s), "this is second. and the 3rd")
        s = "this       is [remove me] number 4! number5? number6. number 7 \n " \
            "number N"
        self.assertEqual(normalize(s), "this is number 4! number5? number6. number 7 number N")