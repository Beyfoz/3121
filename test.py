import unittest
from suggester import Suggester, MAX_FOUND


class TestSuggesterMaxFound(unittest.TestCase):
    def setUp(self):
        # Создаем временный файл с тестовыми словами
        self.test_filename = "test_ruwords.txt"
        with open(self.test_filename, "w", encoding="utf-8") as f:
            for i in range(20):
                f.write(f"word{i}\n")

    def tearDown(self):
        # Удаляем временный файл после тестов
        import os
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_max_found(self):
        """Тестируем, что метод get возвращает не более MAX_FOUND элементов."""
        suggester = Suggester(self.test_filename)
        result = suggester.get("word")
        self.assertLessEqual(len(result), MAX_FOUND)

    def test_no_newline_in_words(self):
        """Тестируем, что слова возвращаются без символа новой строки."""
        suggester = Suggester(self.test_filename)
        result = suggester.get("word")

        # Проверяем, что ни одно слово не содержит \n
        for word in result:
            self.assertNotIn("\n", word, f"Слово '{word}' содержит символ новой строки")


if __name__ == '__main__':
    unittest.main()
