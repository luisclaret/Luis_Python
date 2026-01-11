import unittest

try:
    from first_activity import (
        hello,
        add_two_numbers,
        subtract_two_numbers,
        multiply_two_numbers,
        divide_two_numbers,
        is_even,
        is_odd,
        area_of_triangle,
        area_of_rectangle,
        area_of_square,
        pythagorean_theorem,
        quadratic_formula,
        sum_two_numbers_if_even,
        calculate_first_right_digit,
        is_divisible_by_x,
        convert_to_celsius,
        is_leap_year,
        concat_two_strings,
        convert_to_fahrenheit
    )

except ImportError as import_fail:
    message = import_fail.args[0].split("(", maxsplit=1)
    item_name = import_fail.args[0].split()[3]

    item_name = item_name[:-1] + "()'"

    # pylint: disable=raise-missing-from
    raise ImportError(
        "\n\nMISSING FUNCTION --> In your 'first_activity.py' file, we can not find or import the"
        f" function named {item_name}. \nThe tests for this first exercise expect a function that"
        f' returns the string "Hello, World!"'
        f'\n\nDid you use print("Hello, World!") instead?'
    ) from None


class HelloWorldTest(unittest.TestCase):
    def test_say_hi(self):
        self.assertEqual(hello(), "Hello, World!")

    def test_concat_two_strings(self):
        self.assertEqual(concat_two_strings("Hello, ", "World!"), "Hello, World!")
        self.assertEqual(concat_two_strings("Good ", "Morning"), "Good Morning")
        self.assertEqual(concat_two_strings("", "Test"), "Test")
        self.assertEqual(concat_two_strings("Test", ""), "Test")

    def test_add_two_numbers(self):
        self.assertEqual(add_two_numbers(1, 2), 3)
        self.assertEqual(add_two_numbers(-1, 2), 1)
        self.assertEqual(add_two_numbers(-1, -2), -3)
        self.assertEqual(add_two_numbers(0, 0), 0)

    def test_subtract_two_numbers(self):
        self.assertEqual(subtract_two_numbers(1, 2), -1)
        self.assertEqual(subtract_two_numbers(-1, 2), -3)
        self.assertEqual(subtract_two_numbers(-1, -2), 1)
        self.assertEqual(subtract_two_numbers(0, 0), 0)

    def test_multiply_two_numbers(self):
        self.assertEqual(multiply_two_numbers(1, 2), 2)
        self.assertEqual(multiply_two_numbers(-1, 2), -2)
        self.assertEqual(multiply_two_numbers(-1, -2), 2)
        self.assertEqual(multiply_two_numbers(0, 0), 0)

    def test_divide_two_numbers(self):
        self.assertEqual(divide_two_numbers(1, 2), 0.5)
        self.assertEqual(divide_two_numbers(-1, 2), -0.5)
        self.assertEqual(divide_two_numbers(-1, -2), 0.5)
        with self.assertRaises(ValueError):
            divide_two_numbers(0, 0)
        with self.assertRaises(ValueError):
            divide_two_numbers(1, 0)

    def test_is_even(self):
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(-2))
        self.assertTrue(is_even(-4))
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-1))
        self.assertFalse(is_even(-3))

    def test_is_odd(self):
        self.assertTrue(is_odd(1))
        self.assertTrue(is_odd(3))
        self.assertTrue(is_odd(-1))
        self.assertTrue(is_odd(-3))
        self.assertFalse(is_odd(0))
        self.assertFalse(is_odd(2))
        self.assertFalse(is_odd(4))
        self.assertFalse(is_odd(-2))
        self.assertFalse(is_odd(-4))

    def test_area_of_triangle(self):
        self.assertEqual(area_of_triangle(3, 4), 6)
        self.assertEqual(area_of_triangle(5, 12), 30)
        self.assertEqual(area_of_triangle(6, 8), 24)
        self.assertEqual(area_of_triangle(0, 0), 0)

    def test_area_of_rectangle(self):
        self.assertEqual(area_of_rectangle(3, 4), 12)
        self.assertEqual(area_of_rectangle(5, 12), 60)
        self.assertEqual(area_of_rectangle(6, 8), 48)
        self.assertEqual(area_of_rectangle(0, 0), 0)

    def test_area_of_square(self):
        self.assertEqual(area_of_square(3), 9)
        self.assertEqual(area_of_square(5), 25)
        self.assertEqual(area_of_square(6), 36)
        self.assertEqual(area_of_square(0), 0)

    def test_pythagorean_theorem(self):
        self.assertEqual(pythagorean_theorem(3, 4), 5)
        self.assertEqual(pythagorean_theorem(5, 12), 13)
        self.assertEqual(pythagorean_theorem(6, 8), 10)
        self.assertEqual(pythagorean_theorem(0, 0), 0)

    def test_quadratic_formula(self):
        self.assertEqual(quadratic_formula(1, -3, 2), (2, 1))
        self.assertEqual(quadratic_formula(1, 0, -4), (2, -2))
        self.assertEqual(quadratic_formula(1, -4, 4), 2)
        with self.assertRaises(ValueError):
            quadratic_formula(1, 1, 1)

    def test_sum_two_numbers_if_even(self):
        self.assertEqual(sum_two_numbers_if_even(2, 4), 6)
        self.assertEqual(sum_two_numbers_if_even(3, 4), 0)
        self.assertEqual(sum_two_numbers_if_even(2, 5), 0)
        self.assertEqual(sum_two_numbers_if_even(3, 5), 0)

    def test_calculate_first_right_digit(self):
        self.assertEqual(calculate_first_right_digit(123), 3)
        self.assertEqual(calculate_first_right_digit(456), 6)
        self.assertEqual(calculate_first_right_digit(789), 9)
        self.assertEqual(calculate_first_right_digit(0), 0)

    def test_is_divisible_by_x(self):
        self.assertTrue(is_divisible_by_x(10, 5))
        self.assertTrue(is_divisible_by_x(10, 2))
        self.assertTrue(is_divisible_by_x(10, 10))
        self.assertTrue(is_divisible_by_x(10, 1))
        self.assertFalse(is_divisible_by_x(10, 3))
        self.assertFalse(is_divisible_by_x(10, 4))
        self.assertFalse(is_divisible_by_x(10, 6))

    def test_convert_to_celsius(self):
        self.assertAlmostEqual(convert_to_celsius(32), 0, delta=0.001)
        self.assertAlmostEqual(convert_to_celsius(212), 100, delta=0.001)
        self.assertAlmostEqual(convert_to_celsius(98.6), 37, delta=0.001)
        self.assertAlmostEqual(convert_to_celsius(68), 20, delta=0.001)

    def test_convert_to_fahrenheit(self):
        self.assertAlmostEqual(convert_to_fahrenheit(0), 32, delta=0.001)
        self.assertAlmostEqual(convert_to_fahrenheit(100), 212, delta=0.001)
        self.assertAlmostEqual(convert_to_fahrenheit(37), 98.6, delta=0.001)
        self.assertAlmostEqual(convert_to_fahrenheit(20), 68, delta=0.001)

    def test_is_leap_year(self):
        self.assertTrue(is_leap_year(2000))
        self.assertTrue(is_leap_year(2016))
        self.assertFalse(is_leap_year(1900))
        self.assertFalse(is_leap_year(2019))
        self.assertTrue(is_leap_year(2020))