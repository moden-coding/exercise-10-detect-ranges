#!/usr/bin/env python3

import random
import unittest

from src.detect_ranges import detect_ranges


class TestDetectRanges(unittest.TestCase):

    def test_first(self):
        L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
        Lc = L.copy()
        result = detect_ranges(L)
        self.assertIsInstance(
            result, list,
            msg=f"detect_ranges should return a list. Got {type(result)}.")
        self.assertEqual(
            L, Lc, msg="Do not modify the input list %s!" % Lc)
        self.assertEqual(
            result, [2, (4, 9), 10, (12, 14)],
            msg="Incorrect result for the input list %s!" % L)

    def test_second(self):
        L = [1, 2, 4]
        res = detect_ranges(L)
        self.assertEqual(
            res, [(1, 3), 4],
            msg=f"Incorrect result for the input list {L}!")

    def test_third(self):
        L = [88, 89, 90, 92, 93, 94, 95, 96, 97]
        res = detect_ranges(L)
        self.assertEqual(
            res, [(88, 91), (92, 98)],
            msg=f"Incorrect result for the input list {L}!")

    def test_fourth(self):
        L = [-2, 0, 1, 2, 3]
        res = detect_ranges(L)
        self.assertEqual(
            res, [-2, (0, 4)],
            msg=f"Incorrect result for the input list {L}!")

    def test_fifth(self):
        L = [4, 2, 0, -2, -4]
        self.assertEqual(
            detect_ranges(L), list(reversed(L)),
            msg=f"Incorrect result for the input list {L}!")

    def test_random(self):
        for _ in range(10):
            L = list({random.randint(-100, 100) for _ in range(10)})
            mi = min(L)
            ma = max(L)
            complement = list(set(range(mi, ma + 1)) - set(L))
            result = detect_ranges(L)
            complement_result = detect_ranges(complement)

            def expand(ranges):
                catenation = []
                for x in ranges:
                    try:
                        a, b = x
                        catenation.extend(range(a, b))
                    except TypeError:
                        catenation.append(x)
                return catenation

            catenation = expand(result)
            self.assertEqual(
                sorted(L), catenation,
                msg="Wrong result for input list %s!" % L)
            complement_catenation = expand(complement_result)
            self.assertEqual(
                sorted(complement), complement_catenation,
                msg=f"Wrong result for input list {complement_catenation}!")
            self.assertEqual(
                len(result), len(complement_result) + 1,
                msg=f"Wrong number of ranges for one of input lists:\n{L}\n"
                    f"=>\n{result}\nand\n{complement}\n=>\n"
                    f"{complement_result}!")


if __name__ == '__main__':
    unittest.main()
