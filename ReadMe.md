该文档放了概述以及在自动化测试过程中注意事项

概述：
    ①这是基于Windows+Apache+Mysql+php的Web项目,首先对测试环境进行搭建
    ②列出项目的功能点、子模块；对会员新增等模块还有对购物流程的业务场景编写测试用例，进行测试，测试过程中考虑到前台、后台、以及数据库相应表内数据的变化
    ③使用SQL语句对页面初始化数据与数据库内的数据进行核对测试
    ④使用python+selenium+unittist框架对注册功能进行自动化测试，最后生成对应的Html的测试结果
    ⑤使用HttpWatch Studio抓包工具对注册过程进行拦截，越过前端页面验证，修改其数据，测试数据库中是否设置了验证状态
    
注册方式采用自动化
    图片验证码识别问题
        刷新或重新加载src的验证码会改变，为了与页面保持一致，使用截图方式保存到本地，用Osr图像识别字母（成功率比较低，使用条件限制）
        
装测试用例的文件夹名字必须为Testcase

UnoDeDebug错误：“GBK”编解码器不能解码位置14中的字节0x89:非法多字节序列
可能是解码的时候读取文件和编辑器所用的编码导致的（我读取的文档是UTF - 8，但pycharm是GBK）
解决方法：在读取CSV文件中的open方法中加上encoding = "UTF-8"

在testcase.py中只运行test_suit函数，则只会执行测试套件中加入的测试用例

测试用例必须放在Testcase文件夹下，在testsuit导入类时，必须为from Testcase... import Testcase

HttpWatch越过前端限制，验证数据库是否设置了验证

在Testcase1文件夹想创建一个新的py文件存储email格式错误的测试用例，命名为email.py,结果在自动化测试时会报错，module 'http' has no attribute 'client'，原因：email是系统关键字，不能作为文件名称
