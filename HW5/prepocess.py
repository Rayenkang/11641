import re
import json
import collections




def clean_train_set():

	def read_stop_word_list():
		f = open('stopword.list','r')
		stopword_list = []
		for line in f:
			stopword_list += [line.strip()]
		return stopword_list


	f_origin = open('toytrainset.json','r')
	fw_clean_train = open('toypreset','w')
	stopword_list = read_stop_word_list()

	for line in f_origin:
		json_content = json.loads(line)
		text = json_content.get('text')
		star = json_content.get('stars')
		clean_text = ""

		for word in text.split(' '):
			word = word.lower()
			word = re.sub(r'[^a-z]',"",word)

			if word in stopword_list:
				continue
			clean_text += word + ' '
		clean_review = {}
		clean_review['text'] = clean_text
		clean_review['stars'] = star
		fw_clean_train.write(json.dumps(clean_review) +'\n')


def create_ctf_tokens2000_list():
	f = open('toypreset','r')
	fw = open('text_file','w')

	word_counter = collections.Counter()

	for line in f:
		text = json.loads(line).get('text')
		text = text.split(' ')
		word_counter.update(text)

	word_counter.pop('')

	tokens = word_counter.most_common(2000)

	for w in tokens:
		fw.write(w[0]+'\n')
	

def create_df_tokens2000_list():
	f = open('toypreset','r')
	fw = open('text_file','w')

	word_counter = collections.Counter()

	for line in f:
		text = json.loads(line).get('text')
		text = text.split(' ')
		word_counter.update(set(text))

	word_counter.pop('')

	tokens = word_counter.most_common(2000)

	for w in tokens:
		fw.write(w[0]+'\n')


def create_ctf_feature():
	f = open('toypreset','r')
	fw = open('text_file','w')

	def read_tokens_list():
		f_tokens_list = open('ctf_top2000_tokens_list','r')

		tokens_list = {}
		for line in f_tokens_list:
			line = line.strip().split('\t')
			tokens_list[line[0]] = line[1] 

		return tokens_list

	tokens_list = read_tokens_list()
	
	tokens_set = set(tokens_list.keys())


	for line in f:
		text = json.loads(line).get('text')
		text = text.split(' ')
		word_counter = collections.Counter()
		word_counter.update(text)
		feature_set = set(text) & tokens_set

		feature = dict([(tokens_list[k], word_counter[k]) for k in feature_set])
		print feature



	








