# test_modelcosmic.py
"""
Tests for ModelCosmic module.
"""

import unittest
from modelcosmic import ModelCosmic

class TestModelCosmic(unittest.TestCase):
    """Test cases for ModelCosmic class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ModelCosmic()
        self.assertIsInstance(instance, ModelCosmic)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ModelCosmic()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
