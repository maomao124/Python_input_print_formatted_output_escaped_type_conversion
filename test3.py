"""
 * Project name(项目名称)：Python_input_print_格式化输出_转义_类型转换 
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/21 
 * Time(创建时间)： 19:05
 * Version(版本): 1.0
 * Description(描述)： 格式化输出
 """
# 转换说明符     	解释
# %d、%i	转换为带符号的十进制整数
# %o	转换为带符号的八进制整数
# %x、%X	转换为带符号的十六进制整数
# %e	转化为科学计数法表示的浮点数（e 小写）
# %E	转化为科学计数法表示的浮点数（E 大写）
# %f、%F	转化为十进制浮点数
# %g	智能选择使用 %f 或 %e 格式
# %G	智能选择使用 %F 或 %E 格式
# %c	格式化字符及其 ASCII 码
# %r	使用 repr() 函数将表达式转换为字符串
# %s	使用 str() 函数将表达式转换为字符串

if __name__ == '__main__':
    n1 = 3
    print("数字：%d" % n1)
    n2 = 4
    n3 = 8
    print("数字：%d,%d,%d" % (n1, n2, n3))
    # 指定最小输出宽度
    # 当使用表1中的转换说明符时，可以使用下面的格式指定最小输出宽度（至少占用多少个字符的位置）：
    # %10d 表示输出的整数宽度至少为 10；
    # %20s 表示输出的字符串宽度至少为 20。
    n = 1234567
    print("%10d" % n)
    print("%5d" % n)

    # 指定对齐方式
    # 标志	说明
    # -	指定左对齐
    # +	表示输出的数字总要带着符号；正数带+，负数带-。
    # 0	表示宽度不足时补充 0，而不是补充空格。
    n = 123456
    # %09d 表示最小宽度为9，左边补0
    print("%09d" % n)
    # %+9d 表示最小宽度为9，带上符号
    print("%+9d" % n)
    f = 140.5
    # %-+010f 表示最小宽度为10，左对齐，带上符号
    print("%-+010f" % f)
    s = "Hello"
    # %-10s 表示最小宽度为10，左对齐
    print("%-10s." % s)
    # 指定小数精度
    f = 3.1415926
    print("%8.4f" % f)
    input()