import urllib.request

def downloadFilesFromURL(url, path, filename):
    print('Beginning file download for {}'.format(filename))
    fp = '{}/data/{}'.format(path, filename)
    urllib.request.urlretrieve(url, fp)
    print('Completed download of {}'.format(filename))
    return True
