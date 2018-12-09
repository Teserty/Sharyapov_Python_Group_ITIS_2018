# download pdfs
import multiprocessing as mp
import re, requests
LINK = 'https://wikipedia.org/wiki/London'
TYPE = 'pdf'
pattern = r'href="(?P<url>[a-zA-Z0-9_:/.]*\.'
class FileDownloader:
    def __init__(self, url, extension):
        self.url = url
        self.pattern = pattern + extension + ')"'
        mp.freeze_support()
        self.semaphore = mp.Semaphore(3)
    def download_file(self, file_url):
        self.semaphore.acquire()
        r = requests.get(file_url)
        with open('downloads/' + file_url.split('/')[-1], 'wb') as f:
            f.write(r.content)
        self.semaphore.release()
    def download_files(self):
        p = re.compile(self.pattern)
        r = requests.get(self.url)
        for line in r.iter_lines():
            for m in p.finditer(str(line)):
                mp.Process(target=FileDownloader.download_file,
                           args=(self, m.group('url'),)).start()
if __name__ == '__main__':
    fd = FileDownloader(LINK, TYPE)
    fd.download_files()
