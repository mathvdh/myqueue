# myqueue

My Queue with 2 stacks.


## Installation

```
git clone git@github.com:mathvdh/myqueue.git
cd myqueue/
python setup.py install
or python setup.py develop
```

## Running the tests

```
python setup.py test
```


## Example usage

```
from myqueue import MyQueue

myq = MyQueue()
print "myq.add(1)", myq.add(1) 
print "myq.print_state()"
myq.print_state()

print "myq.add(2)", myq.add(2)
print "myq.print_state()"
myq.print_state()

print "myq.add(3)", myq.add(3)
print "myq.print_state()"
myq.print_state()

print "myq.peek()", myq.peek()
print "myq.print_state()"
myq.print_state()
print "myq.peek()", myq.peek()
print "myq.print_state()"
myq.print_state()

print "myq.poll()", myq.poll()
print "myq.print_state()"
myq.print_state()

print "myq.poll()", myq.poll()
print "myq.print_state()"
myq.print_state()

print "myq.poll()", myq.poll()
print "myq.print_state()"
myq.print_state()
```