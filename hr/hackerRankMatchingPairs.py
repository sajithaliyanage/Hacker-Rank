# Enter your code here. Read input from STDIN. Print output to STDOUT
l_dic = {
			'a':0,
			'b':0,
			'c':0,
			'd':0,
			'e':0,
			'f':0,
			'g':0,
			'h':0,
			'i':0,
			'j':0,
			'k':0,
			'l':0,
			'm':0,
			'n':0,
			'o':0,
			'p':0,
			'q':0,
			'r':0,
			's':0,
			't':0,
			'u':0,
			'v':0,
			'w':0,
			'x':0,
			'y':0,
			'z':0
		}


def no_wrds_in_wrd(wrd):
	tmp_lst = []
	tmp_l_lst = []
	for l in wrd:
		if l not in tmp_l_lst:
			l_no = 0
			for l2 in wrd:
				if l2 == l:
					l_no += 1
			tmp_l_lst.append(l)
			tmp_lst.append(l_no)
		else:
			tmp_lst.append(l_dic[l])
	print tmp_lst
	return tmp_lst
				

N = input()
m_lst = []
while N > 0:
	_wrd = raw_input()
	_wrd = _wrd.strip()
	tmp_wrd = no_wrds_in_wrd(_wrd)
	s_tmp_wrd = tmp_wrd
	m_lst.append(s_tmp_wrd)
	N -= 1
mtaching_pairs = 0
start = 1
for token in m_lst:
	for token2 in m_lst[start:]:
		if token == token2:
			mtaching_pairs += 1
            
	start += 1		
print mtaching_pairs
