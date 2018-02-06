
# coding: utf-8

# In[1]:

import nltk
import re
import pprint
import glob
from operator import itemgetter
import os
import csv
import time
from more_itertools import unique_everseen


# In[2]:

#import os
#os.listdir('.')


# In[3]:

def tokenize(document):
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    return sentences


# In[4]:

def tag_sentences(sentences):
    tagged_sentences = [nltk.pos_tag(sent) for sent in sentences]
    return tagged_sentences


# In[5]:

def search(sentences, regex):
    reqts = []  
    for sent in sentences:
        reqt = ' '.join(sent)
        if re.search(regex, reqt):
            reqt = re.sub('Back to Top','',reqt)
            reqt = re.sub(r"[\[\]\__]",'',reqt)
            reqts.append(reqt)
    return reqts


# In[6]:

# eliminate stop words
def no_stop_words_lemmatize(word, wnl):
    stopwords = nltk.corpus.stopwords.words('english')
    if word not in stopwords:
        root_word = wnl.lemmatize(word)
    return root_word


# In[7]:

def process(nounWord, wnl):
    try:
        noun = nounWord.lower()
        if noun.isalpha():
            word = no_stop_words_lemmatize(noun, wnl)
            return word
        else:
            pass
    except:
        pass


# In[8]:

def entries_to_remove(entries, the_dict):
    for key in entries:
        if key in the_dict:
            del the_dict[key]


# In[9]:

def extract_chunks_backward(tagged_sent, chunk_type='NP'):
    out_sen = []
    out_senTemp = []
    source = []
    target = []
    sourceTemp = []
    targetTemp = []
    source_target = []
    
    for idx, word_pos in enumerate(tagged_sent):
        verb,pos = word_pos
        
        # find the 1st instance of a VB POS
        if pos == "VB":
            
            #idx = starting index
            i = 1   # increment backwards
            j = 0   # while loop variable
            
            # for incrementing forward
            k = idx # capture index of where we start in the sentence
            n = 1   # increment forward
            
            out_senTemp.append(verb)
            targetTemp.append(verb)
        
            while True:
            
                ## going forward for more verbs
                # store the pos of the next word
                nextWord,posNext = tagged_sent[k+n]

                # if pos of previous word is one of the following          
                if posNext=="VBN" or posNext=="VB":              
                    out_senTemp.append(nextWord)
                    targetTemp.append(nextWord)
                    n+=1
                    nextWord,posNext = tagged_sent[k+n]
                
                if posNext=="NNP" or posNext=="NN" or posNext=="NNS":
                    break

                if posNext=="CC":
                    n+=1
                    nextWord2,posNext2 = tagged_sent[k+n]
                    if posNext2=="VB":
                        out_senTemp.append(nextWord2)
                        targetTemp.append(nextWord2)
                        n+=1
                    elif posNext2=="NNP" or posNext2=="NN" or posNext2=="NNS":
                        break
                    else:
                        pass

                if posNext=="TO":
                    n+=1
                    nextWord2,posNext2 = tagged_sent[k+n]
                    if posNext2=="VB":
                        out_senTemp.append(nextWord2)
                        targetTemp.append(nextWord2)
                        n+=1
                    elif posNext2=="NNP" or posNext2=="NN" or posNext2=="NNS":
                        break
                    else:
                        pass
                
                else:
                    n+=1
                        
           
            while j == 0:                        
                        
                ## going backwards for more verbs and for subject
                # store the pos of the previous word
                prevWord,posPrev = tagged_sent[idx-i]            
                
                if posPrev==",":
                    while True: 
                        i+=1
                        prevWord,posPrev = tagged_sent[idx-i]
                        if posPrev==",":
                            break
                        else:
                            pass                    
                
                if posPrev=="VB":
                    out_senTemp.append(prevWord)
                    targetTemp.append(prevWord)
                    i+=1
                    prevWord,posPrev = tagged_sent[idx-i]
                    
                if posPrev=="RB":
                    out_senTemp.append(prevWord)
                    targetTemp.insert(0,prevWord)
                    i+=1
                    prevWord,posPrev = tagged_sent[idx-i]
                        
                elif posPrev=="TO":
                    i+=1
                    prevWord2,posPrev2 = tagged_sent[idx-i]
                    if posPrev2=="VB":
                        out_senTemp.append(prevWord2)
                        targetTemp.append(prevWord2)
                        i+=1
                    elif posPrev2=="NNP" or posPrev2=="NN" or posPrev2=="NNS":
                        while True:
                            if posPrev2=="NNP" or posPrev2=="NN" or posPrev2=="NNS":
                                if prevWord2 == "A":
                                    pass
                                else:
                                    out_senTemp.append(prevWord2)
                                    sourceTemp.append(prevWord2)
                                i+=1
                                prevWord2,posPrev2 = tagged_sent[idx-i]
                            else:
                                j = 1
                                break                              
                    elif posPrev2=="RB":
                            i+=1
                    else:
                        pass

                elif posPrev=="CC":
                    i+=1
                    prevWord2,posPrev2 = tagged_sent[idx-i]
                    if posPrev2=="VB":
                        out_senTemp.append(prevWord2)
                        targetTemp.append(prevWord2)
                        i+=1
                    else:
                        pass
                        
                elif posPrev=="NNP" or posPrev=="NN" or posPrev=="NNS":
                    while True: 
                        if posPrev=="NNP" or posPrev=="NN" or posPrev=="NNS":
                            if prevWord == "A":
                                pass
                            else:
                                out_senTemp.append(prevWord)
                                sourceTemp.append(prevWord)
                            i+=1
                            prevWord,posPrev = tagged_sent[idx-i]
                        else:
                            j = 1
                            break

                else:
                    i+=1
   
            source.append(sourceTemp)
            target.append(targetTemp)
        
            sourceTemp = []
            targetTemp = []

            out_sen.append(out_senTemp)
            out_senTemp = []
    
    source_target.append([source[0],target[0]])
            
    #return out_sen, 
    return source_target


# In[10]:

def extract_chunks_forward(tagged_sent, chunk_type='NP'):
    out_sen = []
    out_senTemp = []
    source = []
    target = []
    sourceTemp = []
    targetTemp = []
    source_target = []
    
    for idx, word_pos in enumerate(tagged_sent):
        verb,pos = word_pos
                
        # find the 1st instance of a VB POS
        if pos == "VB":

            #idx = starting inde use i as an index
            i = 1   # increment forward
            j = 0   # while loop variable
                        
            # for incrementing backward
            k = idx # capture index of where we start in the sentence
            n = 1   # increment backward
                      
            sourceTemp.append(verb)

            
            while True:
                
                prevWord,posPrev = tagged_sent[k-n] 
                
                if posPrev=="RB":
                    out_senTemp.append(prevWord)
                    sourceTemp.insert(0,prevWord)
                    n+=1
                    prevWord,posPrev = tagged_sent[k-n]
                else:
                    break
            
            
            
            while j == 0:

                # store the pos of the next word
                nextWord,posNext = tagged_sent[idx+i]

                # if pos of previous word is one of the following          
                if posNext=="VBN" or posNext=="VB":              
                    out_senTemp.append(nextWord)
                    sourceTemp.append(nextWord)
                    i+=1
                    nextWord,posNext = tagged_sent[idx+i]

                if posNext=="CC":
                    i+=1
                    nextWord2,posNext2 = tagged_sent[idx+i]
                    if posNext2=="VB":
                        out_senTemp.append(nextWord2)
                        sourceTemp.append(nextWord2)
                        i+=1
                    elif posNext=="NNP" or posNext=="NN" or posNext=="NNS":
                        if nextWord2 == "A":
                            pass
                        else:
                            out_senTemp.append(nextWord2)
                            targetTemp.append(nextWord2)
                        i+=1
                    else:
                        pass

                if posNext=="TO":
                    i+=1
                    nextWord2,posNext2 = tagged_sent[idx+i]
                    if posNext2=="VB":
                        out_senTemp.append(nextWord2)
                        sourceTemp.append(nextWord2)
                        i+=1

                elif posNext=="NNP" or posNext=="NN" or posNext=="NNS":
                    while True:
                        if posNext=="NNP" or posNext=="NN" or posNext=="NNS" or posNext=="CC"                             or posNext=="VB" or posNext=="POS":

                            if posNext=="NNP" or posNext=="NN" or posNext=="NNS":
                                if nextWord == "A":
                                    pass
                                else:
                                    out_senTemp.append(nextWord)
                                    targetTemp.append(nextWord)
                                i+=1
                                nextWord,posNext = tagged_sent[idx+i]                             

                            if posNext=="CC":
                                i+=1
                                nextWord2,posNext2 = tagged_sent[idx+i]
                                if posNext2=="NNP" or posNext2=="NN" or posNext2=="NNS":
                                    if nextWord == "A":
                                        pass
                                    else:
                                        out_senTemp.append(nextWord2)
                                        targetTemp.append(nextWord2)
                                    i+=1
                                    nextWord,posNext = tagged_sent[idx+i]                                    
                                else:
                                    j = 1
                                    break
                            if posNext=="POS":
                                out_senTemp.append(nextWord)
                                i+=1
                                nextWord,posNext = tagged_sent[idx+i] 
                            if posNext=="VB":
                                break
                        else:
                            j = 1
                            break                

                else:
                    i+=1                

            source.append(sourceTemp)
            target.append(targetTemp)
            
            sourceTemp = []
            targetTemp = []
            
            out_sen.append(out_senTemp)
            out_senTemp = []
    
    source_target.append([source[0],target[0]])
        
    #return out_sen
    return source_target


# In[ ]:




# In[11]:

if __name__ == "__main__":
    
    startTime = time.time()
    
    total_sents = 0
    total_reqts = 0
    sents_ch = 0
    reqts_ch = 0
    
    total_concepts = 0
    reqts_listTemp = []
    reqts_list = []
    dict_concepts = {}
    chapter = []
    tagged_reqts = []
    
    i = -1  # b/c first directory incremented is the main directory of the rootDir with 
            #  no files of its own, only folders

    # create .csv's for export 
    
    # Nouns 
    concepts = open(r'D:\D Drive\GMU\DAEN 690\regTechReqts\concepts.csv', 'wb')
    writer = csv.writer(concepts)
    row = "Source", "Target", "Number"
    writer.writerow(row)  

    # Requirements
    reqtFile = open(r'D:\D Drive\GMU\DAEN 690\regTechReqts\reqts.csv', 'wb')
    writer = csv.writer(reqtFile)
    row = "Chapter", "Requirement"
    writer.writerow(row)  
    
    # RDF Triples
    rdfFile = open(r'D:\D Drive\GMU\DAEN 690\regTechReqts\rdfs.csv', 'wb')
    writer = csv.writer(rdfFile)
    row = "Source", "Target", "Chapter", "Requirement"
    writer.writerow(row)  

    # Number of Sentences & Requirements per Chapter
    nums = open(r'D:\D Drive\GMU\DAEN 690\regTechReqts\num.csv', 'wb')
    writer = csv.writer(nums)
    row = "Chapter", "Num_Sents", "Num_Reqts"
    writer.writerow(row)  
    
    # All combinations of Requirements for semantic comparison
    #reqtPairs = open(r'D:\D Drive\GMU\DAEN 690\regTechReqtsTest\reqtPairs.csv', 'wb')
    #writer = csv.writer(reqtPairs)
    #row = "Reqt1", "Reqt2"
    #writer.writerow(row)   

    # read all directories and files within root directory
    rootDir = r'D:\D Drive\GMU\DAEN 690\regTechIngest' #sets directory path 

    with concepts:
        for (dirName, subdirList, fileList) in os.walk(rootDir):
            print('Found directory: %s' % dirName)
            
            for ch in subdirList:
                chapter.append(ch.split()[1])

            for fname in fileList:
                reqts_listTemp = []
               
                fn = dirName+'\\'+fname
                fileread = open(fn,'r')
                raw = fileread.read()    
                raw = unicode(raw, errors='ignore')

                sentences = tokenize(raw)
                sents_ch += len(sentences)
                total_sents += len(sentences)

                regex = r'\bshall|shall not|is required|must|requires\b'
                
                # return only sentences where regex applies
                reqts = search(sentences, regex)
                reqts_listTemp.append(reqts)
                reqts_list.append(reqts)
                reqts_ch += len(reqts)
                
                #for reqt in reqts:
                #    print reqt + '\n'

                # tokenize the text
                #sentences = tokenize(str(reqts))
                
                # create an NLTK text
                #text = nltk.Text(sentences)
                
                # tag sentences
                #tagged_sents = tag_sentences(text)
                
                # chapter number
                document = 'ch'+ chapter[i]

                # RDF stopwords
                RDFstopwords = ['thereafter', 'also', 'so']
                
                rdfFile = open(r'D:\D Drive\GMU\DAEN 690\regTechReqts\rdfs.csv', 'ab')
                with rdfFile:
                    writer = csv.writer(rdfFile)
                    
                    # extract RDFs
                    for reqt in reqts:
                        total_reqts += 1
                        sentence = tokenize(reqt)
                        text = nltk.Text(sentence)
                        tagged_sent = tag_sentences(text)
                        tagged_reqts.append(tagged_sent)

                        tagged_sent = tagged_sent.pop(0)

                        try:
                            # backward information extraction
                            backward = []
                            output_sent_bkwd = extract_chunks_backward(tagged_sent)

                            output_bkwd = output_sent_bkwd.pop(0)
                            cleaned_bkwd = []
                            for out in output_bkwd:
                                output_b = [word for word in out if word not in RDFstopwords]
                                cleaned_bkwd.append(output_b)

                            source = cleaned_bkwd[0]
                            source = list(unique_everseen(source))
                            source = ' '.join(source[::-1])

                            target = cleaned_bkwd[1]
                            target = list(unique_everseen(target))                      
                            target = ' '.join(target)
                            #print "source:", source, "; ", "target:", target, "; ", "reqt:", reqt 
                            writer.writerow([source.lower(),target.lower(),document,reqt])
                            
                            # forward information extraction
                            forward = []
                            output_sent_fwd = extract_chunks_forward(tagged_sent)

                            output_fwd = output_sent_fwd.pop(0)
                            cleaned_fwd = []
                            for out in output_fwd:
                                output_f = [word for word in out if word not in RDFstopwords]
                                cleaned_fwd.append(output_f)

                            source = cleaned_fwd[0]
                            source = list(unique_everseen(source))
                            source = ' '.join(source)
                            target = cleaned_fwd[1]
                            target = list(unique_everseen(target))
                            target = ' '.join(target)
                            #print "source:", source, "; ", "target:", target, "; ", "reqt:", reqt
                            writer.writerow([source.lower(),target.lower(),document,reqt])
                        except:
                            pass

                # tokenize the text
                sentences = tokenize(str(reqts))
                
                # create an NLTK text
                text = nltk.Text(sentences)
                
                # tag sentences
                tagged_sents = tag_sentences(text)
                
                # return only nouns
                nounList = []
                wnl = nltk.WordNetLemmatizer()

                for tagged_sent in tagged_sents:
                    nounTempList = []

                    for tagged_word in tagged_sent:
                        if tagged_word[1] == 'NN' or tagged_word[1] == 'NNP' or tagged_word[1] == 'NNS':
                            noun = process(tagged_word[0], wnl)
                            nounTempList.append(noun)
                        else:
                            try:
                                if len(nounTempList) >= 1:
                                    noun_phrase = ' '.join(nounTempList)
                                    nounList.append(noun_phrase)
                            except:
                                pass
                            nounTempList = []


                number_of_occurrences = []

                for item in nounList:
                    number_of_occurrences.append((item, nounList.count(item)))

                concepts = sorted(set(number_of_occurrences))
                concepts = sorted(concepts, key=itemgetter(0), reverse=True)

                # sum all occurrences of concepts across all text files within each Ch
                for c in concepts:
                    if c[0] in dict_concepts:
                        dict_concepts[c[0]] += c[1]
                    else:
                        dict_concepts[c[0]] = c[1]

                fileread.close()

                # remove additional words from dictionary
                additional_stopwords = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
                           's','t','u','v','w','x','y','z','ii','iii','iv','vi','vii','viii','ix','x',
                           'xi','xii','xiii','xiv', 'xv','xvi','xvii','xviii')
                entries_to_remove(additional_stopwords, dict_concepts)

                # number of nouns extracted
                total_concepts += len(dict_concepts)

                # save reqts to file
                reqtFile = open(r'D:\D Drive\GMU\DAEN 690\regTechReqts\reqts.csv', 'ab')
                with reqtFile:   
                    writer = csv.writer(reqtFile)
                    for reqt in reqts_listTemp:
                        for r in reqt:
                            rrow = document, r
                            writer.writerow(rrow)        
                reqts_listTemp = []
 
                
            # save number of sentences and requirements to file
            if i == -1:
                pass
            else:
                nums = open(r'D:\D Drive\GMU\DAEN 690\regTechReqtsTest\num.csv', 'ab')
                with nums:
                    writer = csv.writer(nums)
                    row = document, sents_ch, reqts_ch
                    writer.writerow(row)  

                sents_ch = 0
                reqts_ch = 0
                


            # save data to graph dB format
            concepts = open(r'D:\D Drive\GMU\DAEN 690\regTechReqts\concepts.csv', 'ab')        
            with concepts:
                writer = csv.writer(concepts)
                for k,v in dict_concepts.items():
                    row = k, document, str(v)
                    writer.writerow(row)
            dict_concepts = {}
            
            i += 1        
             
    print "total number of sentences:", total_sents
    print "total number of requirements:", total_reqts
    print "filter %:", 1.0-(float(total_reqts)/float(total_sents)), "%"
    #print "total number of unique concepts:", total_concepts

    endTime = time.time()
    
    print "Start Time:", startTime
    print "End Time:", endTime
    print "Total Time:", (endTime - startTime)


# In[ ]:




# In[ ]:




# In[217]:




# In[256]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:

### save reqts to file
#reqtFile = open(r'D:\D Drive\GMU\DAEN 690\regTechReqtsTest\reqts.csv', 'wb')
#with reqtFile:   
#    writer = csv.writer(reqtFile)
#    for reqt in reqts_list:
#        for r in reqt:
#           writer.writerow([r])


# In[12]:

#print reqts_list


# In[10]:

#globalList =  []
#for eachlist in reqts_list:
#    for eachitem in eachlist:
#        globalList.append(str(eachitem))


# In[21]:

#semanticList = []
#for i in range(len(globalList)-1):
#    for j in range(i+1, len(globalList)):
#        semanticList.append([globalList[i],globalList[j]])


# In[12]:

#print semanticList


# In[ ]:




# In[15]:

"""
def extract_chunks(tagged_sent, chunk_type='NP'):
    out_sen = []
    for idx, word_pos in enumerate(tagged_sent):
        word,pos = word_pos
        print word,pos

grammar = "X: {<NNP>+<MD><VB>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(text)
#print result
"""

"""
from nltk.tree import Tree
from nltk.chunk import ne_chunk
from nltk import tag
simple = []

chunks = nltk.ne_chunk(text)
for elt in chunks:
    if isinstance(elt, Tree):
        simple.append(Tree(elt.label(), [ word for word, tag in elt ]))
    else:
        simple.append( elt[0])

#print simple
"""


# In[ ]:




# In[ ]:




# In[17]:

# Python/NLTK implementation of algorithm to detect similarity between
# short sentences described in the paper - "Sentence Similarity based
# on Semantic Nets and Corpus Statistics" by Li, et al.
# Results achieved are NOT identical to that reported in the paper, but
# this is very likely due to the differences in the way the algorithm was
# described in the paper and how I implemented it.
from __future__ import division
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import brown
import math
import numpy as np
import sys

# Parameters to the algorithm. Currently set to values that was reported
# in the paper to produce "best" results.
ALPHA = 0.2
BETA = 0.45
ETA = 0.4
PHI = 0.2
DELTA = 0.85

brown_freqs = dict()
N = 0

######################### word similarity ##########################

def get_best_synset_pair(word_1, word_2):
    """ 
    Choose the pair with highest path similarity among all pairs. 
    Mimics pattern-seeking behavior of humans.
    """
    max_sim = -1.0
    synsets_1 = wn.synsets(word_1)
    synsets_2 = wn.synsets(word_2)
    if len(synsets_1) == 0 or len(synsets_2) == 0:
        return None, None
    else:
        max_sim = -1.0
        best_pair = None, None
        for synset_1 in synsets_1:
            for synset_2 in synsets_2:
               sim = wn.path_similarity(synset_1, synset_2)
               if sim > max_sim:
                   max_sim = sim
                   best_pair = synset_1, synset_2
        return best_pair

def length_dist(synset_1, synset_2):
    """
    Return a measure of the length of the shortest path in the semantic 
    ontology (Wordnet in our case as well as the paper's) between two 
    synsets.
    """
    l_dist = sys.maxint
    if synset_1 is None or synset_2 is None: 
        return 0.0
    if synset_1 == synset_2:
        # if synset_1 and synset_2 are the same synset return 0
        l_dist = 0.0
    else:
        wset_1 = set([str(x.name()) for x in synset_1.lemmas()])        
        wset_2 = set([str(x.name()) for x in synset_2.lemmas()])
        if len(wset_1.intersection(wset_2)) > 0:
            # if synset_1 != synset_2 but there is word overlap, return 1.0
            l_dist = 1.0
        else:
            # just compute the shortest path between the two
            l_dist = synset_1.shortest_path_distance(synset_2)
            if l_dist is None:
                l_dist = 0.0
    # normalize path length to the range [0,1]
    return math.exp(-ALPHA * l_dist)

def hierarchy_dist(synset_1, synset_2):
    """
    Return a measure of depth in the ontology to model the fact that 
    nodes closer to the root are broader and have less semantic similarity
    than nodes further away from the root.
    """
    h_dist = sys.maxint
    if synset_1 is None or synset_2 is None: 
        return h_dist
    if synset_1 == synset_2:
        # return the depth of one of synset_1 or synset_2
        h_dist = max([x[1] for x in synset_1.hypernym_distances()])
    else:
        # find the max depth of least common subsumer
        hypernyms_1 = {x[0]:x[1] for x in synset_1.hypernym_distances()}
        hypernyms_2 = {x[0]:x[1] for x in synset_2.hypernym_distances()}
        lcs_candidates = set(hypernyms_1.keys()).intersection(
            set(hypernyms_2.keys()))
        if len(lcs_candidates) > 0:
            lcs_dists = []
            for lcs_candidate in lcs_candidates:
                lcs_d1 = 0
                if hypernyms_1.has_key(lcs_candidate):
                    lcs_d1 = hypernyms_1[lcs_candidate]
                lcs_d2 = 0
                if hypernyms_2.has_key(lcs_candidate):
                    lcs_d2 = hypernyms_2[lcs_candidate]
                lcs_dists.append(max([lcs_d1, lcs_d2]))
            h_dist = max(lcs_dists)
        else:
            h_dist = 0
    return ((math.exp(BETA * h_dist) - math.exp(-BETA * h_dist)) / 
        (math.exp(BETA * h_dist) + math.exp(-BETA * h_dist)))
    
def word_similarity(word_1, word_2):
    synset_pair = get_best_synset_pair(word_1, word_2)
    return (length_dist(synset_pair[0], synset_pair[1]) * 
        hierarchy_dist(synset_pair[0], synset_pair[1]))

######################### sentence similarity ##########################

def most_similar_word(word, word_set):
    """
    Find the word in the joint word set that is most similar to the word
    passed in. We use the algorithm above to compute word similarity between
    the word and each word in the joint word set, and return the most similar
    word and the actual similarity value.
    """
    max_sim = -1.0
    sim_word = ""
    for ref_word in word_set:
      sim = word_similarity(word, ref_word)
      if sim > max_sim:
          max_sim = sim
          sim_word = ref_word
    return sim_word, max_sim
    
def info_content(lookup_word):
    """
    Uses the Brown corpus available in NLTK to calculate a Laplace
    smoothed frequency distribution of words, then uses this information
    to compute the information content of the lookup_word.
    """
    global N
    if N == 0:
        # poor man's lazy evaluation
        for sent in brown.sents():
            for word in sent:
                word = word.lower()
                if not brown_freqs.has_key(word):
                    brown_freqs[word] = 0
                brown_freqs[word] = brown_freqs[word] + 1
                N = N + 1
    lookup_word = lookup_word.lower()
    n = 0 if not brown_freqs.has_key(lookup_word) else brown_freqs[lookup_word]
    return 1.0 - (math.log(n + 1) / math.log(N + 1))
    
def semantic_vector(words, joint_words, info_content_norm):
    """
    Computes the semantic vector of a sentence. The sentence is passed in as
    a collection of words. The size of the semantic vector is the same as the
    size of the joint word set. The elements are 1 if a word in the sentence
    already exists in the joint word set, or the similarity of the word to the
    most similar word in the joint word set if it doesn't. Both values are 
    further normalized by the word's (and similar word's) information content
    if info_content_norm is True.
    """
    sent_set = set(words)
    semvec = np.zeros(len(joint_words))
    i = 0
    for joint_word in joint_words:
        if joint_word in sent_set:
            # if word in union exists in the sentence, s(i) = 1 (unnormalized)
            semvec[i] = 1.0
            if info_content_norm:
                semvec[i] = semvec[i] * math.pow(info_content(joint_word), 2)
        else:
            # find the most similar word in the joint set and set the sim value
            sim_word, max_sim = most_similar_word(joint_word, sent_set)
            semvec[i] = PHI if max_sim > PHI else 0.0
            if info_content_norm:
                semvec[i] = semvec[i] * info_content(joint_word) * info_content(sim_word)
        i = i + 1
    return semvec                
            
def semantic_similarity(sentence_1, sentence_2, info_content_norm):
    """
    Computes the semantic similarity between two sentences as the cosine
    similarity between the semantic vectors computed for each sentence.
    """
    words_1 = nltk.word_tokenize(sentence_1)
    words_2 = nltk.word_tokenize(sentence_2)
    joint_words = set(words_1).union(set(words_2))
    vec_1 = semantic_vector(words_1, joint_words, info_content_norm)
    vec_2 = semantic_vector(words_2, joint_words, info_content_norm)
    return np.dot(vec_1, vec_2.T) / (np.linalg.norm(vec_1) * np.linalg.norm(vec_2))

######################### word order similarity ##########################

def word_order_vector(words, joint_words, windex):
    """
    Computes the word order vector for a sentence. The sentence is passed
    in as a collection of words. The size of the word order vector is the
    same as the size of the joint word set. The elements of the word order
    vector are the position mapping (from the windex dictionary) of the 
    word in the joint set if the word exists in the sentence. If the word
    does not exist in the sentence, then the value of the element is the 
    position of the most similar word in the sentence as long as the similarity
    is above the threshold ETA.
    """
    wovec = np.zeros(len(joint_words))
    i = 0
    wordset = set(words)
    for joint_word in joint_words:
        if joint_word in wordset:
            # word in joint_words found in sentence, just populate the index
            wovec[i] = windex[joint_word]
        else:
            # word not in joint_words, find most similar word and populate
            # word_vector with the thresholded similarity
            sim_word, max_sim = most_similar_word(joint_word, wordset)
            if max_sim > ETA:
                wovec[i] = windex[sim_word]
            else:
                wovec[i] = 0
        i = i + 1
    return wovec

def word_order_similarity(sentence_1, sentence_2):
    """
    Computes the word-order similarity between two sentences as the normalized
    difference of word order between the two sentences.
    """
    words_1 = nltk.word_tokenize(sentence_1)
    words_2 = nltk.word_tokenize(sentence_2)
    joint_words = list(set(words_1).union(set(words_2)))
    windex = {x[1]: x[0] for x in enumerate(joint_words)}
    r1 = word_order_vector(words_1, joint_words, windex)
    r2 = word_order_vector(words_2, joint_words, windex)
    return 1.0 - (np.linalg.norm(r1 - r2) / np.linalg.norm(r1 + r2))

######################### overall similarity ##########################

def similarity(sentence_1, sentence_2, info_content_norm):
    """
    Calculate the semantic similarity between two sentences. The last 
    parameter is True or False depending on whether information content
    normalization is desired or not.
    """
    return DELTA * semantic_similarity(sentence_1, sentence_2, info_content_norm) +         (1.0 - DELTA) * word_order_similarity(sentence_1, sentence_2)
        
######################### main / test ##########################


# In[16]:

len(semanticList)


# In[24]:

for sent_pair in semanticList[:10]:
    print "%s\t%s\t%.3f\t%.3f" % (sent_pair[0], sent_pair[1], 
        similarity(sent_pair[0], sent_pair[1], False),
        similarity(sent_pair[0], sent_pair[1], True))


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[10]:

concept = [c for c in concepts if c[1]>19]
print concept


# In[11]:

print concepts


# In[12]:

for c in concepts:
    print document, c[0], c[1]


# In[13]:

myFile = open('concepts.csv', 'wb')

with myFile:
    writer = csv.writer(myFile)
    for c in concepts:
        row = document, str(c[0]), str(c[1])
        writer.writerow(row)


# In[14]:

list1 = [('bank', 23), ('obligation', 7), ('income', 7), ('insurance', 7), ('interest', 5), ('investment', 5), ('payment', 5)]


# In[15]:

list2 = [('bank', 3), ('credit', 2), ('income', 2), ('insurance', 2), ('life', 2), ('back', 1), ('compensation', 1), ('director', 1), ('distribution', 1), ('employee', 1)]


# In[16]:

dict_concepts = {}

for l in list1:
    dict_concepts[l[0]] = l[1]

for k,v in dict_concepts.items():
    print k,v
    


# In[17]:

#for k,v in dict_concepts.items():
    #print k,v
for l in list2:
    if l[0] in dict_concepts:
        dict_concepts[l[0]] += l[1]
    else:
        dict_concepts[l[0]] = l[1]


# In[18]:

for k,v in dict_concepts.items():
    print k,v


# In[19]:

for l in list1:
    print l


nodemap = {}

def addNode(name):
    if name in nodemap:
        node = nodemap[name]
        node["count"] += 1
    else:
        node = {"nodeid": name, "count": 1}
        nodemap[name] = node
    return

list_of_concepts = []

for concept in concepts:
    list_of_concepts.append(concept[0])
sent = ' '.join(list_of_concepts)
print sent

