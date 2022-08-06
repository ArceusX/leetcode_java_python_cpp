"""
. = matches any single char
* = matches repeating char. * ascertains for itself char
    match; not dictated by preceding chat. Untied to .

Text and pattern must match exactly.
"""

import unittest
from isMatch import isMatch

class Test(unittest.TestCase):
    def testIsMatch(self):
        # isMatch(text, pattern) -> bool:
        self.assertEqual(isMatch("", ""), True)
        self.assertEqual(isMatch("a", ""), False)
        self.assertEqual(isMatch("aa", "ba"), False)
        self.assertEqual(isMatch("", "*"), True)
        self.assertEqual(isMatch("a", "*"), True)
        
        self.assertEqual(isMatch("ab", "*"), False)
        self.assertEqual(isMatch("aaa", "*"), True)
        self.assertEqual(isMatch("a", "**"), True)
        self.assertEqual(isMatch("ab", "**"), True)
        
        self.assertEqual(isMatch("", "."), False)
        self.assertEqual(isMatch("a", "."), True)
        self.assertEqual(isMatch("ab", ".."), True)
        self.assertEqual(isMatch("a", ".."), False)
        self.assertEqual(isMatch("aa", "."), False)
        
        self.assertEqual(isMatch("", "*."), False)
        self.assertEqual(isMatch("", ".*"), False)
        self.assertEqual(isMatch("ab", "*."), True)
        self.assertEqual(isMatch("ab", "*.."), True)
        self.assertEqual(isMatch("baac", ".*."), True)
        self.assertEqual(isMatch("acbbc", ".*.*."), True)
        self.assertEqual(isMatch("bc", ".*."), True)
        self.assertEqual(isMatch("acbbc", ".*.**."), True)
        self.assertEqual(isMatch("acbbbd", "*.*.."), True)
        self.assertEqual(isMatch("accbb", ".*.c*"), True)
        self.assertEqual(isMatch("accd", "*.*"), False)
        self.assertEqual(isMatch("baa", "*."), False)
    
if __name__ == '__main__':
    unittest.main()