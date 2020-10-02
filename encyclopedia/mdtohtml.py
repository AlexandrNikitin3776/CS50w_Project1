import re

'''
    this package converts markdown text to html text.
    Package supports:
    - headings
        #
        ##
        ###
        ####
        #####
        ######
    - boldface text
        **Bold text**
    - unordered lists
        - li1
        - li2
        - li3
    - links
        [GitHub Pages](https://pages.github.com/)
    - paragraphs
        \n\n
'''

def convert(mdtext):
    textlist = re.split('\n\n|\r\n\r\n|\r\n', mdtext)
    print(textlist)
    ulflag = False
    for i in range(len(textlist)):
        # bold
        pat = re.compile(r'\*\*(?P<b>.+)\*\*')
        m = re.findall(pat, textlist[i])
        if m:
            for bold in m:
                textlist[i] = re.sub(pat, ''.join(['<b>', bold, '</b>']), textlist[i])
        # ul li
        pat = re.compile(r'^\* (?P<li>.+)$')
        m = re.match(pat, textlist[i])
        if m:
            textlist[i] = ''.join(['<li>', m.group('li'), '</li>'])
            if not ulflag:
                textlist[i] = ''.join(['<ul>\n', textlist[i]])
                ulflag = True
            continue
        elif ulflag:
            textlist[i - 1] += '\n</ul>'
            ulflag = False
        # h1
        pat = re.compile(r'^# (?P<h1>.+)$')
        m = re.match(pat, textlist[i])
        if m:
            textlist[i] = ''.join(['<h1>', m.group('h1'), '</h1>'])
            continue
        # h2
        pat = re.compile(r'^## (?P<h2>.+)$')
        m = re.match(pat, textlist[i])
        if m:
            textlist[i] = ''.join(['<h2>', m.group('h2'), '</h2>'])
            continue
        # h3
        pat = re.compile(r'^### (?P<h3>.+)$')
        m = re.match(pat, textlist[i])
        if m:
            textlist[i] = ''.join(['<h3>', m.group('h3'), '</h3>'])
            continue
        # h4
        pat = re.compile(r'^#### (?P<h4>.+)$')
        m = re.match(pat, textlist[i])
        if m:
            textlist[i] = ''.join(['<h4>', m.group('h4'), '</h4>'])
            continue
        # h5
        pat = re.compile(r'^##### (?P<h5>.+)$')
        m = re.match(pat, textlist[i])
        if m:
            textlist[i] = ''.join(['<h5>', m.group('h5'), '</h5>'])
            continue
        # h6
        pat = re.compile(r'^###### (?P<h6>.+)$')
        m = re.match(pat, textlist[i])
        if m:
            textlist[i] = ''.join(['<h6>', m.group('h6'), '</h6>'])
            continue
        # p
        textlist[i] = ''.join(['<p>', textlist[i], '</p>'])
    return '\n'.join(textlist)


text = '# Git\n\nGit is a \n\n* version\n\n* **control** \n\ntool that can be used to keep track of versions of a software project.\n\n## GitHub\n\nGitHub is an online service for hosting git repositories.'
print(convert(text))


