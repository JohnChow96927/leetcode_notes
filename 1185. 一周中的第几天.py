"""
给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。
输入为三个整数：day、month 和year，分别表示日、月、年。
您返回的结果必须是这几个值中的一个
{"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}。
示例 1：
输入：day = 31, month = 8, year = 2019
输出："Saturday"
示例 2：
输入：day = 18, month = 7, year = 1999
输出："Sunday"
示例 3：
输入：day = 15, month = 8, year = 1993
输出："Sunday"

提示：
给出的日期一定是在1971到2100年之间的有效日期。
"""


def dayOfTheWeek(day: int, month: int, year: int) -> str:
    # 1971-1-1 Friday 星期五, 故设数组下标0为星期四
    week_day_list = ['Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday']
    month_day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    days_past = 0
    days_past += 365 * (year - 1971) + (year - 1969) // 4   # 计算之前年数*365 + 闰年数(不会是2100年)
    days_past += sum(month_day_list[: month - 1])   # 计算year年已度过完整的月数对应的总天数, 累加
    if year % 4 == 0 and year != 2100 and month >= 3:   # 如果当前year是闰年且当前已度过2月, 则加1
        days_past += 1
    days_past += day    # 将当前月已度过的天数加上
    return week_day_list[days_past % 7]

