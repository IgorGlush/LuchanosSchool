import pytest
from LuchanosSchool.HW1 import fibb
from LuchanosSchool.HW1 import summ_min


@pytest.mark.parametrize('n,exprxt',[
    (1,0),
    (2,1),
    (10,34),
    (20,4181)
])
def test_funk_fibb(n, exprxt):
    assert(fibb(n) == exprxt)

@pytest.mark.parametrize('n,err',[
    ('string',TypeError)
])
def test_eror_fibb(n, err):
    with pytest.raises(err):
        fibb(n)


@pytest.mark.parametrize('a,b,c,expect', [
    (10,20,30,30),
    (100,10000,1000,1100),
    (1,1,2,2),
    (9876,123,321,444)
])
def test_summ_min(a,b,c, expect):
    summ_min(a,b,c) == expect

@pytest.mark.parametrize('a,b,c,err',[
    ('string',12,12,TypeError),
    (12,'string',12,TypeError),
    (12,234,'string',TypeError)
])
def test_err_summ_min(a,b,c,err):
    with pytest.raises(err):
        summ_min(a, b, c)