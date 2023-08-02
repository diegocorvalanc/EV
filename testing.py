import unittest
from my_code import time_to_minutes
from my_code import process_data


class test_my_code(unittest.TestCase):
    
    def test_time_to_minutes(self):
        minutes = time_to_minutes("09:00","12:30") # Test case with correct time format
        self.assertEqual(minutes, 210)
        
        invalid_format = time_to_minutes("abc","def") # Test case with invalid time format
        self.assertIsNone(invalid_format)
        

    def test_process_data(self):
        # Test case with valid data
        data = {
            "student1":
                {
                    "attendances": [(1,"09:00","12:00"),(2,"13:00","16:00")]
                }
        }
        result = process_data(data)
        expected_result = {
            "student1":{
                "total_minutes": 360,
                "unique_days": {1,2}
            }
        }
        self.assertEqual(result, expected_result)
        
        # Test case with student without attendances
        data_no_attendances = {
            "student1":{
                "attendances": []
            }
        }
        result_no_attendances = process_data(data_no_attendances)
        expected_resutl_no_attendnces = {
            "student1":{
                "total_minutes": 0,
                "unique_days": set()
            }                
        }
        self.assertEqual(result_no_attendances, expected_resutl_no_attendnces)
        
        
if __name__ == "__main__":
    unittest.main()
        