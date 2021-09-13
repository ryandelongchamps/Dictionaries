def main():
    file = open('info_security.txt','r')
    r = file.read()
    finfile = open('encrypted_file','w')
    text = []

    dict = {'A': '1','a': '2','B':'3','b':'4','C':'5','c':'6','D':'7','d':'8','E':'9','e':'0','F':'Q','f':'q','G':'W','g':'w','H':'E','h':'e','I':'r','i':'R','J':'?','j':'/','K':'.','k':'>','L':'T','l':'"','M':'y','m':'Y','N':'=','n':'+','O':'-','o':'_','P':')','p':'(','Q':'*','q':'&','R':'^','r':'%','S':'$','s':'#','T':'@','t':'!','U':'V','u':'X','V':'|','v':'B','W':';','w':':','X':'i','x':'p','Y':'s','y':'a','Z':'g','z':'n','.':'z',':':' ',' ':'~'}
    for i in r:
        finfile.write(dict[i])

main()