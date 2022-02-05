import os

# File paths
curriculum_dir = "../curriculum"
modules_csv = "./modules.csv"

details = ["Category", "Module Prerequisites", "Audience", "Level"]
dirs = ["categories", "modules", "audiences", "levels"]

def link(text, target="", directory="./"):
	if text == "None":
		return text

	if target == "":
		temp = text.replace(" ", "_")
		target = f"{directory}{temp}.md"

	md_link = f"[{text}]({target})"

	return md_link

# For every module, parse
with open(modules_csv) as f:
	# Storage
	categories = dict()
	audiences = dict()
	levels = dict()
	# Parse everything
	lines = [line.strip() for line in f.readlines()]
	for line in lines:
		# Parse row
		module = line.split(",")
		name, cat, prereqs, audience, level = module
		# Sanitize name
		filename = name.replace(" ", "_")
		## Organize
		# Create or add to categories
		for token in cat.split("\t"):
			try:
				categories[token] += [name]
			except KeyError:
				categories[token] = [name]
		# Create or add to audiences
		for token in audience.split("\t"): 
			try:
				audiences[token] += [name]
			except KeyError:
				audiences[token] = [name]
		# Create or add to levels
		try:
			levels[level] += [name]
		except KeyError:
			levels[level] = [name]
		## Create the Module
		# Create a directory for the module
		module_dir = f"{curriculum_dir}/modules/{filename}/"
		try:
			os.mkdir(module_dir)
		except FileExistsError:
			pass
		module_file = f"{module_dir}/{filename}.md"
		with open(module_file, "w") as out:
			out.write(f"# {name}")
			out.write("\n")
			out.write("## Details\n")
			for token, label, d in zip(module[1:], details, dirs):
				token = token.replace("\t", ", ")
				token_link = link(token, directory=f"../{d}/")
				out.write(f"* {label}: {token_link}\n")
			out.write("\n")
			out.write("## Content\n")
			out.write("Content text.\n")
			out.write("\n")
			out.write("## Related KGC Media\n")
			out.write("* Workshop Example\n")
			out.write("* Tutorial Example\n")
			out.write("\n")
			out.write("## References\n")
			out.write("[1] Reference example.\n")
			out.write("\n")
			out.write("## Contributors\n")
			out.write("* Cogan Shimizu\n")
	## Create the category files
	# Create categories.md
	category_dir = f"{curriculum_dir}/categories"
	try:
		os.mkdir(category_dir)
	except FileExistsError:
		pass
	all_categories_file = f"{curriculum_dir}/categories.md"
	with open(all_categories_file, "w") as out:
		out.write("# All Categories")
		out.write("\n")
		for category in categories.keys():
			category_link = link(category, directory="./categories/")
			out.write(f"* {category_link}\n")
	# Create each of the category files in the folder
	for category in categories.keys():
		category_s = category.replace(" ", "_")
		category_filename = f"{category_dir}/{category_s}.md"
		with open(category_filename, "w") as out:
			out.write(f"# Category: {category}\n")
			for module in categories[category]:
				module_dir = f"../modules/{module.replace(' ','_')}/"
				module_link = link(module, directory=module_dir)
				out.write(f"* {module_link}\n")
			out.write("\n")
	## Create the audience files
	audience_dir = f"{curriculum_dir}/audiences/"
	try:
		os.mkdir(audience_dir)
	except FileExistsError:
		pass
	all_audiences_file = f"{curriculum_dir}/audiences.md"
	with open(all_audiences_file, "w") as out:
		out.write("# All Audiences")
		out.write("\n")
		for audience in audiences.keys():
			audience_link = link(audience, directory="./audiences/")
			out.write(f"* {audience_link}\n")
		# Create each of the category files in the folder
	for audience in audiences.keys():
		audience_s = audience.replace(" ", "_")
		audience_filename = f"{audience_dir}/{audience_s}.md"
		with open(audience_filename, "w") as out:
			out.write(f"# Audience: {audience}\n")
			for module in audiences[audience]:
				module_dir = f"../modules/{module.replace(' ','_')}/"
				module_link = link(module, directory=module_dir)
				out.write(f"* {module_link}\n")
			out.write("\n")
	## Create the level files
	level_dir = f"{curriculum_dir}/levels/"
	try:
		os.mkdir(level_dir)
	except FileExistsError:
		pass
	all_levels_file = f"{curriculum_dir}/levels.md"
	with open(all_levels_file, "w") as out:
		out.write("# All levels")
		out.write("\n")
		for level in levels.keys():
			level_link = link(level, directory="./levels/")
			out.write(f"* {level_link}\n")
		# Create each of the category files in the folder
	for level in levels.keys():
		level_s = level.replace(" ", "_")
		level_filename = f"{level_dir}/{level_s}.md"
		with open(level_filename, "w") as out:
			out.write(f"# level: {level}\n")
			for module in levels[level]:
				module_dir = f"../modules/{module.replace(' ','_')}/"
				module_link = link(module, directory=module_dir)
				out.write(f"* {module_link}\n")
