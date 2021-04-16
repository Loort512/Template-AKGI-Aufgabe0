import random
import string
from unittest import TestCase

import aufgaben


class AufgabeTest(TestCase):
    def check_list(self, l, dim1, dim2):
        self.assertIsNotNone(l)
        self.assertTrue(isinstance(l, list), "Result is not a list")
        self.assertEqual(len(l), dim1, "Length of result was expected to be " + str(dim1) + " but is " + str(len(l)))
        for i in range(0, dim1):
            self.assertTrue(isinstance(l[i], list), str(i) + "th element of result is not a list")
            self.assertEqual(len(l[i]), dim2,
                             "Length of " + str(i) + "th element of result was expected to be " + str(dim2) +
                             " but is " + str(len(l[i])))

    def test_create_3x3_list(self):
        result = aufgaben.create_3x3_list()
        self.check_list(result, 3, 3)

    def test_create_3x3_list_different(self):
        result = aufgaben.create_3x3_list_different()
        self.check_list(result, 3, 3)
        numset = set()
        self.assertIsNotNone(result)
        for i in range(0, 3):
            for j in range(0, 3):
                numset.add(result[i][j])
        self.assertEqual(len(numset), 9, "Not all numbers are different")

    def test_remove_middle_element(self):
        result = aufgaben.remove_middle_element([[0,0,0], [0,0,0], [0,0,0]])
        self.check_list(result, 2, 3)

    def test_convert_to_dict(self):
        result = aufgaben.convert_to_dict([[0,0,0], [0,0,0], [0,0,0]])
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, dict), "Result is not a dictionary")
        self.assertEqual(len(result), 3, "Length of result was expected to be 3 but is " + str(len(result)))
        for i in result.keys():
            self.assertTrue(isinstance(i, str), "Key " + str(i) + " is not a string")
            self.assertTrue(isinstance(result[i], list), "Value " + str(result[i]) + " (at key " + str(i) +
                            ") is not an array")
            self.assertEqual(len(result[i]), 3,
                             "Length of element \"" + i + "\" of result was expected to be 3 but is " +
                             str(len(result[i])))

    def test_get_char(self):
        for i in range(0, 5):
            textlen = random.randint(10,15)
            text = ''.join(random.choice(string.ascii_letters + " ") for _ in range(textlen))
            pos = random.randint(0,textlen-1)
            result = aufgaben.get_char(text, pos)
            self.assertIsNotNone(result)
            self.assertTrue(isinstance(result, str), "Result is not a string")
            self.assertEqual(result, text[pos], str(pos) + "tes Element von \"" + text + "\" sollte " + text[pos] +
                             " sein, ist aber \"" + result + "\"")

    def test_get_word(self):
        for i in range(0, 5):
            wordnum = random.randint(3,8)
            words = []
            for i in range(wordnum):
                words += [''.join(random.choice(string.ascii_letters) for _ in range(random.randint(5,10)))]
            pos = random.randint(0,wordnum-1)
            text = " ".join(words)
            result = aufgaben.get_word(text, pos)
            self.assertIsNotNone(result)
            self.assertTrue(isinstance(result, str), "Result is not a string")
            self.assertEqual(result, words[pos], str(pos) + "tes Wort von \"" + text + "\" sollte " + words[pos] +
                             " sein, ist aber \"" + result + "\"")

    def test_join_by_dashes(self):
        for i in range(0, 5):
            wordnum = random.randint(3,8)
            words = []
            for i in range(wordnum):
                words += [''.join(random.choice(string.ascii_letters) for _ in range(random.randint(5,10)))]
            text = " ".join(words)
            expected = "--".join(words)
            result = aufgaben.join_by_dashes(text)
            self.assertIsNotNone(result)
            self.assertTrue(isinstance(result, str), "Result is not a string")
            self.assertEqual(result, expected, "Ergebnis \"" + expected +
                             "\" sein, ist aber \"" + result + "\"")

    def test_text_to_array(self):
        for i in range(0, 5):
            textlen = random.randint(10,15)
            chars = [random.choice(string.ascii_letters + " ") for _ in range(textlen)]
            result = aufgaben.text_to_array(''.join(chars))
            self.assertIsNotNone(result)
            self.assertTrue(isinstance(result, list), "Result is not a list")
            self.assertListEqual(result, chars)

    def test_text_to_unique_array(self):
        result = aufgaben.text_to_unique_array("This is a test")
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, list), "Result is not a list")
        self.assertListEqual(result, ["T", "h", "i", "s", " ", "a", "t", "e"])

    def test_invert_text(self):
        result = aufgaben.invert_text("Zeichenkette")
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, str), "Result is not a string")
        self.assertEqual(result, "etteknehcieZ")

    def test_make_rotations(self):
        result = aufgaben.make_rotations("test")
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, list), "Result is not a list")
        self.assertListEqual(result, ["test", "estt", "stte", "ttes"])
