import unittest

class TestSequenceOne(unittest.TestCase):
  def test_Success(self):
    self.assertEqual('a','a')
    self.assertTrue(True)
  def test_FailOne(self):
    self.assertEqual('a','b')
  def test_FailTwo(self):
    self.assertTrue(False)
  def test_FailThree(self):
    self.assertRaises(TypeError,dir,unittest)
if __name__ == '__main__':
  unittest.main()
