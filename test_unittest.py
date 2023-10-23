import unittest
from unittest.mock import patch, call
from ex00.ft_map import ft_map
from ex00.ft_filter import ft_filter
from ex00.ft_reduce import ft_reduce
import ex01.main as ex01
import sys
import types
import ex05.TinyStatistician as ex05


class Test_Python_Module_00(unittest.TestCase):
    def test_ex00(self):
        x = [1, 2, 3, 4, 5]
        ret = ft_map(lambda dum: dum + 1, x)
        self.assertTrue(isinstance(ret, types.GeneratorType))
        self.assertListEqual(list(ft_map(lambda t: t + 1, x)), [2, 3, 4, 5, 6])
        ret = ft_filter(lambda dum: not (dum % 2), x)
        self.assertTrue(isinstance(ret, types.GeneratorType))
        self.assertListEqual(
            list(ft_filter(lambda dum: not (dum % 2), x)), [2, 4])
        lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
        ret = ft_reduce(lambda u, v: u + v, lst)
        self.assertEqual(ret, "Hello world")

    @patch('builtins.print')
    def test_ex01(self, mock_print):
        ex01.main()
        self.assertListEqual(mock_print.call_args_list, [call('var_0: 7'),
                                                         call('end'),
                                                         call('var_0: None'),
                                                         call('var_1: []'),
                                                         call('end'),
                                                         call('var_0: ft_lol'),
                                                         call('var_1: Hi'),
                                                         call('end'),
                                                         call('end'),
                                                         call('a: 10'),
                                                         call('hello: world'),
                                                         call('var_0: 12'),
                                                         call('var_1: Yes'),
                                                         call(
                                                             'var_2: [0, 0, 0]'),
                                                         call('end'),
                                                         call('ERROR'),
                                                         call('end'),
                                                         call('a: 10'),
                                                         call('var_0: 42'),
                                                         call('var_1: Yes'),
                                                         call('var_2: world'),
                                                         call('end')])

    def test_ex05(self):
        tstat = ex05.TinyStatistician()
        x = [1, 42, 300, 10, 59]
        ret = tstat.mean(x)
        self.assertEqual(type(ret), float)
        self.assertEqual(ret, 82.4)
        ret = tstat.median(x)
        self.assertEqual(type(ret), float)
        self.assertEqual(ret, 42.0)
        ret = tstat.quartiles(x)
        self.assertEqual(type(ret), list)
        for v in ret:
            self.assertEqual(type(v), float)
        self.assertListEqual(ret, [10.0, 59.0])
        ret = tstat.var(x)
        self.assertAlmostEqual(ret, 12279.439999999999)
        self.assertEqual(type(ret), float)
        ret = tstat.std(x)
        self.assertAlmostEqual(ret, 110.81263465868862)
        self.assertEqual(type(ret), float)
        pass


if __name__ == '__main__':
    unittest.main()
