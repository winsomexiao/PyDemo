.. highlight:: rst

Python 基础知识
====================

Python模块
----------------

   **模块是一个包含了所有你定义的函数和变量以.py结尾的文件**

   - **__name__** 属性：

      - 如果模块是被导入，__name__的值为模块名字(文件名)
      - 如果模块是被直接执行，__name__的值为’__main__’

      当我们编写Python库模块的时候，我们往往运行一些测试语句。当这个程序作为库被import的时候，我们并不需要运行这些测试语句。一种解决方法是在import之前，将模块中的测试语句注释掉。而更优美的解决方法，就是使用__name__。

   - **__doc__** 属性：

      介绍模块的功能

    **aModule.py** ::

        class aClass:
           def whoCall():
                if __name__ == '__main__':
                   print ("aClass selfcall:__name:__"+__name__)
                else:
                    print( "extern call:__name:__"+__name__)
        aClass.whoCall()


    **bModule.py** ::

        from aModule import aClass
        aClass.whoCall()

    直接运行aModule.py,输出如下  ::

        aClass selfcall:__name:____main__

    运行bModule.py,输出如下::

        extern call:__name:__aModule


模块包
~~~~~~~~~~~~~~~~~~~~~~

.. sidebar:: 模块包
    :subtitle: 模块包示意

    .. image:: images\python_moudlepackage.jpg


- 该文件夹中必须包含一个__init__.py的文件，提醒Python，该文件夹为一个模块包。__init__.py可以是一个空文件。
- 可以将功能相似的模块放在同一个文件夹中，构成一个模块包。通过import ModulePackage.aModule 引入ModulePackage模块包中的module模块。