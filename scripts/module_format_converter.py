"""This script converts the full curriculum list into a CSV."""

full_module_list_file_path = "../curriculum/curriculum.md"

module_rows = list()
with open(full_module_list_file_path) as f:
	lines = f.readlines()

	module_row = ""
	for line in lines[8:]:
		if line.startswith("*"):
			if module_row != "":
				module_rows += [module_row]
			# strip away the asterisk and space, remove trailing newline
			module_row = line[2:].strip().replace("*", " Star").replace(".", "").replace("?", "").replace("/", "_")
		elif line == "" or line == "\n":
			# Don't process empty lines
			pass
		else:
			# Extract the pertinent detail from the line
			# line has the form "\s\s*\s.+?:.+?\n"
			# We want the right hand side, and no spaces
			# Sanitize it, as well
			line = line.split(":")[1].strip().replace("*", " Star").replace("/", "_")
			# If this is a list, replace them with tabs
			line = line.replace(", ","\t")
			module_row += f",{line}"

with open("./modules.csv", "w") as out:
	for module_row in module_rows:
		out.write(f"{module_row}\n")