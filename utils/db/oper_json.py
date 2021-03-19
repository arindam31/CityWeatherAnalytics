# import json
# import pathlib
# #
# # #
# with open('../../cities_all.json') as job:
#     data_cities = json.load(job)
#
# backup_city = []
# for line in data_cities:
#     if line['country_full'] is not None:
#         backup_city.append(line)
#
# #
# # d_continent = {}
# #
# # with open('../../CC.json') as job:
# #     data_continents = json.load(job)
# #
# # for line in data_continents:
# #     continent = line['Continent_Code']
# #     if continent in d_continent.keys():
# #         if line['Two_Letter_Country_Code'] not in d_continent[continent]:
# #             d_continent[continent].append(line['Two_Letter_Country_Code'])
# #     else:
# #         d_continent[continent] = list()
# #
# # with open('../../conti_cnt.json', 'w') as job:
# #     json.dump(d_continent, job)
# #
# with open('../../conti_cnt.json') as job:
#     conti_data = json.load(job)
# #
# for continent, value in conti_data.items():
#     for index, l_citi in enumerate(backup_city, start=0):
#         if l_citi['country_code'] in value:
#             backup_city[index]['continent_code'] = continent
#
#
# with open('../../finale.json', 'w') as job:
#     json.dump(backup_city, job, ensure_ascii=False)
# #
# #--------------------------------------
# with open('../../finale.json') as job:
#     result = json.load(job)
#
# bad = 0
# good = 0
# for line in result:
#
#     try:
#         line['continent_code']
#         good += 1
#
#     except KeyError:
#         print(line)
#         bad += 1
#
# print (bad, good)
