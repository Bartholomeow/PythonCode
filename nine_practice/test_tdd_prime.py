import tdd_prime


class TestGCD:
    def test_simple_gcd(self):
        assert tdd_prime.gcd(5, 7) == 1

    def test_simple_gcd1(self):
        assert tdd_prime.gcd(1, 1) == 1

    def test_simple_gcd2(self):
        assert tdd_prime.gcd(1, 0) == 1

    def test_simple_gcd3(self):
        assert tdd_prime.gcd(0, 1) == 1

    def test_simple_gcd4(self):
        assert tdd_prime.gcd(-1, 4) == 1

    def test_simple_gcd5(self):
        assert tdd_prime.gcd(1, -4) == 1

    def test_simple_gcd6(self):
        assert tdd_prime.gcd(-1, 0) == 1

    def test_simple_gcd7(self):
        assert tdd_prime.gcd(0, -1) == 1

    def test_simple_gcd8(self):
        assert tdd_prime.gcd(0, 0) == 0

    def test_simple_gcd9(self):
        assert tdd_prime.gcd(12, 6) == 6

    def test_simple_gcd10(self):
        assert tdd_prime.gcd(6, 12) == 6

    def test_simple_gcd11(self):
        assert tdd_prime.gcd(-6, 12) == 6

    def test_simple_gcd12(self):
        assert tdd_prime.gcd(-12, 6) == 6


class TestLCM:
    def test_simple_lcm(self):
        assert tdd_prime.lcm(5, 7) == 35

    def test_simple_lcm1(self):
        assert tdd_prime.lcm(1, 1) == 1

    def test_simple_lcm2(self):
        assert tdd_prime.lcm(1, 0) == 0

    def test_simple_lcm3(self):
        assert tdd_prime.lcm(0, 1) == 0

    def test_simple_lcm4(self):
        assert tdd_prime.lcm(-1, 4) == 4

    def test_simple_lcm5(self):
        assert tdd_prime.lcm(1, -4) == 4

    def test_simple_lcm6(self):
        assert tdd_prime.lcm(-1, 0) == 0

    def test_simple_lcm7(self):
        assert tdd_prime.lcm(0, -1) == 0

    def test_simple_lcm8(self):
        assert tdd_prime.lcm(0, 0) == "Undefined"

    def test_simple_lcm9(self):
        assert tdd_prime.lcm(12, 6) == 12

    def test_simple_lcm10(self):
        assert tdd_prime.lcm(6, 12) == 12

    def test_simple_lcm11(self):
        assert tdd_prime.lcm(-6, 12) == 12

    def test_simple_lcm12(self):
        assert tdd_prime.lcm(-12, 6) == 12


class TestIsPrime:
    def test_is_prime_2(self):
        assert tdd_prime.is_prime(2) == True

    def test_is_prime_1(self):
        assert tdd_prime.is_prime(1) == False

    def test_is_prime_3(self):
        assert tdd_prime.is_prime(3) == True

    def test_is_prime_4(self):
        assert tdd_prime.is_prime(4) == False

    def test_is_prime_float(self):
        assert tdd_prime.is_prime(1.5) == False

    def test_is_prime_0(self):
        assert tdd_prime.is_prime(0) == False

    def test_is_prime_negative(self):
        assert tdd_prime.is_prime(-1) == False
