import unittest

class TestSequenceOne(unittest.TestCase):
  def test_Success(self):
    self.assertEqual('a','a')
    self.assertTrue(True)
  def test_Fail(self):
    self.assertTrue(False)
if __name__ == '__main__':
  unittest.main()
