#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
import scipy.stats
import copy

################# entropoy
# Tip: feel free to call scipy.stats.entropy.  Make sure to use log base 2.
#
# Input:
# data_frame -- pandas data frame
#
# Output:
# answer -- float indicating the empirical entropy of tyhe data in data_frame
##############################################
def entropy(data_frame):

	# default value until this function is filled in
	answer = 0
	return answer

################# info_gain
# Tip: this function should call entropy
#
# Inputs:
# data_frame -- pandas data frame
# attribute -- string indicating the attribute for which we wish to compute the information gain
# domain -- set of values (strings) that the attribute can take
#
# Output:
# answer -- float indicating the information gain
################################################3
def info_gain(data_frame, attribute, domain):

	# default value until this function is filled in
	answer = 0
	return answer

######## Decision_tree class
#
# This class defines the data structure of the decision tree to be learnt
############################
class Decision_Tree:

	# constructor
	def __init__(self,attribute,branches,label):
		self.attribute = attribute
		self.branches = branches
		self.label = label

	# leaf constructor
	def make_leaf(label):
		return Decision_Tree('class', {}, label)
	
	# node constructor
	def make_node(attribute,branches):
		return Decision_Tree(attribute, branches, None)

	# string representation
	def __repr__(self):
		return self.string_repr(0)
		
	# decision tree string representation
	def string_repr(self,indent):
		indentation = '\t'*indent
		
		# leaf string representation
		if self.attribute == 'class':
			return f'\n{indentation}class = {self.label}'

		# node string representation
		else:
			representation = ''
			for value in self.branches:
				representation += f'\n{indentation}{self.attribute} = {value}:'
				representation += self.branches[value].string_repr(indent+1)
			return representation

	# classify a data point
	def classify(self,data_point):

		# leaf
		if self.attribute == 'class':
			return self.label

		# node
		else:
			return self.branches[data_point[self.attribute]].classify(data_point)

############# choose attribute
# Tip: this function should call info_gain
#
# Inputs:
# attributes_with_domains -- dictionary with attributes as keys and domains as values
# data_frame -- pandas data_frame
#
# Output:
# best_score -- float indicting the information gain score of the best attribute
# best_attribute -- string indicating the best attribute
#################################
def choose_attribute(attributes_with_domains,data_frame):

	# default value until this function is filled in
	best_score = 0
	best_attribute = 'MSZoning'
	return best_score, best_attribute

############# train decision tree
# Tip: this is a recursive function that should call itself as well as
# choose_attribute,  Decision_Tree.make_leaf, Decision_Tree.make_node
#
# Inputs:
# data_frame -- pandas data frame
# attributes_with_domains -- dictionary with attributes as keys and domains as values
# default_class -- string indicating the class to be assigned when data_frame is empty
# threshold -- integer indicating the minimum number of data points in data_frame to allow
#              the creation of a new node that splits the data with some attribute
#
# Output:
# decision_tree -- Decision_Tree object
########################
def train_decision_tree(data_frame,attributes_with_domains,default_class,threshold):

	# default value until this function is filled in
	return Decision_Tree.make_leaf(default_class)

######### eval decision tree
# Tip: this function should call decision_tree.classify
#
# Inputs:
# decision tree -- Decision_Tree object
# data_frame -- pandas data frame
#
# Output:
# accuracy -- float indicating the accuracy of the decision tree
#############
def eval_decision_tree(decision_tree, data_frame):

	# default value until this function is filled in
	accuracy = 0
	return accuracy

########### k-fold cross-validation
# Tip: this function should call train_decision_tree and eval_decision_tree
#
# Inputs:
# train_data -- pandas data frame
# test_data -- pandas data frame
# attributes_with_domains -- dictionary with attributes as keys and domains as values
# k -- integer indicating the number of folds
# threshold_list -- list of thresholds to be evaluated
#
# Outputs:
# best_threshold -- integer indiating the best threshold found by cross validation
# test_accuracy -- float indicating the accuracy based on the test set
#####################################3
def cross_validation(train_data, test_data, attributes_with_domains, k, threshold_list):

	# default value until this function is filled in
	best_threshold = threshold_list[0]
	test_accuracy = 0
	for threshold in threshold_list:
		
		trained_decision_tree = train_decision_tree(train_data,attributes_with_domains,'low',threshold)
		validation_accuracy = eval_decision_tree(trained_decision_tree,train_data)
	return best_threshold, test_accuracy

############################ main
# You should not need to change the code below
#
# This code performs the following operations:
# 1) Load the data
# 2) create a list of attributes
# 3) create a dictionary that maps each attribute to its domain of values
# 4) split the data into train and test sets
# 5) train a decision tree while optimizing the threshold hyperparameter by
#    10-fold cross validation 
#####################################

#load data
data_frame = pd.read_csv("categorical_real_estate.csv")
data_frame = data_frame.fillna('NA')
# print(data_frame)

# get attributes
attributes = list(data_frame.columns)
attributes.remove('class')

# create dictionary that maps each attribute to its domain of values
attributes_with_domains = {}
for attr in attributes:
	attributes_with_domains[attr] = set(data_frame[attr])


#split data in to train and test
train_data = data_frame.iloc[0:1000]
test_data = data_frame.iloc[1000:]
print(train_data)
# perform 10-fold cross-validation
best_threshold, accuracy = cross_validation(train_data, test_data, attributes_with_domains, 10, [10,20,40,80,160])
# print(f'Best threshold {best_threshold}: accuracy {accuracy}')

