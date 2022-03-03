import unittest
from main import mr_carbon
from json import load
from unittest.mock import Mock
from pathlib import Path

test_folder = Path("tests")

def str_list_to_float_list(str_list):
    return [float(f) for f in str_list[1 : len(str_list) - 1].split(", ")]

class TestCalculation(unittest.TestCase):
    def test_small_petrol(self):
        #ARRANGE
        file_path = test_folder / "test_small_petrol.json"
        file = open(file_path, "r")
        test_dictionary = load(file)
        file.close()
        http_request = Mock()
        http_request.get_json.return_value = test_dictionary 
        co2e_per_m = 0.14946
        distances = [97348, 97242]       

        #ACT
        answer = mr_carbon(http_request)

        #ASSERT
        correct_results = [97348 * 0.14946, 97242 * 0.14946]
        float_answers = str_list_to_float_list(answer)
        for i in range(len(correct_results)):
            self.assertTrue(abs(
                float_answers[i] - distances[i] * co2e_per_m
                ) < 0.001)

if __name__ == '__main__':
    unittest.main()
