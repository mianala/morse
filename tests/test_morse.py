import unittest
from morse import decode

class TestMorse(unittest.TestCase):
    def test_empty_message(self):
        self.assertEqual(decode(""), "")

    def test_a(self):
        self.assertEqual(decode(".-"), "A")

    def test_b(self):
        self.assertEqual(decode("-..."), "B")

    def test_c(self):
        self.assertEqual(decode("-.-."), "C")

    def test_d(self):
        self.assertEqual(decode("-.."), "D")

    def test_e(self):
        self.assertEqual(decode("."), "E")

    def test_f(self):
        self.assertEqual(decode("..-."), "F")

    def test_g(self):
        self.assertEqual(decode("--."), "G")

    def test_h(self):
        self.assertEqual(decode("...."), "H")

    def test_i(self):
        self.assertEqual(decode(".."), "I")

    def test_j(self):
        self.assertEqual(decode(".---"), "J")

    def test_k(self):
        self.assertEqual(decode("-.-"), "K")

    def test_l(self):
        self.assertEqual(decode(".-.."), "L")

    def test_m(self):
        self.assertEqual(decode("--"), "M")

    def test_n(self):
        self.assertEqual(decode("-."), "N")

    def test_o(self):
        self.assertEqual(decode("---"), "O")

    def test_p(self):
        self.assertEqual(decode(".--."), "P")

    def test_q(self):
        self.assertEqual(decode("--.-"), "Q")

    def test_r(self):
        self.assertEqual(decode(".-."), "R")

    def test_s(self):
        self.assertEqual(decode("..."), "S")

    def test_t(self):
        self.assertEqual(decode("-"), "T")

    def test_u(self):
        self.assertEqual(decode("..-"), "U")

    def test_v(self):
        self.assertEqual(decode("...-"), "V")

    def test_w(self):
        self.assertEqual(decode(".--"), "W")

    def test_x(self):
        self.assertEqual(decode("-..-"), "X")

    def test_y(self):
        self.assertEqual(decode("-.--"), "Y")

    def test_z(self):
        self.assertEqual(decode("--.."), "Z")

    def test_sos(self):
        self.assertEqual(decode("... --- ..."), "SOS")