# "files.autoSave": "afterDelay"

#!/ usr/bin/env python

# make sure to install these packages before running :
# pip install pandas
# pip install sodapy
6
import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets . Note ’None ’
# in place of application token , and no username or password :
client = Socrata ("www . datos .gov .co", None )

# Example authenticated client ( needed for non - public datasets ):
# client = Socrata (www. datos .gov.co ,
# MyAppToken ,
# username =" user@example . com" ,
# password =" AFakePassword ")

# First 2000 results , returned as JSON from API / converted to Python
# list of
# dictionaries by sodapy .
results = client . get ("ch4u - f3i5 ", limit =2000)
23
2# Convert to pandas DataFrame
results_df = pd . DataFrame . from_records ( results )