# test_all.py（LH816专属版，无错误）
import pytest
from python_exercises import (
    find_duplicates, difference_set, square_tuple,
    merge_dicts, ToDo, flatten_list_once
)

# 测试找重复元素
def test_find_duplicates():
    assert set(find_duplicates([1,2,2,3,4,4])) == {2,4}
    assert find_duplicates([1,2,3]) == []

# 测试集合差集
def test_difference_set():
    assert difference_set({1,2,3},{2,3,4}) == {1}
    assert difference_set({1},{1}) == set()

# 测试元组平方
def test_square_tuple():
    assert square_tuple((1,2,3)) == (1,4,9)
    assert square_tuple(()) == ()

# 测试字典合并
def test_merge_dicts():
    d1 = {'a':1,'b':2}
    d2 = {'b':3,'c':4}
    assert merge_dicts(d1,d2) == {'a':1,'b':5,'c':4}

# 测试待办清单
def test_todo_class():
    todo = ToDo()
    todo.add_task("买牛奶")
    todo.add_task("写代码")
    assert todo.list_tasks() == ["买牛奶", "写代码"]
    todo.remove_task("买牛奶")
    assert todo.list_tasks() == ["写代码"]

# 测试扁平化列表
def test_flatten_list_once():
    assert flatten_list_once([[1,2],[3,4],5]) == [1,2,3,4,5]
    assert flatten_list_once([]) == []