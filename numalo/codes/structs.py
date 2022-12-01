#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : handle_template.py
# @Author    : Bangguo Chen
# @Email     : mail@cbguo.com
# @Demand    : 
# @Solution  : 
#

import os
import re
from typing import Union, List


def decorator_set_get(func):
    func_name = func.__name__
    sg_name = re.sub("^get", "", func_name)
    sg_name = re.sub("^set", "", sg_name)
    flag_get_str = False
    if func_name.startswith("get_"):
        if func_name.endswith("_str"):
            flag_get_str = True
            sg_name = re.sub("_str$", "", sg_name)

    def _get(self):
        # print(f"_get, func_name: {func_name}, sg_name: {sg_name}")
        _data = getattr(self, sg_name)

        if func_name.endswith("_str"):
            return "\n".join(_data)
        return _data

    def _set(self, data):
        # print(f"_set, func_name: {func_name}, sg_name: {sg_name}")
        _data = list()
        if isinstance(data, str):
            _data = data.split("\n")
        elif isinstance(data, (list, tuple)):
            _data = data
        setattr(self, sg_name, _data)
        return True

    if func.__name__.startswith("set_"):
        return _set
    else:
        return _get


class CodeTemp(object):
    def __init__(self):
        """
        >>> ct = CodeTemp()
        >>> ct.set_start("#!/user/bin/env python\\n# -*- coding:utf-8 -*- ")
        True
        >>> ct.get_start()
        ['#!/user/bin/env python', '# -*- coding:utf-8 -*- ']
        >>> ct.get_start_str()
        '#!/user/bin/env python\\n# -*- coding:utf-8 -*- '

        >>> ct.set_description(["# description", '\"\"\"', "",'\"\"\"'])
        True
        >>> ct.get_description()
        ['# description', '\"\"\"', '', '\"\"\"']
        >>> ct.get_description_str()
        '# description\\n\"\"\"\\n\\n\"\"\"'

        """

        self._keys = [
            "_start",
            "_include_packages",
            "_description",
            "_code",
            "_test",
            "_main"
        ]
        self._start = list()
        self._include_packages = list()
        self._description = list()
        self._code = list()
        self._test = list()
        self._main = list()

        # flag_str
        self._start_flag_reg = r"\s*#\s*!/usr.*"
        self._include_packages_flag_reg = r"^\s*# \s*include\s*packages\s*"
        self._description_flag_reg = r"^\s*# \s*description\s*"
        self._code_flag_reg = r"^\s*# \s*code\s*"
        self._test_flag_reg = r"^\s*# \s*test\s*"
        self._main_flag_reg = r"^\s*# \s*__main__\s*"

    def get_match_key(self, line):

        for key in self._keys:
            key_flag_reg = f"{key}_flag_reg"
            if re.match(getattr(self, key_flag_reg), line):
                return f"{key}"
        return ""

    def load(self, file):
        with open(file, "r") as f:
            data = f.readlines()
        assert data, f"Is empty!, file: {file}"
        assert re.match(self._start_flag_reg, data[0])

        i = 0
        len_data = len(data)
        _key = ""
        while i < len_data:
            line = data[i]
            i += 1
            i_key = self.get_match_key(line)
            if i_key:
                _key = i_key
            else:
                getattr(self, _key).append(line)

    def dump(self, file):
        texts = list()

        for key in self._keys:
            val = getattr(self, key)

            if key != self._keys:
                val = [f"# {key.lstrip('_')}\n"] + val
            if key == "_code":
                val = self.remove_def(val)

            texts.extend(val)

        if isinstance(file, str):
            with open(file, "w", encoding="utf-8") as f:
                f.write("".join(texts))

    @decorator_set_get
    def set_start(self, data: Union[List, str]):
        pass

    @decorator_set_get
    def get_start(self):
        pass

    @decorator_set_get
    def get_start_str(self):
        pass

    @decorator_set_get
    def set_include_packages(self, data: Union[List, str]):
        pass

    @decorator_set_get
    def get_include_packages(self):
        pass

    @decorator_set_get
    def get_include_packages_str(self):
        pass

    @decorator_set_get
    def set_description(self, data: Union[List, str]):
        pass

    @decorator_set_get
    def get_description(self):
        pass

    @decorator_set_get
    def get_description_str(self):
        pass

    @decorator_set_get
    def set_code(self, data: Union[List, str]):
        pass

    @decorator_set_get
    def get_code(self):
        pass

    @decorator_set_get
    def get_code_str(self):
        pass

    @decorator_set_get
    def set_test(self, data: Union[List, str]):
        pass

    @decorator_set_get
    def get_test(self):
        pass

    @decorator_set_get
    def get_test_str(self):
        pass

    @decorator_set_get
    def set_main(self, data: Union[List, str]):
        pass

    @decorator_set_get
    def get_main(self):
        pass

    @decorator_set_get
    def get_main_str(self):
        pass

    def remove_def(self, val):
        _ = self
        while val:
            line = val.pop()
            if '"""' in line or "'''" in line:
                val.extend([line, "\n" * 2])
                break
            if line.startswith("def "):
                break
        return val


if __name__ == '__main__':
    ct = CodeTemp()
    ct.load("/media/root/panda/progs/cbguos/numalo/numalo/codes/template.py")

    print(f"_start: {ct.get_start()}")
    print(f"_include_packages: {ct.get_include_packages()}")
    print(f"_description: {ct.get_description()}")
    print(f"_code: {ct.get_code()}")
    print(f"_test: {ct.get_test()}")
    print(f"_main: {ct.get_main()}")
    ct.dump(os.path.join(
        "/media/root/panda/progs/cbguos/numalo/gTest/fac01", "test_template.py"
    ))

if __name__ == '__main__get':
    ct = CodeTemp()
    print(ct.set_start("# hello start"))
    print(ct.get_start())
    print(ct.get_start_str())
    print(ct.set_description("# description"))
    print(ct.get_description())
    pass
