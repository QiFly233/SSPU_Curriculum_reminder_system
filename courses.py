import re


class Courses:
    def handle(self, log):
        log = log.split('activity = new TaskActivity(')
        course_dict = {}
        course_list = []
        for i in range(1, len(log)):
            course_info = re.findall('".*?","(.*?)",".*?","(.*?)",".*?","(.*?)",".*?","",""\\)', log[i])
            course_time = re.findall('index =(.*?)\\*unitCount\\+(.*?);', log[i])
            course_dict = {
                '教师': course_info[0][0],
                '学科名称': course_info[0][1],
                '教室': course_info[0][2],
                '周': course_time[0][0],
                '节次': str(int(course_time[0][1]) + 1) + '-' + str(int(course_time[-1][1]) + 1)
            }
            course_list.append(course_dict)
        return course_list

course = Courses()