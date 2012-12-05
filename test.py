import unittest

class TestSequenceOne(unittest.TestCase):
  def test_Success(self):
    self.assertEqual('a','a')
    self.assertTrue(True)
if __name__ == '__main__':
  unittest.main()
