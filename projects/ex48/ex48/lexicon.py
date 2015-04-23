import string

def convert_int(s):
    try:
        return int(s)
    except ValueError:
        return None

def convert_number(s):
    if s.isdigit():
        return int(s)
    else:
        return None


def scan(words):
    dic = {'direction': ['north', 'east', 'west', 'south'], 
            'verb': ['go', 'kill', 'eat'],
            'stop': ['the', 'in', 'of'],
            'noun': ['bear', 'princess']
    }

    list_r = []
    list_word = words.split()
    for word in list_word:
        type_r = 'error'
        word_int = convert_number(word)
        if word_int != None:
            type_r = 'number'
            word = word_int
        else:
            word_lower = word.lower()
            for k in dic:
                if word_lower in dic[k]:
                    type_r = k
                    word = word.lower()
                    break
        list_r.append((type_r, word))

    return list_r


