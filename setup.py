from setuptools import setup, find_packages
setup(
    name="spiderdata-server",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'Flask',
        'Flask-HTTPAuth',
        'gevent',
        'gevent-websocket',
        'pymysql'
    ],
)
