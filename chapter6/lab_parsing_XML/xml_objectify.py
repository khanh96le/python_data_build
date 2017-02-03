import pandas as pd
from pandas import DataFrame
from lxml import objectify

path = '../data/Performance_MNR.xml'
parsed = objectify.parse(open(path))
root = parsed.getroot()

data = []
skip_fields = ['PARENT_SEQ', 'INDICATOR_SEQ', 'DESIRED_CHANGE', 'DECIMAL_PLACES']
for elt in root.INDICATOR:
  el_data = {}
  for child in elt.getchildren():
    if child.tag in skip_fields:
      continue
    el_data[child.tag] = child.pyval
  data.append(el_data)

print 0
