# tests/test_app.py

import unittest
import app

class TestApp(unittest.TestCase):
    def test_main_runs(self):
        # Just a basic sanity check
        self.assertIsNone(app.main())

if __name__ == '__main__':
    unittest.main()
