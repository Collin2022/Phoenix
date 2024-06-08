def installLibrary(libraryname:str, mirror:str="https://mirrors.tuna.tsinghua.edu.cn/", args:str="") -> None:
    """
    使用pip安装依赖库
    :param libraryname: PIP库的ID(大多数情况下是库名称)
    :param mirror: PIP库安装镜像(默认为清华镜像源)
    :param args: PIP安装的额外参数
    """
    import os
    os.system("pip install {libraryname} -i {mirror} {args}")

def uninstallLibrary(libraryname:str, args:str="") -> None:
    """
    使用pip安装依赖库
    :param libraryname: PIP库的ID(大多数情况下是库名称)
    :param args: PIP安装的额外参数
    """
    import os
    os.system("pip uninstall {libraryname} {args}")

def pipUpdate() -> None:
    """
    自动升级pip安装器
    """
    import os
    os.system("python -m pip install pip --upgrade")

def downloadLibrary(libraryname:str, args:str) -> None:
    """
    使用pip安装whl文件
    :param libraryname: PIP库的ID(大多数情况下是库名称)
    :param args: PIP安装的额外参数
    """
    import os
    os.system("pip download {libraryname} {args}")
