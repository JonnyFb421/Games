import unittest
from unittest.mock import patch
import re

from hangman import hangman

class TestHangman(unittest.TestCase):
    def test_get_hangman_words_contains_no_special_characters(self):
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        for word in hangman.get_hangman_words():
            self.assertIsNone(regex.match(word))

    def test_get_hangman_words_returns_list_of_strings(self):
        words = hangman.get_hangman_words()
        self.assertIsInstance(words, list)
        for word in words:
            self.assertIsInstance(word, str)

    @patch('builtins.input', return_value="Taco")
    def test_get_guess_from_user_with_multiple_characters(self, mock_input):
        self.assertIsNone(hangman.get_guess_from_user([]))

    @patch('builtins.input', return_value="t")
    def test_get_guess_from_user_with_valid_input(self, mock_input):
        result = hangman.get_guess_from_user([])
        self.assertEqual(result, "t")

    @patch('builtins.input', return_value="T")
    def test_get_guess_from_user_is_case_insensitive(self, mock_input):
        result = hangman.get_guess_from_user([])
        self.assertEqual(result, "t")

    @patch('builtins.input', return_value="t")
    def test_get_guess_from_user_with_duplicated_character(self, mock_input):
        guessed_chars = ['t']
        self.assertIsNone(hangman.get_guess_from_user(guessed_chars))

    def test_is_man_hanged_with_guesses_left(self):
        current_guess_count = 1
        max_guess_count = 8
        self.assertFalse(hangman.is_man_hanged(current_guess_count, max_guess_count))

    def test_is_man_hanged_without_remaining_guesses(self):
        current_guess_count = 8
        max_guess_count = 8
        self.assertTrue(hangman.is_man_hanged(current_guess_count, max_guess_count))

    def test_is_guess_correct_with_correct_guess(self):
        guess = 'a'
        answer = 'apple'
        self.assertTrue(hangman.is_guess_correct(guess, answer))

    def test_is_guess_correct_with_incorrect_guess(self):
        guess = 'a'
        answer = 'poop'
        self.assertFalse(hangman.is_guess_correct(guess, answer))

    @patch('hangman.get_hangman_words', ['Taco'])
    @patch('hangman.get_guess_from_user')
    def test_create_new_game_with_winner(self, words_mock, guess_mock):
        guess_mock.side_effects = ['t', 'a', 'c', 'o']
        self.assertTrue(hangman.create_new_game())

    def test_is_puzzle_solved_with_solved_puzzle(self):
        self.assertTrue(hangman.is_puzzle_solved(['p', 'o'], 'poop'))

    def test_is_puzzle_solved_with_unsolved_puzzle(self):
        self.assertFalse(hangman.is_puzzle_solved(['p', 'o'], 'taco'))
