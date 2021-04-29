import random
from math import sqrt

class Taquin:

	def __init__(self, initial_state, size=3):

		self.size = int(sqrt(len(initial_state))) if initial_state else size
		self.final_state = self.generate_final()
		self.initial_state = initial_state if initial_state else self.generate_random()

	def generate_random(self, max_shuffle=random.randint(100, 1000)):

		state = self.final_state.copy()
		i = 0

		while i < max_shuffle:
			index = state.index(0)
			
			y, x = index / self.size, index % self.size

			neighbours = [
				(x - 1 >= 0, -1),
				(x + 1 < self.size, +1),
				(y - 1 >= 0, -self.size),
				(y + 1 < self.size, +self.size),
			]

			exist = False

			while not exist:
				exist, di = neighbours[random.randint(0, 3)]	
			
			state[index] = state[index + di]
			state[index + di] = 0

			i += 1
		
		print(f"Generate random board (shuffle: {max_shuffle})")
		return state

	def generate_final(self):

		final_state = [0 for i in range(self.size * self.size)]
		x, y = 0, 0
		n = self.size

		value = 1
		while value < self.size * self.size:
			i = 0
			while i < n:
				#print(f"{value}: index {i} - coords y/x {y}/{x}")
				final_state[x + y * self.size] = value
				value += 1
				i += 1
				x += 1
			
			x -= 1
			y +=1
			n -= 1

			i = 0
			while i < n:
				#print(f"{value}: coords y/x {y}/{x}")
				final_state[x + y * self.size] = value
				value += 1
				i += 1
				y += 1
			if value == self.size * self.size:
				break

			x -= 1
			y -= 1
			
			i = 0
			while i < n:
				#print(f"{value}: coords y/x {y}/{x}")
				final_state[x + y * self.size] = value
				value += 1
				i += 1
				x -= 1

			x += 1
			y -= 1
			
			n -= 1

			i = 0
			while i < n:
				#print(f"{value}: coords y/x {y}/{x}")
				final_state[x + y * self.size] = value
				value += 1
				i += 1
				y -= 1
			x += 1
			y += 1
			
		return final_state

	def is_solvable(self):

		state = self.initial_state.copy()
		
		izero = state.index(0)
		fzero = self.final_state.index(0)
		dzero = abs(izero % self.size - fzero % self.size) + abs(int(izero / self.size) - int(fzero / self.size))

		moves = 0
		print(f"State init {moves}:\n{state}\n{self.final_state}")
		# while self.final_state != state:
		for i, v in enumerate(self.final_state):

			index = state.index(v)

			if v != state[i]:
				state[index] = state[i]
				state[i] = v
				print(f"State {moves}:\n{state}\n{self.final_state}")
				moves += 1

			if self.final_state == state:
				print(f"Transpositions: {moves} / zero: {dzero}\tSolvable: {dzero % 2 == moves % 2}")
				return dzero % 2 == moves % 2

		print("Error: Unable to know if this taquin is solvable.")
		exit(0)

