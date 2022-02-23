# dh_tools.py


def main():
    infile = open("tools_dh_proceedings.csv", "r")
    tools = []
    title = infile.readline()
    titles = title.replace("\n", "").replace("\ufeff", "").split(",")
    # print(titles)
    lines = infile.readlines()[1:]
    for line in lines:
        tool = line.replace("\n", "").split(",")
        tools.append(tool)
    tools = sorted(tools, key=lambda x: x[5], reverse=True)
    print(tools[0:10])

    calculate_total(tools,titles)

    print_tool(titles, tools)

    top_year_tool = top_year(titles, tools)
    print(top_year_tool)

    infile.close()


def top_year(titles, tools):
    year = input("Please enter a year to search: ")
    index = titles.index(year)
    tools = sorted(tools, key=lambda x: x[index], reverse=True)
    return tools[0]


def print_tool(titles, tools):
    name = input("Please enter a name to search: ")
    for tool in tools:
        string = ""
        if tool[0].lower() == name:
            for i in range(len(titles)):
                string = string + f"{titles[i]} is {tool[i]} \n"
            print(string)


def calculate_total(tools,titles):
    titles.append("total")
    for tool in tools:
        total = 0
        for idx in range(1, len(tool)):
            total = total + int(tool[idx])
        tool.append(total)
    print(tools[0:10])
    # print(titles)


main()