import collections
import pandas as pd

if __name__ == "__main__":
    df = pd.read_excel("./data/Week1_challenge_data_source.xlsx")

    print("Top 10 handsets")
    handset_counter = collections.Counter(df["Handset Type"])
    for handset in sorted(handset_counter, key=lambda h: handset_counter[h], reverse=True)[:10]:
        print(handset, handset_counter[handset])
    print("=" * 60)

    print("Top 3 manufacturers and top 5 handsets for each of them")
    manufact_counter = collections.Counter(df["Handset Manufacturer"])
    for manufact in sorted(manufact_counter, key=lambda m: manufact_counter[m], reverse=True)[:10]:
        print(manufact, manufact_counter[manufact])
        handsets_by_manufact_counter = collections.Counter(
            df.loc[df["Handset Manufacturer"] == manufact]["Handset Type"])
        for handset in sorted(handsets_by_manufact_counter, key=lambda h: handsets_by_manufact_counter[h], reverse=True)[:5]:
            print("\t", handset, handsets_by_manufact_counter[handset])
