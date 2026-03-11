# python_exercises.py（LH816专属版，无错误）
# 1. 找列表重复元素
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

# 2. 集合差集
def difference_set(a, b):
    return a - b

# 3. 元组元素平方
def square_tuple(tpl):
    return tuple(num * num for num in tpl)

# 4. 合并字典并累加值
def merge_dicts(d1, d2):
    merged = d1.copy()
    for key, value in d2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

# 5. 待办清单类
class ToDo:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        if isinstance(task, str) and task.strip() != "":
            self.tasks.append(task.strip())
    def remove_task(self, task):
        task_clean = task.strip()
        if task_clean in self.tasks:
            self.tasks.remove(task_clean)
    def list_tasks(self):
        return self.tasks.copy()

# 6. 扁平化嵌套列表（一层）
def flatten_list_once(lst):
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(item)
        else:
            flattened.append(item)
    return flattened