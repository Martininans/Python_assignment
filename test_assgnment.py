import unittest

class TestStringMethods(unittest.TestCase):

    def test_calculate_string_length(self):
        self.assertEqual(calculate_string_length("hello"), 5)
        self.assertEqual(calculate_string_length(""), 0)

    def test_get_first_and_last_two_chars(self):
        self.assertEqual(get_first_and_last_two_chars("hello"), "helo")
        self.assertEqual(get_first_and_last_two_chars("h"), "")
        self.assertEqual(get_first_and_last_two_chars(""), "")

    def test_add_ing_or_ly(self):
        self.assertEqual(add_ing_or_ly("read"), "reading")
        self.assertEqual(add_ing_or_ly("swim"), "swimming")
        self.assertEqual(add_ing_or_ly("car"), "caring")

    def test_longest_word_and_length(self):
        self.assertEqual(longest_word_and_length(["hello", "world", "python"]), ("python", 6))
        self.assertEqual(longest_word_and_length(["cat", "dog", "bird"]), ("bird", 4))
        self.assertEqual(longest_word_and_length([]), (None, 0))

    def test_remove_odd_index_chars(self):
        self.assertEqual(remove_odd_index_chars("hello"), "el")
        self.assertEqual(remove_odd_index_chars("python"), "yhn")
        self.assertEqual(remove_odd_index_chars(""), "")

    def test_find_minimum(self):
        self.assertEqual(find_minimum([3, 1, 4, 1, 5]), 1)
        self.assertEqual(find_minimum([-5, -10, 0, 7]), -10)
        self.assertEqual(find_minimum([]), None)

    def test_find_maximum(self):
        self.assertEqual(find_maximum([3, 1, 4, 1, 5]), 5)
        self.assertEqual(find_maximum([-5, -10, 0, 7]), 7)
        self.assertEqual(find_maximum([]), None)

    def test_repeat_string_or_return(self):
        self.assertEqual(repeat_string_or_return("hello", 3), "hellohellohello")
        self.assertEqual(repeat_string_or_return("python", 0), "")
        self.assertEqual(repeat_string_or_return("", 5), "")

    def test_square_elements(self):
        self.assertEqual(square_elements([1, 2, 3]), [1, 4, 9])
        self.assertEqual(square_elements([-3, 0, 2]), [9, 0, 4])

    def test_sum_of_squared_elements(self):
        self.assertEqual(sum_of_squared_elements([1, 2, 3]), 14)
        self.assertEqual(sum_of_squared_elements([-3, 0, 2]), 13)
