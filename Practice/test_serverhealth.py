#!/usr/bin/venv python3


import unittest

from serverHealth import status

class Test_Server_health(unittest.TestCase):
   def test_status(self):
      expected = "WARNING"
      self.assertEqual(status(20,20,89), expected)

   def test_imput(self):
      expected = "CRITICAL"
      self.assertEqual(status(95,50,30), expected)
   
   def test_zero(self):
      expected = "CRITICAL"
      self.assertEqual(status(0,0,95), expected)


unittest.main()
