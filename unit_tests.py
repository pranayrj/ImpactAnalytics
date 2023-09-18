import unittest
from CheckAttendanceEligibilty import AttendClass


class TestAttendClass(unittest.TestCase):
    def test_for_n_equals_1(self):
        N = 1
        university = AttendClass()
        result1 = f"{university.ways_to_attend_classes(N)}"
        result2 = f"{university.ways_miss_graduation(N)}/{university.ways_to_attend_classes(N)}"
        self.assertEqual(result1, f"2")
        self.assertEqual(result2, f"1/2")

    def test_for_n_equals_2(self):
        N = 2
        university = AttendClass()
        result1 = f"{university.ways_to_attend_classes(N)}"
        result2 = f"{university.ways_miss_graduation(N)}/{university.ways_to_attend_classes(N)}"
        self.assertEqual(result1, f"4")
        self.assertEqual(result2, f"2/4")

    def test_for_n_equals_4(self):
        N = 4
        university = AttendClass()
        result1 = f"{university.ways_to_attend_classes(N)}"
        result2 = f"{university.ways_miss_graduation(N)}/{university.ways_to_attend_classes(N)}"
        self.assertEqual(result1, f"15")
        self.assertEqual(result2, f"7/15")

    def test_for_n_equals_5(self):
        N = 5
        university = AttendClass()
        result1 = f"{university.ways_to_attend_classes(N)}"
        result2 = f"{university.ways_miss_graduation(N)}/{university.ways_to_attend_classes(N)}"
        self.assertEqual(result1, f"29")
        self.assertEqual(result2, f"14/29")

    def test_for_n_equals_6(self):
        N = 6
        university = AttendClass()
        result1 = f"{university.ways_to_attend_classes(N)}"
        result2 = f"{university.ways_miss_graduation(N)}/{university.ways_to_attend_classes(N)}"
        self.assertEqual(result1, f"56")
        self.assertEqual(result2, f"27/56")

    def test_for_n_equals_7(self):
        N = 7
        university = AttendClass()
        result1 = f"{university.ways_to_attend_classes(N)}"
        result2 = f"{university.ways_miss_graduation(N)}/{university.ways_to_attend_classes(N)}"
        self.assertEqual(result1, f"108")
        self.assertEqual(result2, f"52/108")

    def test_for_n_equals_10(self):
        N = 10
        university = AttendClass()
        result1 = f"{university.ways_to_attend_classes(N)}"
        result2 = f"{university.ways_miss_graduation(N)}/{university.ways_to_attend_classes(N)}"
        self.assertEqual(result1, f"773")
        self.assertEqual(result2, f"372/773")

if __name__ == '__main__':
    unittest.main()