import pandas as pd
import pandasql as psql
import urllib.parse

df_data = pd.read_csv(
    'Engineering Student Count Details (College wise - Branch wise).csv')
df_updated = df_data.groupby('College Name').agg({'College Code': 'first', 'Category Name': 'first', 'University': 'first', 'District': 'first',
                                                  'Zone': 'first', 'Group': 'first', 'Total No of students': 'sum', '1st year': 'sum'})
df_updated = df_updated.sort_values(by='College Code')
df_updated.to_csv('unique_collage.csv')
print(df_updated.describe())


df_updated2 = df_updated.groupby('Zone').agg(
    {'Total No of students': 'sum', '1st year': 'sum'})
# print(df_updated2)
print(df_updated2.describe())
df_updated2.to_csv('zone_wise.csv')

# query for colleges which have max number of students in zone 4, 16, and 22
query = "SELECT `College Name`, zone, MAX(`Total No of students`) as total_students, `1st year` FROM df_updated WHERE Zone IN ('Zone IV : MIT - Chromepet', 'Zone XIV : Karaikudi', 'Zone XXII : Madurai') group by zone"
max_college_in_zones = psql.sqldf(query, locals())
max_college_in_zones.to_csv('max_college_in_zones.csv')
print(max_college_in_zones)


college_names = max_college_in_zones['College Name'].values
for college in college_names:
    place_name = college
    encoded_place_name = urllib.parse.quote(place_name)
    map_link = f"https://www.google.com/maps?q={encoded_place_name}"
    print(place_name,"Google Maps Link:", map_link)