

class Store:
	def __init__(self,state=None,reducer_func=None):
		self.state = state
		self.reducer_func = reducer_func
		self.listeners = []
		self.dispatch(EmptyAction())
	def getState(self):
		return self.state
	def dispatch(self, action):
		if self.reducer_func is not None:
			self.state = self.reducer_func(self.state, action)
		for xx in self.listeners:
			xx()
	def subscribe(self, rx):
		self.listeners.append(rx)

def create_store(reducer_func):
	return Store(None,reducer_func)

def combinedReducer(state,action):
	# if you get a state that is None
	# return the default
	if state is None:
		return { "x" : 0 }
	if action.type == "INCREMENT":
		return { "x" : state["x"] + action.value }
	elif action.type == "DECREMENT":
		return { "x" : state["x"] - action.value }
	else:
		return state

# def incrementReducer(state,action):
#	if state is None:
#		return { "x" :  0 }
#	if not state.has_key("x"):
#		return { "x" : 0 }
#	else:
#		if action.value>0:
#			return { "x" : state["x"] + action.value}
#		elif action.value==0:
#			return state
#		else:
#			return { "x" : state["x"]+1 }

#def decrementReducer(state,action):
#	if not state.has_key("x"):
#		return { "x" :  1 }
#	else:
#		if action.value != 0:
#			return { "x" : state["x"] - action.value }
#		else:
#			return { "x" : state["x"]  - 1}


# def dispatch(state, action):
#	if action is None:
#		return { "x" : 0 }
#	if action.type == "INCREMENT":
#		return incrementReducer(state,action)
#	elif action.type == "DECREMENT":
#		return decrementReducer(state,action)

class Action:
	def __init__(self, type):
		self.type = type

class EmptyAction(Action):
	def __init__(self):
		Action.__init__(self,None)
		
class IncrementAction(Action):
	def __init__(self,value):
		Action.__init__(self,"INCREMENT")
		self.value = value

class DecrementAction(Action):
	def __init__(self,value):
		Action.__init__(self,"DECREMENT")
		self.value = value
		
def small_test():		
	state = dispatch(None, None)
	assert(state["x"]==0)
	state = dispatch( { "x" : 0 }, IncrementAction(1) )
	assert(state["x"]==1)

# FINAL CODE down here
# make the store and give it the incrementReducer

store = create_store(reducer_func=combinedReducer)

# print when you get a change
def render():
	print("render", store.getState())

# subscribe to the changes
store.subscribe(render)

# this will init the state
store.getState()

# tell it to increment two times
store.dispatch(IncrementAction(1))
store.dispatch(IncrementAction(1))
store.dispatch(DecrementAction(1))


