"""
 * Project name(项目名称)：Python_input_print_格式化输出_转义_类型转换 
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/21 
 * Time(创建时间)： 18:55
 * Version(版本): 1.0
 * Description(描述)： print()函数
 print (value,...,sep='',end='\n',file=sys.stdout,flush=False)

 """

if __name__ == '__main__':
    user_name = '123'
    user_age = 19
    # 同时输出多个变量和字符串
    print("名：", user_name, "年龄：", user_age)
    # 同时输出多个变量和字符串，指定分隔符
    print("名：", user_name, "年龄：", user_age, sep='-   -')

    # 设置end 参数，指定输出之后不再换行
    print("hello\t", end="")
    print(4, "\t", end="")
    print(2.99, end="")
    print()
    print("hello", end="\t")
    print(4, end="\t")
    print(2.99, end="\t")

    file = open("test2.txt", "a")
    print("hello", file=file)
