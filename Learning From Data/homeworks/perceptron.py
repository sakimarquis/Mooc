# -*- coding: utf-8 -*-
"""
a github solution
"""

import numpy as np
import random

class PLA:
	def __init__(self, n=10):
		# Number of points
		self.n = n
		self.f = np.random.uniform(-1, 1, 2)
		self.X = np.random.uniform(-1, 1, (n, 2))
		self.correct_y = np.array([self.correct_classify(i) for i in range(n)])

		self.w = np.zeros(3)

	def get_misclassified_indices(self):
		misclassified_indices = []
		for i in range(self.n):
			if self.is_misclassified(i):
				misclassified_indices.append(i)
		return misclassified_indices

	def is_misclassified(self, i):
		return self.classify(i) != self.correct_y[i]

	def correct_classify(self, i):
		return self._correct_classify(self.X[i])

	def _correct_classify(self, p):
		r = np.sign(self.f[0]*p[0] + self.f[1] - p[1])

		return r

	def classify(self, i):
		return self._classify(self.X[i])

	def _classify(self, p):
		return np.sign(self.w[0] + self.w[1]*p[0] + self.w[2]*p[1])

	def iterate(self):
		misclassified_indices = self.get_misclassified_indices()
		if len(misclassified_indices) == 0:
			return 0

		random_index = random.choice(misclassified_indices)
		random_X = self.X[random_index]

		random_X = np.insert(random_X, 0, 1)
		new_X = self.correct_y[random_index] * random_X
		self.w = np.add(self.w, new_X)

		return len(misclassified_indices)


if __name__ == '__main__':

	test_points = np.random.uniform(-1, 1, (100, 2))

	iterations = 1000
	total = 0
	prob_total = 0
	for i in range(iterations):
		pla = PLA(n=100)
		count = 0
		while pla.iterate() > 0:
			count += 1
		total += count

		incorrect_count = 0
		for p in test_points:
			if pla._classify(p) != pla._correct_classify(p):
				incorrect_count += 1
		prob_total += incorrect_count/len(test_points)

	print('Average iterations: ', total/iterations)
	print('Average P[f(x)=/=g(x)]: ', prob_total/iterations)