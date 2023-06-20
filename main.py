
class Task:
    def __init__(self, taskid, status, title, content):
        self.taskid = taskid
        self.status = status
        self.title = title
        self.content = content


currentTaskDictionary = dict()
doneTaskDictionary = dict()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')
