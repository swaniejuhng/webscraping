#사이트에서 찾은 외부 URL을 모두 리스트로 수집
allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    internalLinks = getInternalLinks(bsObj, splitAddress(domain)[0])
    externalLinks = getExternalLinks(bsObj, splitAddress(domain)[0])

    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link == "/":
            link = domain
        elif link[0:2] == "//":
            link = "http:" + link
        elif link[0:1] == "/":
            link = domain + link

        if link not in allIntLinks:
            print("About to get link : " + link)
            allIntLinks.add(link)
            getAllExternalLinks(link)

domain = "http://oreilly.com"
getAllExternalLinks(domain)
