class Parser:

	def __init__(self, args):

		if args.file:
			self.size = None
			self.state = []
			self.parse_file(args.file)	
		else:
			self.size = args.size
			self.state = None


	def parse_file(self, file):

		try:
			lines = open(file).read().split('\n')
		except Exception as error:
			print(f"[PARSER ERROR] Open failed:\n{error}")

		try:
			for line in lines:
				epured = line.split('#')
				# print(epured)

				if len(epured) > 2:
					print("Error: Only one comment maximum per line")
					exit(0)
				
				epured = epured[0]
				
				if epured:

					if self.size:
						values = [value for value in epured.split(' ') if value.isnumeric()]
						if self.size != len(values):
							print("Error: Board must be a square")
							exit(0)

						self.state.extend(int(v) for v in values)
					
					else:
						self.size = int(epured)

			print(f"Parser board state: {self.state}")

		except Exception as error:
			print(f"[PARSER ERROR] Parsing failed:\n{error}")
