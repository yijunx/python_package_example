# witout this init file, the error is:

# ___________________________________________ ERROR collecting app/idgenerator/test/test_idgenerator.py ____________________________________________
# ImportError while importing test module '/Users/yijun/qrojects/python_package_example/app/idgenerator/test/test_idgenerator.py'.
# Hint: make sure your test modules/packages have valid Python names.
# Traceback:
# /usr/local/Cellar/python@3.10/3.10.8/Frameworks/Python.framework/Versions/3.10/lib/python3.10/importlib/__init__.py:126: in import_module
#     return _bootstrap._gcd_import(name[level:], package, level)
# app/idgenerator/test/test_idgenerator.py:3: in <module>
#     from ..src.idgenerator import generate_credit_card_number, generate_guid, generate_object_id, generate_password
# E   ImportError: attempted relative import with no known parent package