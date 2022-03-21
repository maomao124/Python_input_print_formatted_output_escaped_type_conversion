"""
 * Project name(项目名称)：Python_input_print_格式化输出_转义_类型转换 
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/21 
 * Time(创建时间)： 18:51
 * Version(版本): 1.0
 * Description(描述)： input
 """

if __name__ == '__main__':
    a = input("Enter a number: ")
    b = input("Enter another number: ")
    print(a)
    print(b)
    print(type(a))
    print(type(b))

    c = a + b
    print(c)
    a = int(a)
    b = int(b)
    c = a + b
    print(c)
