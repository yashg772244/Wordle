import unittest
import HW03_Yash_Gilda_dictionary as dictionary
import HW03_Yash_Gilda_ui as ui
import HW03_Yash_Gilda_wordle as wordle
from unittest.mock import patch

class wordle_test(unittest.TestCase):
    def test_compare_word_true(self) -> None:
        """To test compare word function"""
        self.assertTrue(wordle.compareWord("hello","hello"))
    
    def test_compare_word_false(self) -> None:
        """To test compare word function"""
        self.assertFalse(wordle.compareWord("hello","books"))

    def test_exit_game_true(self) -> None:
        """To check if the game exits successfully"""
        self.assertTrue(ui.exit_game(""))

    def test_exit_game_false(self) -> None:
        """To check if the game exits successfully"""
        self.assertFalse(ui.exit_game("hello"))

    def test_check_char_true(self) -> None:
        """To check if the user input consists of characters only"""
        self.assertTrue(ui.check_char("@wert"))

    def test_check_char_false(self) -> None:
        """To check if the user input consists of characters only"""
        self.assertFalse(ui.check_char("hello"))

    def test_check_dic_true(self) -> None:
        """To check if the word is present in the dictionary"""
        self.assertTrue(ui.check_dic("aaaaa"))

    def test_check_dic_false(self) -> None:
        """To check if the word is present in the dictionary"""
        self.assertFalse(ui.check_dic("hello"))

    def test_check_len_true(self) -> None:
        """To check if the length of the word is 5"""
        self.assertTrue(ui.check_len("aaaa"))

    def test_check_len_false(self) -> None:
        """To check if the length of the word is 5"""
        self.assertFalse(ui.check_len("hello"))

    
if __name__ == "__main__":
    unittest.main()