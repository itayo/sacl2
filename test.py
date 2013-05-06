import unittest
from sacl2 import *

class TestSequenceOne(unittest.TestCase):
  def test_isDebugEnabled(self):
    self.assertTrue(isDebug())
  def test_parseData(self):
    (done,todo) = parseXML(test=True)
    self.assertEqual(148,len(todo))
    self.assertEqual(79,len(done))
if __name__ == '__main__':
  unittest.main()
