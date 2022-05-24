import selenium, time, os, csv, re, string
import pandas as pd


df = pd.read_excel('Final Prod/EditOutput(1).xlsx')

(df.notnull()).astype('float')
df.info()

df = df.astype({'Total Main Area (Exterior Measured)':'string'})
#df['Total Main Area (Exterior Measured)'] = df['Total Main Area (Exterior Measured)'].str.replace('0', '-1')
df['Total Main Area (Exterior Measured)'].str.replace(r'\s\*{2,}[\s\n]', '1')

df['Total Main Area (Exterior Measured)'] = df['Total Main Area (Exterior Measured)'].str.replace(' Sq. Ft', '')
df['Total Main Area (Exterior Measured)'] = df['Total Main Area (Exterior Measured)'].str.replace(',', '')

#print(df['Total Main Area (Exterior Measured)'])


df['Total Acreage'] = df['Total Acreage'].str.split('/').str[1]
df['Total Acreage'] = df['Total Acreage'].str.replace(' acres', '')
df = df.astype({'Total Acreage':'float'})
df = df.astype({'Land Homesite Value':'float'})
df = df.astype({'Total Land Market Value':'float'})

df['Total Main Area (Exterior Measured)'] = pd.to_numeric(df['Total Main Area (Exterior Measured)'],errors = 'coerce')
#df = df.astype({'Total Main Area (Exterior Measured)':'float'})

#df.info()

df['$ per Sq.ft'] = df['Total Appraised Value'].astype(float, errors='ignore').div(df['Total Main Area (Exterior Measured)'].astype(float, errors='ignore'))
df['$ per Acreage'] = df['Total Land Market Value'].astype(float, errors='ignore').div(df['Total Acreage'].astype(float, errors='ignore'))

writer = pd.ExcelWriter('FinalOutput.xlsx')
df.to_excel(writer, 'Values')
writer.save()