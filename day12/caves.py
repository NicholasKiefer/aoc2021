def number_of_routes(data):
    all_caves = [x for y in data for x in y]
    caves = {x: [] for x in all_caves}
    for x in data:
        caves[x[0]].append(x[1])
        caves[x[1]].append(x[0])
    routes = [["start"]]
    starts = ["start"]
    while len(starts) > 0:
        start = starts[0]
        to_append = []
        for route in routes:
            current_exits = [i for i in caves[start] if i[0].isupper() or i not in route]
            for i in current_exits:
                if route[-1] == start:
                    new_route = [i for i in route]
                    new_route.append(i)
                    to_append.append(new_route)
        for i in to_append:
            if i not in routes:
                routes.append(i)
                if "end" not in i:
                    starts.append(i[-1])
        starts.remove(start)
        starts = list(set(starts))
    routes = [i for i in routes if i[0] == "start" and i[-1] == "end"]
    return len(routes)


"""
new approach: always check if end is reachable, otherwise prune
if end is reached add to final counter list
add all current end states to starts
"""


if __name__ == "__main__":
    with open("testdata.txt", "r") as file:
        d = file.read().splitlines()
    d = [x.split("-") for x in d]
    print(number_of_routes(d))
