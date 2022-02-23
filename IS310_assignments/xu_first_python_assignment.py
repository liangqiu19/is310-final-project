# xu_week2.py
# Store popularity count in each year for different DH tools, update the data structure and print out the results


def main():
    dh_tools_popularity_by_year = [
        {
            'name': 'Python',
            '2015': 9,
            '2016': 22,
            '2017': 27,
            '2018': 32,
            '2019': 35
        },
        {
            'name': 'JavaScript',
            '2015': 8,
            '2016': 18,
            '2017': 12,
            '2018': 6,
            '2019': 15
        },
        {
            'name': 'Twitter',
            '2015': 10,
            '2016': 18,
            '2017': 26,
            '2018': 16,
            '2019': 12
        },
        {
            'name': 'Github',
            '2015': 2,
            '2016': 6,
            '2017': 17,
            '2018': 5,
            '2019': 10
        },
        {
            'name': 'Gephi',
            '2015': 11,
            '2016': 16,
            '2017': 14,
            '2018': 10,
            '2019': 9
        },
        {
            'name': 'GeoNames',
            '2015': 2,
            '2016': 4,
            '2017': 3,
            '2018': 1,
            '2019': 8
        },
        {
            'name': 'Transkribus',
            '2015': 0,
            '2016': 1,
            '2017': 2,
            '2018': 1,
            '2019': 8
        },
        {
            'name': 'Excel',
            '2015': 5,
            '2016': 9,
            '2017': 3,
            '2018': 6,
            '2019': 7
        },
        {
            'name': 'MySQL',
            '2015': 0,
            '2016': 6,
            '2017': 9,
            '2018': 5,
            '2019': 7
        }

    ]
    years = ['2015', '2016', '2017', '2018', '2019']
    add_overall(years, dh_tools_popularity_by_year)
    for tools in dh_tools_popularity_by_year:
        name = tools["name"]
        value_2015 = tools["2015"]
        value_2019 = tools["2019"]
        overall = tools["total_popularity"]
        print(f"The popularity for {name} in 2015 is {value_2015}.\n"
              f"The popularity for {name} in 2019 is {value_2019}.\n"
              f"The overall popularity for {name} is {overall}.\n")


def add_overall(years, table):
    for tools in table:
        overall = 0
        for year in years:
            overall += tools[year]
            tools['total_popularity'] = overall


def get_value(key, table):
    return table[key]


main()

