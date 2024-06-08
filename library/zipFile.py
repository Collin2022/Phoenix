def loadZipfile(zip_path, dir_path):
    """
    zip 文件解压
    :param zip_path: zip 压缩包路径
    :param dir_path: 解压路径
    :return:
    """
    import zipfile
    f = zipfile.ZipFile(zip_path, 'r')  # 压缩文件位置
    for file in f.namelist():
        f.extract(file, dir_path)  # 解压位置
    f.close()


def compression_zip(dir_path, out_put_zip_path):
    """
    压缩指定文件夹
    :param dir_path: 目标文件夹路径
    :param out_put_zip_path: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    import os, zipfile
    # 目录切换
    os.chdir(dir_path)
    zip_ = zipfile.ZipFile(out_put_zip_path, "w", zipfile.ZIP_DEFLATED)  # outFullName为压缩文件的完整路径
    for path, dir_names, filenames in os.walk("./"):
        # 过滤 .git 文件夹
        new_root = path.replace("\\", "/")
        for filename in filenames:
            file_path = f"{new_root}/{filename}"
            if not os.path.exists(file_path):
                continue
            zip_.write(os.path.join(new_root, filename))
    zip_.close()


def compression_zip_files(file_list, out_put_zip_path):
    """
    压缩多个文件
    :param file_list: 目标文件列表路径
    :param out_put_zip_path: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    import zipfile, os
    zip_ = zipfile.ZipFile(out_put_zip_path, "w", zipfile.ZIP_DEFLATED)  # outFullName为压缩文件的完整路径
    for file_name in file_list:
        if not os.path.exists(file_name):
            continue
        zip_.write(file_name)
    zip_.close()