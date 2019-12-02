from urllib.request import urlopen
from urllib.parse import unquote
import random
import re
from bs4 import BeautifulSoup
import unittest

class TestWikipedia(unittest.TestCase):
    bsObj = None
    url = None

    def test_PageProperties(self):
        global bsObj
        global url

        url = "http://en.wikipedia.org/wiki/Monty_Python"
        # 처음 100페이지를 테스트합니다
        for i in range(1, 100):
            bsObj = BeautifulSoup(urlopen(url))
            titles = self.titleMatchesURL()
            self.assertEquals(titles[0], titles[1])
            self.assertTrue(self.contentExists())
            url = self.getNextLink()
        print("Done!")

    def titleMatchesURL(self):
        global bsObj
        global url
        pageTitle = bsObj.find("h1").get_text()
        urlTitle = url[(url.index("/wiki/") + 6):]
        urlTitle = urlTitle.replace("_", " ")
        urlTitle = unquote(urlTitle)
        return [pageTitle.lower(), urlTitle.lower()]

    def contentExists(self):
        global bsObj
        content = bsObj.find("div", {"id":"mw-content-text"})
        if content is not None:
            return True
        return False

    def getNextLink(self):
        # 5장에서 설명한 방법에 따라 페이지의 링크를 무작위로 반환합니다
        global bsObj
        links = bsObj.find("div", {"id":"bodyContent"}).findAll("a", href = re.compile("^(/wiki/)((?!:).)*$"))
        link = links[random.randint(0, len(links) - 1)].attrs['href']
        print("Next link is : " + link)
        return "http://en.wikipedia.org" + link

if __name__ == '__main__':
    unittest.main()
