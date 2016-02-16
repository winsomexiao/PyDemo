.. highlight:: rst

Sphinx写笔记
========================

Sphinx写笔记体现在两个方面
  - 能生成python项目里面代码的API文档，使用 :program:`sphinx-apidoc`

  - 能将手工编写的*.rst文件转换成html网页， :program:`make html`

Sphinx配置
--------------------
  - 安装 Sphinx，使用  :program:`$ pip3 install Sphinx`

  - 为项目生成文档，使用 :program:`sphinx-quickstart` ，本文中以 :file:`d:/project/pyDemo/doc` 作为根目录
    这里生成的时候要注意，向导要求指定的根目录我喜欢在项目目录下建一个doc文档，专门放sphinx的相关文件。
    向导运行完毕后，我建立的文档结构如下

   .. image:: images/Sphinx_Folder.jpg

  - 修改 :file:`doc/conf.py`  :file:`sys.path.insert(0, os.path.abspath('..'))`

  - doc目录下的index.rst作为主页文件，人工按需要修改，修改成自己需要的样子，把各个*.rst串起来，形成一本笔记

  - 在项目路径下执行（此处是 :file:`d:/project/pyDemo/` )
    :program:`sphinx-apidoc   -o ./doc  .`
    生成api文档（rst格式）,不要遗忘最后的点，表示当前项目目录下寻找代码模块并生成API文档
    如果不需要生成API文档，此步可以跳过

  - 将rst文件转换生成html网页文件，在项目路的文档径下执行如下命令（此处是 :file:`d:/project/pyDemo/doc`)
    :program:`make html`

Sphinx语法参考
------------------------
  - http://pm.readthedocs.org/doc/sphinx.html#id11
  - http://sphinx-doc-zh.readthedocs.org/en/latest/contents.html
  - http://jwch.sdut.edu.cn/book/tool/UseSphinx.html
  - http://avnpc.com/pages/writing-best-documentation-by-sphinx-github-readthedocs
  - http://ju.outofmemory.cn/entry/64265


在PyCharm中配置Sphinx的外部工具
----------------------------------

为了将在编码过程中将文档记录下来，在PyCharm中集成Sphinx的外部工具，在项目里面随时写文档，并转换成html，这里配置两个外部工具，见如下截图

 .. image:: images/PyCharm_Sphinx_Setting.jpg

上传项目到Github
------------------------
在GitHub上注册一个用户，然后新建一个repository, 使用pycharm先pull下代码，然后再push上去

 .. image:: images/PyCharm_Github.jpg

首先在github->settings->Webhooks services->add services ->ReadTheDocs,激活这个选项。

 .. image:: images/Github_ReadTheDocs.jpg

 .. image:: images/ReadTheDocs_Import.jpg


修改ReadTheDocs中的设置
------------------------
需要修改ReadTheDocs中的conf.py的路径配置，设置为实际项目中的路径，本处就是  :file:`doc/conf.py`
现在就可以在ReadTheDocs网页上看生成的笔记了。
