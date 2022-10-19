# PYTEST

## 1. DEFINE
- A Python testing tool

## 2. INSTALL
```commandline
pip3 install -U pytest
pytest --version
pytest --help
```

## 3. INVOKE TEST:
[LINK](https://docs.pytest.org/en/7.1.x/how-to/usage.html#invoke-python)

### 3.1. Pytest tự detect:
Dùng 1 trong 2 command sau:
```commandline
pytest 
python -m pytest
```
Note: nếu dùng `pytest` --> add current dir vào sys.path (TODO-Tìm hiểu thêm sự khác nhau)
- pytest sẽ tìm các tests trong folder + sub-folder của vị trí chạy command
- Tìm các đối tượng thoả điều kiện: 
  - File: test_\*.py/\*_test.py
  - Hàm: test*
    - bên ngoài Classs
    - bên trong các Class với prefix Test*. Không tính các hàm có \_\_init__)

Một số option hỗ trợ:
- -s: hiển thị output của các hàm print
- -v: hiển thị pass, fail cho tất cả các test case
- -q: hiển thị kết quả ngắn gọn (quiet reporting)

### 3.2. Chỉ định đối tượng cụ thể
- Chỉ định một đối tượng cụ thể:
```commandline
pytest <file_name>
pytest <dir/>
pytest <file_name>::<func_name>
pytest <file_name>::<class_name>::<func_name>
pytest <dir>/<file_name>::<class_name>::<func_name>
```
- Filter theo keyword:
```commandline
pytest -k "keywordA and keyworkB not keyworkC"
```
- So sánh keyword condition để so sáng với combined identification (id: <file_name>::<class_name>::<func_name>)

- Dùng [marker](https://docs.pytest.org/en/7.1.x/example/markers.html) :
```commandline
pytest -m <marker_name>
```
Cần gán marker cho đối tượng test (class, function). Có thể dùng not/and/or để filter marker. Ví dụ: `@pytest.marker.name1`. Ngoài các marker mặc định, có thể khai báo thêm trong file `pytest.ini`:
```doctest
[pytest]
markers =
slow: marks tests as slow (deselect with '-m "not slow"')
serial
```

- Rerun failed case(s):
```commandline
pytest --lf # last-failed: chỉ chạy các case fail trong lần vừa rồi
pytest --ff # failed-first: chạy các case fail trong lần vừa rồi, sau đó chạy các case pass
```

- Note: Invoke từ code: `retcode = pytest.main()` (???)


# 4. Configuration:
- Configuration files at root dir:
  - pytest.ini --> TODO-Tìm hiểu thêm các options
  - pyproject.toml --> TODO-Tìm hiểu thêm cái này
  - tox.ini
  - setup.cfg
  - conftest.py: chứa các fixture dùng chung, các behavior chung sau khi assert fail
  
- Các option trong pytest.ini:
  - testpaths:
    List ra các folder. Giới hạn các folder tìm kiếm khi chạy `pytest`
  
  - norecursedirs: bỏ qua test trong các folder này
  
  - python_functions/python_files/python_classes
    Định nghĩa suffix, prefix để detect test functions
  
  - filterwarnings:
    Lọc các loại warning muốn hiển thị (mặc định ko filter)
    --> TODO: ignore::DeprecationWarning để loại bỏ các warning bị deprecated

# 5. Assert:
  [LINK](https://docs.pytest.org/en/7.1.x/how-to/assert.html#assert)

## 5.1. Assert statement:
```python
assert <statement>, "Message if statement = False"
```

## 5.2. Assert Exception:
## 5.3. Assert Warning:


# 6. FIXTURES:
```python
import pytest


@pytest.fixture
def init_number():
    return 10

def test_print(init_number):
    for x in range(init_number):
        print('\nLine', x)
```
- Gắn nhãn fixture cho function. Khi function khác truyền parameter có tên giống fixture function --> param sẽ được gán giá trị mà fixture function trả về
- Nguyên văn tiếng Anh - When going to run a test: 
    + looks at function’s parameters
    + searches for fixtures that have the same names as parameters
    + runs those fixtures, captures what returned (if anything), and passes those objects into function as arguments.

- Một số đặc điểm:
  - Fixtures can request other fixtures 
  - Reusable 
  - Can request many fixtures at a time 
  - Can be requested more than once per test (return values are cached)
    - --> trong cùng 1 test mỗi fixture có thể được gọi dùng nhiều lần. Nhưng giá trị khởi tạo của nó sẽ được cached lại đúng, để mỗi lần gọi đều đem giá trị khởi tạo ra sử dụng.
    Note: --> TODO-Cần check 
          Pytest only caches one instance of a fixture at a time, which means that when using a parametrized fixture, pytest may invoke a fixture more than once in the given scope.

- Các tham số của `@pytest.fixture` label:
  - autouse=True
  - scope="<scope_item>" - scope items:
    - function (default)
    - class
    - module
    - package
    - session (tất cả các test trong lần chạy)


# 8. Other
- Tear down cho fixture:
  + dùng yield thay vì 'return': các phần code dưới yield sẽ được thực hiện sau khi test kết thúc, nhưng theo reverse order của fixture

- Allure report: https://docs.qameta.io/allure-report/#_pytest
  - A.Fog vs a.Di trao đổi tài liệu gì đó liên quan allure - KUC
    - https://github.com/kintone-labs/kuc-tests/blob/master/.github/workflows/report-kuc-tests.yml
    - https://github.com/marketplace/actions/allure-report-with-history




https://docs.pytest.org/en/6.2.x/reference.html