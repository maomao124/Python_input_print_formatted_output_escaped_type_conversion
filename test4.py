"""
 * Project name(项目名称)：Python_input_print_格式化输出_转义_类型转换 
 * Package(包名): 
 * File(文件名): test4
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/21 
 * Time(创建时间)： 19:20
 * Version(版本): 1.0
 * Description(描述)： 转义
 """

# 转义字符	说明
# \n	换行符，将光标位置移到下一行开头。
# \r	回车符，将光标位置移到本行开头。
# \t	水平制表符，也即 Tab 键，一般相当于四个空格。
# \a	蜂鸣器响铃。注意不是喇叭发声，现在的计算机很多都不带蜂鸣器了，所以响铃不一定有效。
# \b	退格（Backspace），将光标位置移到前一列。
# \\	反斜线
# \'	单引号
# \"	双引号
# \	在字符串行尾的续行符，即一行未完，转到下一行继续写。

if __name__ == '__main__':
    print("1\n\n\n2")
    print("1\t2\t3\t4")
    print("\a")

