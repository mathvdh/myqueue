#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from myqueue import MyQueue

class TestMyQueue(unittest.TestCase):
	def test_peek(self):
		q = MyQueue()
		q.add(1)
		q.add(2)
		q.add(3)

		self.assertTrue(q.peek() == 1)
		self.assertTrue(q.peek() == 1)
		self.assertTrue(q.size() == 3)

	def test_poll(self):
		q = MyQueue()
		q.add(1)
		q.add(2)
		q.add(3)

		self.assertTrue(q.poll() == 1)
		self.assertTrue(q.poll() == 2)
		self.assertTrue(q.size() == 1)

	def test_size(self):
		q = MyQueue()
		q.add(1)
		q.add(2)
		q.add(3)

		self.assertTrue(q.size() == 3)

	def test_add(self):
		q = MyQueue()
		self.assertTrue(q.size() == 0)

		q.add(1)
		self.assertTrue(q.size() == 1)

		q.add(2)
		self.assertTrue(q.size() == 2)

		q.add(3)
		self.assertTrue(q.size() == 3)
