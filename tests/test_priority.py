import pytest
from taskmanager import core


def test_add_task_stores_priority():
    tasks = core.add_task([], "Assignment", priority="high")
    assert tasks[0]["priority"] == "high"


def test_default_priority_is_medium():
    tasks = core.add_task([], "Assignment")
    assert tasks[0]["priority"] == "medium"


def test_tasks_with_priority_returns_matching_tasks():
    tasks = []
    tasks = core.add_task(tasks, "Task 1", priority="high")
    tasks = core.add_task(tasks, "Task 2", priority="low")
    tasks = core.add_task(tasks, "Task 3", priority="high")

    result = core.tasks_with_priority(tasks, "high")

    assert len(result) == 2
    assert result[0]["title"] == "Task 1"
    assert result[1]["title"] == "Task 3"


def test_invalid_priority_raises_error():
    with pytest.raises(ValueError):
        core.add_task([], "Bad Task", priority="urgent")