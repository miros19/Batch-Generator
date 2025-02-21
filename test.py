import unittest
from batch_generator import BatchGenerator

class TestBatchGenerator(unittest.TestCase):
    def test_over_1_MB_record(self):
        test_string = ""
        for i in range(1000001):
            test_string += "1"
        
        generator = BatchGenerator([test_string])
        
        result = generator.array_of_batches()
        
        self.assertEqual(result, [[]])
    
    def test_1_MB_record(self):
        test_string = ""
        for i in range(1000000):
            test_string += "1"
        
        generator = BatchGenerator([test_string])
        
        result = generator.array_of_batches()
        
        self.assertEqual(result, [[test_string]])

    def test_501_records(self):
        test_array = []
        for i in range(502):
            test_array.append(str(i))
        
        generator = BatchGenerator(test_array)
        
        result = generator.array_of_batches()
        
        self.assertEqual(len(result), 2)
    
    def test_5_MB_batch(self):
        test_string = ""
        for i in range(1000000):
            test_string += "1"
        
        test_array = [test_string for i in range(10)]

        generator = BatchGenerator(test_array)
        
        result = generator.array_of_batches()
        
        self.assertEqual(len(result), 2)
        self.assertEqual(len(result[0]), 5)
        self.assertEqual(len(result[1]), 5)
    
    def test_0_records(self):
        array = []
        generator = BatchGenerator(array)
        
        result = generator.array_of_batches()
        
        self.assertEqual(result, [[]])
        
        
if __name__ == "__main__":
    unittest.main()