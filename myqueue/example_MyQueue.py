#!/usr/bin/env python
# -*- coding: utf-8 -*-

from MyQueue import MyQueue

myqueue = MyQueue()
print "myqueue.add(1)", myqueue.add(1) 
print "myqueue.print_state()"
myqueue.print_state()

print "myqueue.add(2)", myqueue.add(2)
print "myqueue.print_state()"
myqueue.print_state()

print "myqueue.add(3)", myqueue.add(3)
print "myqueue.print_state()"
myqueue.print_state()

print "myqueue.peek()", myqueue.peek()
print "myqueue.print_state()"
myqueue.print_state()
print "myqueue.peek()", myqueue.peek()
print "myqueue.print_state()"
myqueue.print_state()

print "myqueue.poll()", myqueue.poll()
print "myqueue.print_state()"
myqueue.print_state()

print "myqueue.poll()", myqueue.poll()
print "myqueue.print_state()"
myqueue.print_state()

print "myqueue.poll()", myqueue.poll()
print "myqueue.print_state()"
myqueue.print_state()