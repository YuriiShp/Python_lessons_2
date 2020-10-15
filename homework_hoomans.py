from datetime import date


class People:

    def __init__(self, filename):
        with open(filename) as f:
            self.data = f.read().split('\n')

    def older_then(self, age):
        res = []
        for line in self.data:
            if line:
                name, last, bd = line.split()
                birh_day = bd.split('.')
                today = date.today().strftime(r'%d.%m.%Y').split('.')
                years = int(today[2]) - int(birh_day[2])
                if int(today[1]) < int(birh_day[1]):
                    years -= 1
                elif int(today[1]) == int(birh_day[1]):
                    if int(today[0]) < int(birh_day[0]):
                        years -= 1
                if years >= age:
                    res.append(line)
        return res

    def younger_then(self, age):
        res = []
        for line in self.data:
            if line:
                name, last, bd = line.split()
                birh_day = bd.split('.')
                today = date.today().strftime(r'%d.%m.%Y').split('.')
                years = int(today[2]) - int(birh_day[2])
                if int(today[1]) < int(birh_day[1]):
                    years -= 1
                elif int(today[1]) == int(birh_day[1]):
                    if int(today[0]) < int(birh_day[0]):
                        years -= 1
                if years < age:
                    res.append(line)
        return res


peop_list = People('hoomanlist.txt')
print(peop_list.older_then(30))
print(peop_list.younger_then(30))
