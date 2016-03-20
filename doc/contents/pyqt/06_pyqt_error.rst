.. highlight:: rst

PyQt新手犯错
=======================

本文将自己学习PyQt的新手阶段犯错的东西记录下来

连接slot槽函数时加了括号
------------------------------------
self.tsWork.procegressBarSignal.connect(self.setProcegressBar)
错误的写法： self.tsWork.procegressBarSignal.connect(self.setProcegressBar())