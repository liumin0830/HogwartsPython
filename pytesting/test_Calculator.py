import pytest
import yaml

from pytesting.Calculator import Calculator

# 解析测试数据文件
def get_datas(dkey):
    with open("Datas/calc.yml", 'r', encoding='UTF-8') as f:
        datas = yaml.safe_load(f)
    add_datas = datas[dkey]["datas"]
    add_ids = datas[dkey]["ids"]
    return [add_datas,add_ids]

# 解析测试步骤文件 "./steps/add_steps.yml"
def steps(tpath,calc,par1,par2,expect):
    with open(tpath,encoding="UTF-8") as f:
        lstep = yaml.safe_load(f)
    for step in lstep:
        if 'add' == step:
            result = calc.add(par1,par2)
            print("\nstep add")
        elif 'add1' == step:
            result = calc.add1(par1,par2)
            print("step add1")
        assert  expect == result

class TestCalculator:
    def setup_class(self):
        self.calc = Calculator()

    def setup(self):
        print("\n")

    def teardown(self):
        print("\n")

    """ 
        + 计算
        1.正整数
        2.大数据（亿）
        3.正小数
        4.负数
        5.零
        6.其他字符
    """
    # @pytest.mark.parametrize('num1,num2,result',
    #                          [(1, 1, 2), (100000000, 100000000, 200000000), (0.1, 0.2, 0.3), (-2, -3, -5), (0, 0, 0),
    #                           (0, 5, 5), ("sd", 1, "输入类型错误")],
    #                          ids=["int_test", "big_test", "float_test", "neg_test", "zero1_test", "zero2_test",
    #                               'other_test']
    #                          )
    @pytest.mark.parametrize('num1,num2,result',
                             get_datas("add")[0],
                             ids=get_datas("add")[1]
                             )
    def test_add(self,num1,num2,result):
        result1 = self.calc.add(num1,num2)
        assert result == result1
        print("\n计算：{0} + {1},预期：{2},计算结果：{3}".format(num1,num2,result,result1))

    """ 
        - 计算
        1.正整数
        2.大数据（亿）
        3.正小数
        4.负数
        5.零
        6.其他字符
    """
    # @pytest.mark.parametrize('num1,num2,result',
    #                          [(10,3,7),(999999999,100000000,899999999),(0.3,0.2,0.1),
    #                           (-2,-3,1),(-3,-2,-1),(0,8,-8),(8,0,8),("s",1,"输入类型错误")],
    #                          ids=["int_test","big_test","float_test",
    #                               "neg1_test","neg2_test","zero1_test","zero2_test","other_test"])
    @pytest.mark.parametrize('num1,num2,result',
                             get_datas("sub")[0],
                             ids=get_datas("sub")[1])
    def test_sub(self,num1,num2,result):
        result1 = self.calc.sub(num1, num2)
        assert result == result1
        print("\n计算：{0} - {1},预期：{2},计算结果：{3}".format(num1, num2, result, result1))

    """ 
        * 计算
        1.正整数
        2.大数据（亿）
        3.正小数
        4.负数
        5.零
        6.其他字符
    """
    # @pytest.mark.parametrize('num1,num2,result',
    #                          [(1,3,3),(9,100000000,900000000),(0.3,0.2,0.06),
    #                           (-2,-3,6),(-3,2,-6),(0,8,0),("s",1,"输入类型错误")],
    #                          ids=["int_test","big_test","float_test",
    #                               "neg1_test","neg2_test","zero1_test","other_test"])
    @pytest.mark.parametrize('num1,num2,result',
                             get_datas("mul")[0],
                             ids=get_datas("mul")[1])
    def test_mul(self,num1,num2,result):
        result1 = self.calc.mul(num1, num2)
        assert result == result1
        print("\n计算：{0} - {1},预期：{2},计算结果：{3}".format(num1, num2, result, result1))

    """ 
            / 计算
            1.正整数
            2.大数据（亿）
            3.正小数
            4.负数
            5.零
            6.其他字符
        """
    # @pytest.mark.parametrize('num1,num2,result',
    #                          [(3, 1, 3), (999999999, 9, 111111111), (0.3, 0.2, 1.5),
    #                           (-9, -3, 3), (-9, 2, -4.5), (0, 8, 0),(10,0,"除数不能为0"),("s", 1, "输入类型错误")],
    #                          ids=["int_test", "big_test", "float_test",
    #                               "neg1_test", "neg2_test", "zero1_test","zero2_test", "other_test"])
    @pytest.mark.parametrize('num1,num2,result',
                             get_datas("div")[0],
                             ids=get_datas("div")[1])
    def test_div(self,num1,num2,result):
        result1 = self.calc.div(num1, num2)
        assert result == result1
        print("\n计算：{0} - {1},预期：{2},计算结果：{3}".format(num1, num2, result, result1))

    """
        测试步骤的数据驱动
    """
    @pytest.mark.parametrize('num1,num2,expect',get_datas("add")[0],ids=get_datas("add")[1])
    def test_add_steps(self,num1,num2,expect):
        steps("./steps/add_steps.yml",self.calc,num1,num2,expect)
        # assert 2 == self.calc.add(1,1)
        # assert 3 == self.calc.add1(1, 1)
        # assert 0 == self.calc.add(1, 1)
