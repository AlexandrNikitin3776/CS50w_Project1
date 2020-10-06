import re


def convert(mdtext):
    textlist = re.split("\n\n|\r\n\r\n|\r\n", mdtext)
    # print(textlist)
    ulflag = False
    for i in range(len(textlist)):
        # hyperlinks
        pat = re.compile(r"\[(?P<text>.[^]]+)\]\((?P<link>.[^)]+)\)")
        mh = pat.search(textlist[i])
        while mh:
            newpat = re.compile(f"\[{mh.group('text')}\]\({mh.group('link')}\)")
            textlist[i] = re.sub(
                newpat,
                f"<a href=\"{mh.group('link')}\">{mh.group('text')}</a>",
                textlist[i],
            )
            mh = pat.search(textlist[i])

        # bold
        pat = re.compile(r"\*\*(?P<text>.[^*]+)\*\*")
        mb = pat.search(textlist[i])
        while mb:
            newpat = re.compile(f"\*\*{mb.group('text')}\*\*")
            textlist[i] = re.sub(
                newpat, f"<strong>{mb.group('text')}</strong>", textlist[i]
            )
            mb = pat.search(textlist[i])
        # ul li
        pat = re.compile(r"^\* (?P<li>.+)$")
        m = re.match(pat, textlist[i])
        if m:
            textlist[i] = "".join(["<li>", m.group("li"), "</li>"])
            if not ulflag:
                textlist[i] = "".join(["<ul>\n", textlist[i]])
                ulflag = True
            continue
        elif ulflag:
            textlist[i - 1] += "\n</ul>"
            ulflag = False
        # h1
        pat = re.compile(r"^# (?P<h1>.+)$")
        m = re.match(pat, textlist[i])
        if m:
            textlist[i] = "".join(["<h1>", m.group("h1"), "</h1>"])
            continue
        # h2
        pat = re.compile(r"^## (?P<h2>.+)$")
        m = re.match(pat, textlist[i])
        if m:
            textlist[i] = "".join(["<h2>", m.group("h2"), "</h2>"])
            continue
        # h3
        pat = re.compile(r"^### (?P<h3>.+)$")
        m = re.match(pat, textlist[i])
        if m:
            textlist[i] = "".join(["<h3>", m.group("h3"), "</h3>"])
            continue
        # h4
        pat = re.compile(r"^#### (?P<h4>.+)$")
        m = re.match(pat, textlist[i])
        if m:
            textlist[i] = "".join(["<h4>", m.group("h4"), "</h4>"])
            continue
        # h5
        pat = re.compile(r"^##### (?P<h5>.+)$")
        m = re.match(pat, textlist[i])
        if m:
            textlist[i] = "".join(["<h5>", m.group("h5"), "</h5>"])
            continue
        # h6
        pat = re.compile(r"^###### (?P<h6>.+)$")
        m = re.match(pat, textlist[i])
        if m:
            textlist[i] = "".join(["<h6>", m.group("h6"), "</h6>"])
            continue
        # p
        textlist[i] = "".join(["<p>", textlist[i], "</p>"])
    return "\n".join(textlist)
