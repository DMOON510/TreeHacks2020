import random
import numpy as np



def recommend(galleries, visitor):
	for i in range(len(visitor.preference)):
		visitor.score[i]= 0.5 * len(galleries[i].visitors) + visitor.preference[galleries[i].name]
		visitor.score_np[i] = np.asarray(visitor.score[i])
	visitor.recommendation = visitor.score_np.argmax()


def like(visitor):
	for i in range(len(visitor.preference)):
		visitor.preference[i] = random.randrange(1, 5, 1)


class visitor(object):
	"""A visitor who visits a museum. Receive a recommmedation of a gallery"""
	def __init__(self, gallery=None):
		self.preference = [0, 0, 0, 0, 0]
		self.has_visited = []
		self.score = [0,0,0,0,0]
		self.score_np = np.asarray(self.score)
		self.recommendation = self.score_np.argmax()
		self.gallery = gallery

	def move_to(self, gallery):
		self.gallery.remove_visitor(self)
		gallery.add_visitor(self)
		self.has_visited += gallery

	def __repr__(self): 
		return self



class gallery(object):
	"""there are five exhibit in total and each has indicator of crowdness"""	
	def __init__(self, name, crowdness=1):
		self.name = name
		self.crowdness = crowdness
		self.visitors = []
 	   
	def add_visitor(self, visitor):
		self.visitors.append(visitor)
		visitor.current_visiting = self
	def remove_visitor(self, visitor):
		self.vistiors.remove(visitor)
		visitor.gallery = None
	def __str__(self):
		return self



        
