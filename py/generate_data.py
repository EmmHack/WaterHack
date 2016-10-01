#!/usr/bin/python

#Author : Manaileng Mabu
#Email  : manailengmj@gmail.com
#Tell   : +2715 268 2243
#Cell   : +2779 859 5080

import sys, codecs

def createDict(inFile):
	wordList = []
	flst = []
	wrd = ""

	for ln in inFile:
		line = ln.split(",")
		print line[1]
        	#wordList.append(line)
        
#	for wrd in wordList:
 #   		chars = ''
  #  		word = wrd
   # 		#print word
    #		for char in wrd:
    #			chars = chars + char + ' '
    #			#print chars,
    #		word = word +'\t\t\t' + chars
    #		#print word
    #		flst.append(word + '\n')	     
     #           
    #	toF = codecs.open("Dict.txt","w","utf-8")
    #	toF.writelines(flst)
    #	toF.close()

if __name__ == '__main__':
        
    if len(sys.argv) < 2:
        print "Usage: " + str(sys.argv[0]) + " inputfile (.txt)"
        sys.exit()
      
    inFile = codecs.open(sys.argv[1],"r","utf-8")
        
    createDict(inFile)
