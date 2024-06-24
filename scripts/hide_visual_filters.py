#!/usr/bin/env python3

import glob 
import json

# function which sets the isHiddenInViewMode flag to True if it not yet exists or if its False
def set_hide_flag(filter_item):
  if not 'isHiddenInViewMode' in filter_item:
    filter_item['isHiddenInViewMode'] = True
    return True
  if filter_item['isHiddenInViewMode'] == False:
    filter_item['isHiddenInViewMode'] = True
    return True
   
  return False
  
  
# Find all visual definitions
file_pattern = '**/visual.json'
files = glob.glob(file_pattern,  recursive = True)


# Iterate over all visual.json files
for file in files:
  with open(file, 'r+') as f:
    data = json.load(f)
    rewritefile = False
    if 'filterConfig' in data:
      # Iterate over all filter definitions
      for i, item in enumerate(data['filterConfig']['filters']):
        # If displayName was changed (usually by user in Power BI Desktop) then do not overwrite the filter config
        # This is a workaround to let the user decide if certain visual should be excluded from this procedure
        if 'displayName' in data['filterConfig']['filters'][i]:
          if data['filterConfig']['filters'][i]['displayName'] == data['filterConfig']['filters'][i]['field']['Column']['Property']:
            rewritefile = set_hide_flag(data['filterConfig']['filters'][i])
        else:
         rewritefile = set_hide_flag(data['filterConfig']['filters'][i])

    if rewritefile == True:
      f.seek(0)                    # Set file position to the start
      json.dump(data, f, indent=2) # Write JSON to file
      f.truncate()                 # Remove remaining part



   
   