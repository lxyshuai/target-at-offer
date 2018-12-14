# coding=utf-8
"""
题目描述：
亲们！！我们的外国友人YZ这几天总是睡不好,初中奥数里有一个题目一直困扰着他,特此他向JOBDU发来求助信,希望亲们能帮帮他。问题是：求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数。

输入：
输入有多组数据,每组测试数据为一行。

每一行有两个整数a,b(0<=a,b<=1,000,000,000)。

输出：
对应每个测试案例,输出a和b之间1出现的次数。

样例输入：
0 5
1 13
21 55
31 99
样例输出：
1
6
4
7

 按每一位来考虑，

    1)此位大于1，这一位上1的个数有 ([n / 10^(b+1) ] + 1) * 10^b
    2)此位等于0，为 ([n / 10^(b+1) ] ) * 10^b
    3)此位等于1，在0的基础上加上n mod 10^b + 1

    举个例子：


    30143:
    由于3>1,则个位上出现1的次数为(3014+1)*1
    由于4>1,则十位上出现1的次数为(301+1)*10
    由于1=1，则百位上出现1次数为(30+0)*100+(43+1)
    由于0<1，则千位上出现1次数为(3+0)*1000

    注:以百位为例，百位出现1为100~199，*100的意思为单步出现了100~199，100次，*30是因为出现了30次100~199,+(43+1)是因为左后一次301**不完整导致。
    如果还不懂，自己拿纸和笔大致写下，找下规律，就能推导出来了！
"""


class Solution(object):
    def count_number_of_one_between_number1_and_number2(self, number1, number2):
        def count_one(number):
            count = 0
            number_list = map(int, list(str(number)))
            for index, each_number in enumerate(number_list):
                after = len(number_list) - index - 1
                if each_number == 0:
                    count += (number / 10 ** (after + 1)) * 10 ** after
                elif each_number == 1:
                    count += (number / 10 ** (after + 1)) * 10 ** after + number % (10 ** after) + 1
                else:
                    count += (number / 10 ** (after + 1) + 1) * 10 ** after
            return count

        return count_one(number1) - count_one(number2)


if __name__ == '__main__':
    print Solution().count_number_of_one_between_number1_and_number2(12, 0)
