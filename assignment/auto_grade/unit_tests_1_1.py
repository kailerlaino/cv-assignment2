import unittest
import numpy as np

class TestImagePatches(unittest.TestCase):
    """Simple dummy test for image patches to verify autograder is working."""
    
    def test_dummy_test(self):
        """Dummy test that always passes to verify autograder functionality."""
        # Simple test that checks basic numpy functionality
        arr = np.array([1, 2, 3])
        expected = np.array([1, 2, 3])
        np.testing.assert_array_equal(arr, expected)
        
        # Test that we can import the student's code
        try:
            import filters
            self.assertTrue(True, "Successfully imported filters module")
        except ImportError:
            self.fail("Could not import filters module")
        
        # Test function call with simple input to check input/output types
        try:
            # Create a simple test image
            test_img = np.array([[1, 2], [3, 4]], dtype=np.float64)
            
            # Call the function with basic parameters
            result = filters.image_patches(test_img, patch_size=(2, 2))
            
            # Check output type
            self.assertIsInstance(result, list, "Output should be a list")
            self.assertTrue(len(result) > 0, "Output should contain at least one patch")
            
            # Check that patches are numpy arrays
            for patch in result:
                self.assertIsInstance(patch, np.ndarray, "Each patch should be a numpy array")
                
        except Exception as e:
            self.fail(f"Function call failed: {str(e)}")

if __name__ == '__main__':
    unittest.main() 