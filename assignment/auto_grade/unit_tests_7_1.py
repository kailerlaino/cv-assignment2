import unittest
import numpy as np
import sys, os
from scipy import ndimage

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import blob_detection

class TestGaussianFilter(unittest.TestCase):
    """Simple dummy test for Gaussian filter to verify autograder is working."""
    
    def test_dummy_test(self):
        """Dummy test that always passes to verify autograder functionality."""
        # Simple test that checks basic numpy functionality
        arr = np.array([1, 2, 3])
        expected = np.array([1, 2, 3])
        np.testing.assert_array_equal(arr, expected)
        
        # Test that we can import the student's code
        try:
            import blob_detection
            self.assertTrue(True, "Successfully imported blob_detection module")
        except ImportError:
            self.fail("Could not import blob_detection module")
        
        # Test function call with simple input to check input/output types
        try:
            # Create a simple test image
            test_img = np.array([[1, 2], [3, 4]], dtype=np.float64)
            
            # Call the function with basic parameters
            result = blob_detection.gaussian_filter(test_img, sigma=1.0)
            
            # Check output type and shape
            self.assertIsInstance(result, np.ndarray, "Output should be a numpy array")
            self.assertEqual(result.shape, test_img.shape, "Output shape should match input shape")
            self.assertEqual(result.dtype, np.float64, "Output should be float64")
            
        except Exception as e:
            self.fail(f"Function call failed: {str(e)}")

if __name__ == '__main__':
    unittest.main() 