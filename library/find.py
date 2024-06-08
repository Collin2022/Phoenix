def searchFileInFolder(path, filename):
    import os
    for root, dirs, files in os.walk(path):
        if filename in dirs or filename in files:
            root = str(root)
            return os.path.join(root, filename)
    else:
        return False
