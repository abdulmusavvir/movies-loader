import unittest
import json
import os
from junit_xml import TestSuite, TestCase

class TestJSONLoaderMethods(unittest.TestCase):
    movies = []

    @classmethod
    def setUpClass(cls):
        """Load the movies JSON file before any tests run."""
        with open('movies.json') as json_file:
            cls.movies = json.load(json_file)

    def test_rank(self):
        """Test that the rank of the first movie is '1'."""
        self.assertEqual(self.movies[0]['rank'], '1')

    def test_title(self):
        """Test that the title of the first movie is 'The Shawshank Redemption'."""
        self.assertEqual(self.movies[0]['title'], 'The Shawshank Redemption')

    def test_id(self):
        """Test that the ID of the first movie is 'tt0111161'."""
        self.assertEqual(self.movies[0]['id'], 'tt0111161')

if __name__ == '__main__':
    # Create the reports directory if it doesn't exist
    if not os.path.exists('reports'):
        os.makedirs('reports')

    # Create a Test Suite and run the tests
    suite = unittest.TestLoader().loadTestsFromTestCase(TestJSONLoaderMethods)
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    # Create XML report
    test_cases = []

    # Collect failed test cases
    for test, reason in result.failures:
        test_cases.append(TestCase(test.id(), reason))

    # Collect skipped test cases
    for test, reason in result.skipped:
        test_cases.append(TestCase(test.id(), reason, skipped=True))
        
    # Collect successful test cases
    for test in result.testsRun:  # Loop over the total tests run
        test_id = test.id() if test else None  # Ensure test is not None
        if test_id and not any(tc.test_case_id == test_id for tc in test_cases):  # Check for existing cases
            test_cases.append(TestCase(test_id, None))  # Add as success

    junit_xml_path = "reports/test_results.xml"
    with open(junit_xml_path, "w") as f:
        TestSuite("Test JSON Loader Methods", test_cases).to_file(f, prettyprint=True)

    print("Test results have been saved to:", junit_xml_path)
