\# 刷题软件 - 前端部分



\## 项目概述

基于PyQt5开发的刷题软件前端界面，包含登录注册、题目练习、错题本、数据统计等功能。



\## 技术栈

\- Python 3.6+

\- PyQt5 5.15.10



\## 项目结构

main.py # 程序主入口，包含窗口类和业务逻辑

LoginUi.py # 登录界面UI（由Qt Designer生成）

InterfaceUi.py # 主界面UI（由Qt Designer生成）



\## 功能模块



\### 1. 用户认证

\- 登录/注册界面

\- 密码可见性切换

\- 界面阴影效果和无边框设计



\### 2. 主界面功能

\- \*\*首页\*\*：科目选择（马原、思修、近代史等）

\- \*\*我的\*\*：个人信息管理

\- \*\*功能模块\*\*：

&nbsp; - 导入题目

&nbsp; - 数据统计

&nbsp; - 错题本



\### 3. 刷题功能

\- 单选题界面（含选项和答案显示）

\- 多选题界面

\- 简答题界面

\- 题目导航（上一题/下一题）



\### 4. 数据统计

\- 总刷题数、正确率、错题数、学习时长

\- 各科目正确率可视化展示

\- 模拟数据展示（需后端接入真实数据）



\### 5. 错题本

\- 错题列表

\- 错题详情查看

\- 答案和解析显示



\## 后端接口需求（ai生成，可参考）



\### 用户相关

```python

\# 登录验证

def verify\_login(account, password) -> bool



\# 用户注册  

def register\_user(account, password) -> bool



\# 获取用户信息

def get\_user\_info(user\_id) -> dict



\###题目相关

\# 获取题目列表

def get\_questions(subject, chapter) -> list



\# 提交答案

def submit\_answer(user\_id, question\_id, answer) -> bool



\# 记录错题

def record\_wrong\_question(user\_id, question\_id) -> bool



\###统计相关

\# 获取学习统计数据

def get\_statistics(user\_id) -> dict

\# 返回格式：

{

&nbsp;   "total\_questions": 156,

&nbsp;   "correct\_questions": 122, 

&nbsp;   "wrong\_questions": 34,

&nbsp;   "study\_time": "12.5h",

&nbsp;   "subject\_accuracy": {

&nbsp;       "马克思主义原理": 0.85,

&nbsp;       "思想道德与法治": 0.76,

&nbsp;       # ...

&nbsp;   }

}



\###导入相关

\# 导入题目文件

def import\_questions(file\_path, subject) -> bool



\##前端数据存储结构

\###当前用户信息

user\_now = ''  # 全局变量存储当前登录用户

\###模拟数据结构（需后端替换）

\#在 MainWindow.init\_statistics\_data() 中

self.total\_questions = 156      # 需从后端获取

self.correct\_questions = 122    # 需从后端获取  

self.wrong\_questions = 34       # 需从后端获取

self.study\_time = "12.5h"       # 需从后端获取



\###运行方式

pip install -r requirements.txt

python main.py

