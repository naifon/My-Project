import hashlib

def DI(file,sha1):
    hasher = hashlib.sha256()
    with open(file, 'rb') as open_file:
        content = open_file.read()
        hasher.update(content)

    resSh1 = hasher.hexdigest()

    print(resSh1)
    if sha1 == resSh1:
        re = "The data is correct\nFile SH255:  " + str(resSh1)
    else:
        re = "The data is incorrect\nFile SH255:  " + str(resSh1)


    return re
