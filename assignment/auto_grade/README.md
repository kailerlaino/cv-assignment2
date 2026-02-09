# HW2 Autograder

This autograder is designed to test student submissions for HW2 - Image Processing and Edge Detection.

## How to Run

### For Testing Your Own Code

To test the code in the `code/` directory:

```bash
cd hw2/assignment
python auto_grade/autograder.py --submission_dir_name . --submission_id code --config auto_grade/config.json
```

### Command Breakdown

- `--submission_dir_name .` - Look in the current directory for submissions
- `--submission_id code` - Process the submission named "code" (your code directory)
- `--config auto_grade/config.json` - Use the configuration file in the auto_grade directory

### What Happens

1. The autograder loads the configuration from `config.json`
2. It validates that your `code/` directory contains all required files:
   - `filters.py`
   - `corners.py`
3. It copies test files from `auto_grade/` to your `code/` directory
4. It runs all tests and generates scores 
5. Results are saved to `grades.csv` and detailed results in `detailed_results/`

### Required Files

Your `code/` directory must contain:
- `filters.py` - Image filtering and edge detection functions
- `corners.py` - Corner detection functions

### Test Files

The autograder will copy these test files to your code directory:
- `unit_tests_1_1.py` 
- `unit_tests_2_1.py` 
- `unit_tests_2_2.py` 
- `unit_tests_3_1.py` 
- `unit_tests_5_1.py` 
- `unit_tests_6_1.py` 
- `unit_tests_7_1.py` 

### Output

- `grades.csv` - Summary scores for all test suites
- `detailed_results/` - Individual test results for each test suite

## Troubleshooting

- **"Config file not found"**: Make sure to use `--config auto_grade/config.json`
- **"Missing file" errors**: Ensure all required files exist in your `code/` directory
- **Test failures**: Check the detailed error messages to see which specific tests failed
- **Tests not updating**: Remove `__pycache__` directories to force Python to reload test files

## Test Structure

Each test file contains a simple dummy test that:
1. Verifies basic numpy functionality
2. Checks that your code modules can be imported
3. Calls your functions with simple inputs to verify input/output types
4. Ensures the autograder infrastructure is functioning correctly

When you're ready to implement the actual homework functions, you can replace these dummy tests with real test cases that check your implementations.


### Submission Format

Your submission folder should have the following structure:

```
your_UT_EID
└── code/                  # Student's implementation code
    ├── common.py          # Common utilities (MUST BE INCLUDED if you made any changes)
    ├── corners.py         # Corner detection implementation
    ├── filters.py         # Image filtering implementation
    ├── blob_detection.py  # Blob detection implementation
    ├── image_patches/             # Directory with the detected image patches in it.
    │   └── ...
    ├── gaussian_filter/           # Directory with filtered image and edge responses
    │   └── ...
    ├── sobel_operator/            # Directory with Sobel filtered outputs
    │   └── ...
    ├── log_filter/                # Directory with LoG response outputs
    │   └── ...
    ├── feature_detection/         # Directory with Harris and Corner detections
    │   └── ...
    ├── polka_detections/          # Directory with polka detection outputs
    │   └── ...
    └-─ cell_detections/           # Directory with cell detection outputs
        └── ...
```

**Note: You do NOT need to include any of the autograde code in your submission - only your implementation files in the `code/` directory.**

Ensure all required files from the assignment are present in the `code/` directory and test your submission locally using the autograder before submitting.



