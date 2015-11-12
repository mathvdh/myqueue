# -*- coding: utf-8 -*-

class MyQueue:
	def __init__(self):
		self.stack_in = []
		self.stack_out = []

	def _stack_in_empty(self):
		return len(self.stack_in) == 0

	def _stack_out_empty(self):
		return len(self.stack_out) == 0

	def _in_to_out(self):
		while(not self._stack_in_empty()):
			self.stack_out.append(self.stack_in.pop())

	def print_state(self):
		print "stack_in :", self.stack_in
		print "stack_out : ", self.stack_out

	#returns (and remove) the head of the queue
	def poll(self):
		val = self.peek()
		self.stack_out.pop()
		return val

	#returns the size of the queue
	def size(self):
		return len(self.stack_in) + len(self.stack_out)

	#returns (without removing) the head of the queue
	def peek(self):
		if (self._stack_out_empty()):
			self._in_to_out()
		
		if(not self._stack_out_empty()):
			return self.stack_out[len(self.stack_out)-1]
		else:
			return None

	#adds an element to the queue
	def add(self, val):
		self.stack_in.append(val)

