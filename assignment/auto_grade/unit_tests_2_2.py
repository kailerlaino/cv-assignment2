import unittest
import numpy as np

class TestEdgeDetection(unittest.TestCase):
    """Simple dummy test for edge detection to verify autograder is working."""
    
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
            result = filters.edge_detection(test_img)
            
            # Check output type and structure
            self.assertIsInstance(result, tuple, "Output should be a tuple")
            self.assertEqual(len(result), 3, "Output should have 3 elements (Ix, Iy, grad_magnitude)")
            
            Ix, Iy, grad_magnitude = result
            
            # Check each output component
            for component in [Ix, Iy, grad_magnitude]:
                self.assertIsInstance(component, np.ndarray, "Each component should be a numpy array")
                self.assertEqual(component.shape, test_img.shape, "Component shape should match input shape")
                self.assertEqual(component.dtype, np.float64, "Component should be float64")
            
        except Exception as e:
            self.fail(f"Function call failed: {str(e)}")

if __name__ == '__main__':
    unittest.main() 