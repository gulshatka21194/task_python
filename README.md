# task_python
Описание задания:

Get a list of pairs from a configuration file (sample configuration file is provided below), and replace value1 by value2 for all matches in a given text file (sample text file is provided below). All values in configuration file are unique; no need to take care of preventing change of already changed value. Names of both files are passed as command line arguments. Sort changed lines by the total number of symbols replaced, starting from the most changed line. Output resulting text to console.

Sample configuration file:

	a=z
	b=y
	c=x

Sample text file:

	jgrebk6hnae
	cnhjrfyjvth3nxr
	b#sjcf_ansvo!
	djf#aemfaaofna%


Запуск:

	$ git clone https://github.com/gulshatka21194/task_python
    	$ cd task_python
    
  	Запуск скрипта:
	$ python3 task.py --config input/config.txt --text input/text.txt
   
	Запуск тестов:
	$ python3 -m unittest test.py
