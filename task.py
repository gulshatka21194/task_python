import argparse

def read_from_file(filename):
	try:
		with open(filename) as file:
			strs = [line.strip() for line in file]
			return strs
	except IOError:
		print('No file', filename)
		return 0

def replace_text(configs, texts):
	d = dict()
	for text in texts:
		counter = 0
		for conf in configs:
			conf = conf.split('=')
			counter += text.count(conf[0])
			text = text.replace(conf[0], conf[1])
		d[counter] = text
	return d

def sort_dict(d):
	return list(dict(sorted(d.items(), key=lambda x: x[0], reverse=True)).values())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='input/config.txt', help='config file')
    parser.add_argument('--text', type=str, default='input/text.txt', help='text file')
    opt = parser.parse_args()

    configs = read_from_file(opt.config)
    texts = read_from_file(opt.text)
    if configs != 0 and texts != 0:
    	print('\n'.join(sort_dict(replace_text(configs, texts))))
