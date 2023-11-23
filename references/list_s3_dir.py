from typing import List
import pandas as pd
import tempfile

def list_files(s3_dir: str, suffix="tsv") -> List[str]:
	"""List files in an s3 directory."""
	pattern = re.compile(f".*\\.{suffix}")
	with tempfile.TemporaryDirectory() as tmpdir:
		local_file = os.path.join(tmpdir, "ls.tsv")
		os.system(f"aws s3 cp {s3_dir} > {local_file}")
		stream = open(f"{local_file}", "r")
		file_list = []
		for line in stream:
			line = line.rstrip()
			line_split = line.split()
			file_name = line_split[-1]
			search = pattern.search(file_name)
			if search:
				file_list.append(search.group(0))
	return file_list

