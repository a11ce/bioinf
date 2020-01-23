output.ls : transliterate.py hungarian.tl   procText.ls
	python3 transliterate.py hungarian.tl < procText.ls > output.ls

procText.ls : replaceSpaces.py rawText.ls
	python3 replaceSpaces.py < rawText.ls > procText.ls

clean : 
	rm procText.ls output.ls