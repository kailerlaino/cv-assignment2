import unittest
import numpy as np

class TestHarrisDetector(unittest.TestCase):
    """Simple dummy test for Harris detector to verify autograder is working."""
    
    def test_dummy_test(self):
        """Dummy test that always passes to verify autograder functionality."""
        # Simple test that checks basic numpy functionality
        arr = np.array([1, 2, 3])
        expected = np.array([1, 2, 3])
        np.testing.assert_array_equal(arr, expected)
        
        # Test that we can import the student's code
        try:
            import corners
            self.assertTrue(True, "Successfully imported corners module")
        except ImportError:
            self.fail("Could not import corners module")
        
        # Test function call with simple input to check input/output types
        try:
            # Create a simple test image
            test_img = np.array([[1, 2], [3, 4]], dtype=np.float64)
            
            # Call the function with basic parameters
            result = corners.harris_detector(test_img, window_size=(2, 2))
            
            # Check output type and shape
            self.assertIsInstance(result, np.ndarray, "Output should be a numpy array")
            self.assertEqual(result.shape, test_img.shape, "Output shape should match input shape")
            self.assertEqual(result.dtype, np.float64, "Output should be float64")
            
        except Exception as e:
            self.fail(f"Function call failed: {str(e)}")

if __name__ == '__main__':
    unittest.main() 