import webbrowser,sys,pyperclip
sys.argv
if len(sys.argv)>1:
    address=' '.join(sys.argv[1:])
else:
    address=pyperclip.paste()
    print (address)
    
webbrowser.open('https://'+address)
#webbrowser.open('https:'+sys.argv[1]) #Both Works