from BeautifulSoup import BeautifulSoup
import os
import re
import popen2
def reconstruct():
    homedir = os.getcwd()
    #tmp= homedir +  "/cache/result.html"
    #print "--------------" + tmp
    soup = BeautifulSoup(open(homedir +  "/cache/youdao.html"))
    head = BeautifulSoup(open(homedir +  "/cache/construction/head.html"))
    bodystart = BeautifulSoup(open(homedir +  "/cache/construction/body-start.txt"))
    bodyend = BeautifulSoup(open(homedir +  "/cache/construction/body-end.txt"))
    result = soup.find('div',{"id":"results"})
    sousuo = soup.find('form',{"id":"f"})
    #sousuo  = str(sousuo).replace("action=\"/search\"","action=\"http://dict.youdao.com/search\"")
    #result  = str(result).replace("href=\"/example/","href=\"http://dict.youdao.com/example/")
    #os.system("echo "" > cache/result.html")
    fin,fout = popen2.popen2("tee -a cache/result.html")
    fout.write("<html>")
    fout.write(str(head))
    fout.write("<body>")
    fout.write(str(bodystart))
    fout.write("\n")
    fout.write("<div class=\"c-header\">")
    fout.write(str(sousuo))
    fout.write("</div>")
    fout.write(str(result))
    fout.write(str(bodyend))
    fout.write("</body>")
    fout.write("</html>")
    fout.close()
    #sed -i 's/text/111/g' test 
    #sed -e "s:':kd:g" iii  
    #action="/search"  ------------action="http://dict.youdao.com/search"
    #href="/example/"-----href="http://dict.youdao.com/example/"
    #result  = str(result).replace("href=\"/example/","href=\"http://dict.youdao.com/example/")
    os.system("sed -i -e 's/action=\"\/search/action=\"http:\/\/dict.youdao.com\/search/g' cache/result.html")
    os.system("sed -i -e 's/href=\"\/example/href=\"http:\/\/dict.youdao.com\/example/g' cache/result.html")
    os.system("sed -i -e 's/<\/div><\/div><\/div>/ /g' cache/result.html")
