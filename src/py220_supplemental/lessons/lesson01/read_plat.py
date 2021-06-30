import platform

print("Machine      :", platform.machine())
print("Version      :", platform.python_version())
print("Version tuple:", platform.python_version_tuple())
print("Compiler     :", platform.python_compiler())
print("Build        :", platform.python_build())
print("Node         :", platform.node())
print("Platform     :", platform.platform())
print("System       :", platform.system())

"""
linux:
Machine      : x86_64
Version      : 3.7.3
Version tuple: ('3', '7', '3')
Compiler     : GCC 5.4.0 20160609
Build        : ('default', 'Apr 25 2019 15:14:16')
Node         : CHQ-ANDYMI-LX
Platform     : Linux-4.4.0-17134-Microsoft-x86_64-with-debian-stretch-sid
System       : Linux

windows:
Machine      : AMD64
Version      : 3.7.2
Version tuple: ('3', '7', '2')
Compiler     : MSC v.1916 64 bit (AMD64)
Build        : ('tags/v3.7.2:9a3ffc0492', 'Dec 23 2018 23:09:28')
Node         : CHQ-ANDYMI-LX
Platform     : Windows-10-10.0.17134-SP0
System       : Windows
"""
