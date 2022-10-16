import task
import unittest

class TestPython(unittest.TestCase):
   def setUp(self):
        self.res_dict = dict(zip([4, 3, 2, 1], ['djf#zemfzzofnz%', 'y#sjxf_znsvo!', 'jgreyk6hnze', 'xnhjrfyjvth3nxr']))
        self.config_file = 'input/config.txt'
        self.text_file = 'input/text.txt'

   def test_replace_text(self):
    res = task.replace_text(['a=z', 'b=y', 'c=x'], ['jgrebk6hnae', 'cnhjrfyjvth3nxr', 'b#sjcf_ansvo!', 'djf#aemfaaofna%'])
    self.assertEqual(res, self.res_dict)

   def test_sort_dict(self):
    res = task.sort_dict(self.res_dict)
    self.assertEqual(res, ['djf#zemfzzofnz%', 'y#sjxf_znsvo!', 'jgreyk6hnze', 'xnhjrfyjvth3nxr'])

   def test_read_from_file_config(self):
    res = task.read_from_file(self.config_file)
    self.assertEqual(res, ['a=z', 'b=y', 'c=x'])

   def test_read_from_file_text(self):
    res = task.read_from_file(self.text_file)
    self.assertEqual(res, ['jgrebk6hnae', 'cnhjrfyjvth3nxr', 'b#sjcf_ansvo!', 'djf#aemfaaofna%'])

   def test_read_from_file_config_error(self):
    res = task.read_from_file('input/config.tx')
    self.assertEqual(res, 0)

   def test_read_from_file_text_error(self):
    res = task.read_from_file('input/text.tx')
    self.assertEqual(res, 0)