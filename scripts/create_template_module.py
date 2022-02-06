import os

# Utility data and functions
labels = ["Category", "Module Prerequisites", "Audience", "Level"]
dirs = ["categories", "modules", "audiences", "levels"]

def link(text, target="", directory="./"):
	if text == "None":
		return text

	if target == "":
		temp = text.replace(" ", "_")
		target = f"{directory}{temp}.md"

	md_link = f"[{text}]({target})"

	return md_link

# Data paths
modules_dir = "../curriculum/modules/"
module_name = "Test Module"
module_dir  = f"{modules_dir}{module_name}/"

# Attempt to create the module directory
try:
	os.mkdir(module_dir)
except FileExistsError:
	pass

# Create the Module File and dummy contents.
module_file = f"{module_dir}{module_name}.md"
with open(module_file, "w") as out:
	out.write(f"# {module_name}")
	out.write("\n")
	out.write("## Details\n")
	for label, d in zip(labels, dirs):
		token_link = link("Missing", directory=f"../{d}/")
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
	out.write("* Temporary Name\n")