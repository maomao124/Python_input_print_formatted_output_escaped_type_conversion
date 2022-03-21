"""
 * Project name(项目名称)：Python_input_print_格式化输出_转义_类型转换 
 * Package(包名): 
 * File(文件名): test5
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/21 
 * Time(创建时间)： 19:22
 * Version(版本): 1.0
 * Description(描述)： 类型转换
 """
# 函 数	作 用
# int(x)	将 x 转换成整数类型
# float(x)	将 x 转换成浮点数类型
# complex(real，[,imag])	创建一个复数
# str(x)	将 x 转换为字符串
# repr(x)	将 x 转换为表达式字符串
# eval(str)	计算在字符串中的有效 Python 表达式，并返回一个对象
# chr(x)	将整数 x 转换为一个字符
# ord(x)	将一个字符 x 转换为它对应的整数值
# hex(x)	将一个整数 x 转换为一个十六进制字符串
# oct(x)	将一个整数 x 转换为一个八进制的字符串

if __name__ == '__main__':
    str1 = "123"
    print(str1)
    print(type(str1))
    n1 = int(str1)
    print(n1)
    print(type(n1))
    n2 = float(str1)
    print(n2)
    print(type(n2))
    n3 = chr(n1)
    print(n3)
    print(type(n3))
    n4 = hex(n1)
    print(n4)
    print(type(n4))
    n5 = oct(n1)
    print(n5)
    print(type(n5))
