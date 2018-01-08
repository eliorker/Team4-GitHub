import unittest
import no_cli


class TestCV(unittest.TestCase):
    def test_register(self):
        self.assertEqual(no_cli.register("elio321","123","mail","0","0509099545"),True )
    def test_login(self):
        self.assertEqual(no_cli.login("elio321", "123"), True)
    def test_addslashes(self):
        self.assertEqual(no_cli.addslashes("elior"), "'elior'")
    def test_token_read(self):
        self.assertEqual(no_cli.tokenread(),"elio321")


if __name__ == '__main__':
    unittest.main()