def func(starting_chain, reaction_dict, n):
    # step 0: NNCB
    # step 1: NCNBCHB
    pairs = [starting_chain[i] + starting_chain[i + 1] for i in range(len(starting_chain) - 1)]
    chain_dict = {x: pairs.count(x) for x in reaction_dict.keys()}
    for step in range(n):
        new_dict = {x: 0 for x in reaction_dict.keys()}
        for i in chain_dict.items():
            if i[1] > 0:
                pair1 = i[0][0] + reaction_dict[i[0]]
                pair2 = reaction_dict[i[0]] + i[0][1]
                new_dict[pair1] += i[1]
                new_dict[pair2] += i[1]
        chain_dict = new_dict
    # generate single dict again for counting
    counts = {i: 0 for i in set("".join([i for i in chain_dict.keys()]))}
    for i in counts.keys():
        for j in chain_dict.keys():
            if i in j[0]:
                counts[i] += chain_dict[j]
    maximum = counts[max(counts, key=lambda x: counts[x])]
    minimum = counts[min(counts, key=lambda x: counts[x])]
    return maximum - minimum - 1


if __name__ == "__main__":
    with open("data.txt", "r") as file:
        d = file.read().split("\n\n")
    chain = [i for i in d[0]]
    reactions = {i.split(" -> ")[0]: i.split(" -> ")[1] for i in d[1].split("\n")}
    print(func(chain, reactions, 10))
    print(func(chain, reactions, 40))
