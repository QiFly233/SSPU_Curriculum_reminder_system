import re
from login import login


class Courses:
    def __init__(self):
        self.log = login.login_course()
        print(self.log)

    def handle(self):
        log = self.log.split('activity = new TaskActivity(')
        course_list = []
        course_query_list = {}
        for i in range(1, len(log)):
            course_info = re.findall('".*?","(.*?)",".*?","(.*?)",".*?","(.*?)",".*?","",""\\)', log[i])
            course_time = re.findall('index =(.*?)\\*unitCount\\+(.*?);', log[i])
            time = ''
            for j in range(len(course_time)):
                time = time + course_time[j][1] + ','
            course_dict = {
                '教师': course_info[0][0],
                '学科名称': course_info[0][1],
                '教室': course_info[0][2],
                '周': course_time[0][0],
                '节次': time
            }
            course_list.append(course_dict)
            course_detail_dict = {
                time:
                    {
                        '教师': course_info[0][0],
                        '学科名称': course_info[0][1],
                        '教室': course_info[0][2],
                    }
            }
            print(course_detail_dict)
            if not course_time[0][0] in course_query_list:
                course_query_list[course_time[0][0]] = []
            course_query_list[course_time[0][0]].append(course_detail_dict)

        print(course_query_list)
        return course_list


courses = Courses()
courses.handle()