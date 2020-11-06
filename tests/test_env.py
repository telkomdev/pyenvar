import os
import unittest
import pathlib
import pyenvar

class TestEnv(unittest.TestCase):

    def test_parse(self):
        env_data = 'USERNAME="admin"\nPASSWORD=12345'
        parsed = pyenvar.parse(env_data)

        self.assertEqual('admin', parsed.get('USERNAME'))
    
    def test_load(self):
        here = pathlib.Path(__file__).parent.resolve()
        env_path = '{0}/.env.example'.format(here)
        pyenvar.load(path=env_path)
        print(os.environ.keys())
        self.assertEqual('admin', os.environ.get('USERNAME'))


if __name__ == '__main__':
    unittest.main()