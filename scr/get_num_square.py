import os

num = os.environ.get("INPUT_NUM")
if num:
  try:
    num = int(num)
  except Exception:
    exit()
else:
  num = Null
  
  
print(f"::set-output name=num_squared::{num**2}")
