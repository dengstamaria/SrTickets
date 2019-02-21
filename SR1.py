# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 15:29:38 2019

@author: 10009174
"""


import pandas as pd
import re



#open file
df = pd.read_excel('Book1.xlsx')

#extract strings from pandas column and check who from the team worked on the ticket
df['AIM Engineer']=df['Comments and Work notes'].str.extract("(VICTOR BRACAMONTE|RICKY SALAZAR|CHRISTIAN M. AMBAYEC|MA. FATIMA B. SANTOS|Mc Dave Paul Alban|MARK DONALD ASILO|Isagani Ortega|Kathrina Rufino|Jossalyn Bonozo|Edgar Bunyog)", flags=re.IGNORECASE,expand=True)

#show output
print(df)

#df.to_excel('sr_out.xlsx')


