def keywords (link):

    import requests as r
    output = r.get(link)
    code = output.text

    keyword = []
    in1 = code.find('property')
    in2 = 0
    in3 = 0
    in4 = 0
    i=0

    while i == 0 :

        in2 = code.find('content',in1+1)
        in3 = code.find('"',in2+1)
        if code[in3:code.find('"',in3+1)+1] not in keyword:
            keyword.append(code[in3:code.find('"',in3+1)+1])

        in1 = code.find('property',in1+1)

        if '<meta' not in code[in1+1:]:
            break
            
    return(keyword)


def outlinks (link):

    import requests as r
    output = r.get(link)
    code = output.text

    outlink = []
    in1 = code.find('a href')
    in2 = 0
    i=0

    while i == 0 :
        in2 = code.find('"',in1+1)

        if (code[in2:code.find('"',in2+1)+1] not in outlink) & (len(code[in2:code.find('"',in2+1)+1])<200):
             outlink.append(code[in2:code.find('"',in2+1)+1])

        if 'a href' not in code[in1+1:]:
            break

        in1 = code.find('a href',in1+1)
        
    return (outlink)




