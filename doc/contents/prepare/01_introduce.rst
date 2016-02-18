.. highlight:: rst

准备工作介绍
====================

开发环境搭建
----------------

作为一个初学者，第一步就是搭建python的开发环境，因为我是要用pyqt包写界面的，在网上看了写文章，都是用Eric 5开发的.
所以本文主要说一下搭建环境的步骤：须先安装Python，再安装PyQt，再安装Eric或PyCharm

  - Python 3.4 ： 最原始的方式就是到Python官网 https://www.python.org/downloads/ 下载python3.4，
    但实际上学习Python有很多依赖的软件包，后续一个个安装比较麻烦，本人是新手，看人推荐是安装的Anaconda， https://www.continuum.io/downloads 里面集成了很多常用的软件包，如numpy等，不用自己一个个装。

  - PyQt5: 目前网上很多PyQt的例子还是用PyQt4写的，不过本人喜欢新东西，安装的是PyQt5， 这个直接到官网上下载就可以了。
    PyQt提供了一个QT设计师的程序，可以用来图形化的设计界面UI，但生成的.ui文件要通过pyuic命令转换成.py代码，不过可以使用Eric或PyCharm开发IDE辅助转换就很方便了。
    PyQt安装会自动安装到andconda的Anaconda3\Lib\site-packages\PyQt5下

  - Eric5 :到官网 http://eric-ide.python-projects.org/ 下载最Eric5安装包，Eric是免费的，代码提示较弱。

  .. seealso::
     具体见Eric章节

  - PyCharm5 :到官网 http://eric-ide.python-projects.org/ 下载最Eric5安装包，PyCharm是收费的，功能强大。

  .. seealso::
     具体见PyCharm章节


相关模块包概要
----------------

