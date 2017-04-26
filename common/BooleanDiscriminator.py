import re

def BooleanDiscriminator(equation):
	threeMarkFormat = re.sub(r"([0-9]+) *([<|>|=]+) *([0-9]+) *([<|>|=]+) *([0-9]+)",r"\1\2\3and\3\4\5",equation)
	print(threeMarkFormat)
	spaceFormat = re.sub(" +","",threeMarkFormat)
	print(spaceFormat)
	bracketFormat = re.sub(r"([0-9]+[<|>|=]+[0-9]+)",r"(\1)",spaceFormat)
	print(bracketFormat)
	andFormat = bracketFormat.replace('and','&')
	print(andFormat)
	orFormat = andFormat.replace('or','|')
	print(orFormat)
	baseBracketFormat = re.sub(r"^(.*)$",r"(\1)",orFormat) 
	formatText = baseBracketFormat

	#formatText = list(formatText)
	print(formatText)

	maxNest = 0
	nestLevel = 0
	colLevel = 0
	nestColCount = [0,0]
	result = [[[]]]
	formatText = list(formatText)
	textCount = formatText
	forCount = 1

	if formatText[0] == "(" :
		print("括弧始まり")
		formatText.pop(0)
	else:
		print("括弧じゃない！？")

	for i in formatText:
		print(i)
		print("nestLevel "+ str(nestLevel) )
		print("nestColCount "+ str(nestColCount) )
		print(result)
		print("")		
		if i == "(":
			if maxNest <= nestLevel + 1:
				nestColCount.append(0)
				result.append([[]])
				maxNest = nestLevel
			result[nestLevel][nestColCount[nestLevel]].append( str(nestLevel + 1) + "-" + str(nestColCount[nestLevel + 1]) )
			nestLevel = nestLevel + 1
		elif i == ")":
			if len(textCount) > forCount:
				print("閉じ括弧処理" + str(textCount[forCount]))
				if textCount[forCount] == "&" or textCount[forCount] == "|":
					nestColCount[nestLevel] = nestColCount[nestLevel] + 1
					result[nestLevel].append([])
				else:
					nestColCount[nestLevel] = nestColCount[nestLevel] + 1
					nestLevel = nestLevel - 1
		elif i == "&" or i == "|":
			if len(textCount) > forCount:
				result[nestLevel][nestColCount[nestLevel]].append(i)
				nestColCount[nestLevel] = nestColCount[nestLevel] + 1
				result[nestLevel].append([])
				result[nestLevel-1][nestColCount[nestLevel-1]].append( str(nestLevel) + "-" + str(nestColCount[nestLevel] - 1) )
				if textCount[forCount] == "(":
					nestLevel = nestLevel - 1
		else:
			result[nestLevel][nestColCount[nestLevel]].append(i)
		forCount = forCount + 1

	print(result)


if __name__ == "__main__":
	#BooleanDiscriminator("( 6 >10 ) or ( ( 0 < 4 <= 100) and 6> 10  )")
	BooleanDiscriminator("( ( 0 < 4 <= 100) and 6> 10  )")