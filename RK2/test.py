import unittest
from RK2 import *


class TestSchoolTasks(unittest.TestCase):

    def setUp(self):
        # Создаем тестовые данные
        self.classes = [
            SchClass(1, '1А'),
            SchClass(2, '1Б'),
            SchClass(3, '1В'),
            SchClass(11, '2А'),
            SchClass(22, '3Б'),
            SchClass(33, '4Г'),
        ]

        self.pupils = [
            Pupil(1, 'Аксенов', 3, 1),
            Pupil(2, 'Соломахин', 4, 1),
            Pupil(3, 'Лемзиков', 6, 2),
            Pupil(4, 'Семенов', 0, 2),
            Pupil(5, 'Уваров', 10, 3),
        ]

        self.pupils_classes = [
            PupilClass(1, 1),
            PupilClass(1, 2),
            PupilClass(2, 3),
            PupilClass(2, 4),
            PupilClass(3, 5),
            PupilClass(11, 1),
            PupilClass(11, 2),
            PupilClass(22, 3),
            PupilClass(22, 4),
            PupilClass(33, 5),
        ]

    def test_task1(self):
        otm = one_to_many(self.classes, self.pupils)
        result = task1(otm)
        expected_result = [('Аксенов', 3, '1А'), ('Соломахин', 4, '1А'), 
                           ('Лемзиков', 6, '1Б'), ('Семенов', 0, '1Б'), 
                           ('Уваров', 10, '1В')]
        self.assertEqual(result, expected_result)

    def test_task2(self):
        otm = one_to_many(self.classes, self.pupils)
        result = task2(otm, self.classes)
        expected_result = [('1В', 10), ('1А', 7), ('1Б', 6)]
        self.assertEqual(result, expected_result)

    def test_task3(self):
        mtm = many_to_many(self.classes, self.pupils_classes, self.pupils)
        result = task3(mtm, self.classes)
        expected_result = {'1А': ['Уваров', 'Лемзиков'],
                           '2А': ['Аксенов', 'Соломахин'],}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
