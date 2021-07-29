# File ：setup.py
from setuptools import setup
setup(
    # 打包的包名
    name='pytest_encode',
    # gitbub中包的地址
    url='https://github.com/xxx/pytest-encode',
    # 版本
    version='1.0',
    # 作者
    author="dachamiao",
    # 作者邮箱
    author_email='1344232142@qq.com',
    # 描述
    description='set your encoding and logger',
    # 详细描述
    long_description='Show Chinese for your mark.parametrize(). Define logger variable for getting your log',
    classifiers=[# 分类索引  pip 对所属包的分类
        'Framework :: Pytest',  # 框架
        'Programming Language :: Python',   # 语言
        'Topic :: Software Development :: Testing', # 开发类型
        'Programming Language :: Python :: 3.8',    # 支持版本
    ],
    # 许可证="专有" 随便写
    license='proprietary',
    # 包名
    packages=['pytest_encode'],
    # 通过哪些关键词可以发现本包
    keywords=[
        'pytest', 'py.tests', 'pytest_encode',
    ],
    # 需要安装的依赖
    install_requires=[
        'pytest'
    ],
    # 入口模块 或者入口函数   入口可以直接写项目名称 也可以指定到文件或类
    entry_points={
        'pytest11': [
            'pytest-encode = pytest_encode',
        ]
    },
    # windows要加这个设置 否则会有不可预知的错误发生
    zip_safe=False
)