from chamada import *


class TestChamada(object):
    def test_cada_coisa_com_mgs(self):
        cada_coisa("um teste com mgs")
        assert 1

    def test_cada_coisa_sem_mgs(self):
        cada_coisa()
        assert 1

    def test_main(self):
        main()
        assert 1

