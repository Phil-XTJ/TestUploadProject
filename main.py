import sys
sys.path.append("C:\\Users\\MrXia\\Desktop\\Python_test\\test_dir")

import module_code as module
print("下面我将要调用模块进行实例化对象")
t = module.cla(99)
t.tt()
print("\n\n下面我将要调用模块中的函数方法")
module.test1()
