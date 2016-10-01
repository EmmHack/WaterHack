#!/usr/bin/python

#Author : Manaileng Mabu
#Email  : manailengmj@gmail.com
#Tell   : +2715 268 2243
#Cell   : +2779 859 5080

import sys, codecs

def createDict(inFile):
	meters = []
	flst = []
	wrd = []

	number = 450450450

	for ln in inFile:
		wrd.append(ln)
		#for i in range(0, 10):
		#	number += 10
		#	meters.append( ln + "," + str(number))
	
	with open("city_meters.txt",'a') as filemeter:
		for m in wrd:
			number += 10
			filemeter.write(m.replace("\n",'') + "," + str(number) + "\n")

        
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
