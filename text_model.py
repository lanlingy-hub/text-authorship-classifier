#
# finalproject
#
# Part I: Building an initial text model 
# Part II: Saving and retrieving a text model
# Part III: Adding features to the model
# Part IV: Adding methods for scoring and classification
# Part V: Comparing texts

#
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 13:57:47 2025

@author: yanglanling
"""
import math

def test():
    """ your docstring goes here """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)

def clean_text(txt) :
    """returns a list containing the words in txt after it has been “cleaned”"""
    txt = txt.lower()
    for symbol in """.,?"'!;:""":
        txt = txt.replace(symbol, "")
    word_list = txt.split()
    return word_list

def stem(word):
     """return the stem of s"""
     if len(word) <= 3:
         return word
     elif len(word) >= 5 and word[-4:] == 'tion':
         return word[:-4]
     elif len(word) >= 4 and word[-3:] == 'ing':
         return word[:-3]
     elif len(word) >= 3 and word[-2:] == 'ed':
         return word[:-2]
     elif len(word) >= 3 and word[-2:] == 'er':
         return word[:-2]
     elif len(word) >= 3 and word[-2:] == 'ly':
         return word[:-2]
     elif len(word) >= 2 and word[-1] == 's' and word[-2:] != 'ss':
         return word[:-1]
     else:
         return word

def compare_dictionaries(d1, d2):
    """ return their log similarity score"""
    if d1 == {}:
        return -50
    total = 0
    for key in d1:
        total += d1[key]
    score = 0
    for key in d2:
        count2 = d2[key]
        if key in d1:
            count1 = d1[key]
            prob = count1/total
            score += count2 * math.log(prob)
        else:
            prob = 0.5 / total
        score += count2 * math.log(prob)
    return score
  
    
class TextModel:
    def __init__(self, model_name):
        """construct a new TextModel"""
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.punctuation = {}
        
    def __repr__(self):
        """Return a string representation of the TextModel."""
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of punctuation marks: ' + str(len(self.punctuation)) + '\n'
        return s
    
    
    def add_string(self, s):
        """Analyzes the string txt and adds its pieces to all of the 
        dictionaries in this text model"""      
        for x in s:
            if x in ".,?\"'!:;":
                if x in self.punctuation:
                    self.punctuation[x] +=1
                else:
                    self.punctuation[x] =1
        
        words_with_punct = s.split()
        count = 0
        for w in words_with_punct:
            count += 1
            if len(w) > 0 and w[-1] in ".!?":
                if count in self.sentence_lengths:
                    self.sentence_lengths[count] += 1
                else:
                    self.sentence_lengths[count] = 1
                count = 0
        if count > 0:
            if count in self.sentence_lengths:
                self.sentence_lengths[count] +=1
            else:
                self.sentence_lengths[count] = 1
                
        word_list = clean_text(s)           
        for w in word_list:
            if w in self.words:
                self.words[w]+= 1
            else:
                self.words[w] = 1
        
            length = len(w)
            if length in self.word_lengths:
                self.word_lengths[length] += 1
            else:
                self.word_lengths[length] = 1
                
            suffix = stem(w)
            if suffix in self.stems:
                self.stems[suffix] += 1
            else:
                self.stems[suffix] = 1
                
    def add_file(self, filename):
        """adds all of the text in the file identified by filename to the model"""
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text = f.read()
        f.close()
        self.add_string(text)
        
    def save_model(self):
        """saves the TextModel object self by writing its various feature 
        dictionaries to files"""
        words_filename = self.name + '_words'
        f = open(words_filename, 'w')
        f.write(str(self.words))
        f.close()
        
        lengths_filename = self.name +'_word_lengths'
        f = open(lengths_filename, 'w')
        f.write(str(self.word_lengths))
        f.close()
        
        stems_filename = self.name +'_stems'
        f = open(stems_filename, 'w')
        f.write(str(self.stems))
        f.close()
        
        sentence_lengths_filename = self.name +'_sentence_lengths'
        f = open(sentence_lengths_filename,'w')
        f.write(str(self.sentence_lengths))
        f.close()
        
        punctuation_filename = self.name +'_punctuation'
        f = open(punctuation_filename,'w')
        f.write(str(self.punctuation))
        f.close()
        
    def read_model(self):
        """ reads the stored dictionaries for the called TextModel object from 
        their files and assigns them to the attributes of the called TextModel"""
        words_filename = self.name + '_words'
        f = open(words_filename, 'r')
        words_str =f.read()
        f.close()
        self.words = dict(eval(words_str))
        
        lengths_filename = self.name + '_word_lengths'
        f = open(lengths_filename, 'r')
        lengths_str = f.read()
        f.close()
        self.word_lengths = dict(eval(lengths_str))
        
        stems_filename = self.name +'_stems'
        f = open(stems_filename, 'r')
        stems_str = f.read()
        f.close()
        self.stems = dict(eval(stems_str))
       
        sentence_lengths_filename = self.name + '_sentence_lengths'
        f = open(sentence_lengths_filename, 'r')
        sentence_lengths_str = f.read()
        f.close()
        self.sentence_lengths = dict(eval(sentence_lengths_str))
        
        punctuation_filename = self.name +'_punctuation'
        f = open(punctuation_filename,'r')
        punctuation_str = f.read()
        f.close()
        self.punctuation = dict(eval(punctuation_str))
        
    def similarity_scores(self, other):
        """returns a list of log similarity scores measuring the similarity 
        of self and other """
        word_score = compare_dictionaries(other.words, self.words)
        length_score = compare_dictionaries(other.word_lengths, self.word_lengths)
        stem_score = compare_dictionaries(other.stems, self.stems)
        sent_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        punc_score = compare_dictionaries(other.punctuation, self.punctuation)
        scores = [word_score,length_score,stem_score,sent_score,punc_score]
        return scores
    
    def classify(self, source1, source2):
        """compares the called TextModel object (self) to two other “source” 
        TextModel objects (source1 and source2) and determines which of these 
        other TextModels is the more likely source of the called TextModel"""
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print('scores for ' + source1.name +':' + str(scores1))
        print('scores for ' + source2.name + ':' + str(scores2))
        count1 = 0
        count2 = 0
        for i in range(len(scores1)):
            if scores1[i] > scores2[i]:
                count1 += 1 
            elif scores2[i] > scores1[i]:
                count2 += 1
        if count1 > count2:
            print(self.name + ' is more likely to have come from ' + source1.name)
        else:
            print(self.name + ' is more likely to have come from ' + source2.name)
            
def create_models():
    churchill = TextModel('churchill')
    churchill.add_file('churchill.txt')
    churchill.save_model()
    
    hitler = TextModel('hitler')
    hitler.add_file('hitler.txt')
    hitler.save_model()
    
def run_tests():
    """ Classify four new texts using churchill vs hitler models"""
    source1 = TextModel('churchill')
    source1.add_file('churchill.txt')

    source2 = TextModel('hitler')
    source2.add_file('hitler.txt')

    new1 = TextModel('new_churchill')
    new1.add_file('new_churchill.txt')
    new1.classify(source1, source2)
    
    new2 = TextModel('new_hitler')
    new2.add_file('new_hitler.txt')
    new2.classify(source1, source2)
    
    new3 = TextModel('F1')
    new3.add_file('F1_comment.txt')
    new3.classify(source1, source2)
    
    new4 = TextModel('trump')
    new4.add_file('trump.txt')
    new4.classify(source1, source2)
    
    
    
    
    
    
    
                
                
        
        
        
            
        
        
        
        
        
   
        
        
        
        
      
                
        
        
        
    
