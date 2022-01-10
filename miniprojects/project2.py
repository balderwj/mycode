#!/usr/bin/env python3


import pandas as pd
import matplotlib.pyplot as plt

def main():
    # importing a module
    
    df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")    
    nbaDF = df[df['Team'] == "Lakers"]
    

    # organize counts to sort which college has most active NBA players
    #counts = df.College.value_counts()
    
    # top paid NBA players using counts.
    

    print(nbaDF)


main()



