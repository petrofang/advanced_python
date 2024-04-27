# (c) Giles Cooper 2024
"""Determine the characteristics of the set that you will display 
    via filtering and/or plots.

Submit a document that indicates the data set that you will be working 
with, and a explanation of each of the views you will be creating.  
(You may use one of the exercise requirements as an example of how to do this)

Your work with the file must include at least 8 views of the data and 2 plots.
"""
##############################################################################
"""
I will be working with the dataset of Dungeons & Dragons 5th edition monsters.

for views I might do:
    All dragons
    All humanoids
    All swimmers
    above/below a particular challenge threshold
    Some table based on their alignment 
    some sort of number crunch or data re-factoring that will allow me to
        import these directly into my game
    a user-interface that lets the user dynamically query the database?
    some of the values contain commas, eg "Speed" can assume walk/run but may
        also have options for burrow, swim, fly etc.. might see if we can 
        break those out and sort by swim speed, race & alignment, etc
    plenty of opportunity for data validation and interesting queries!

for plots:  
    alignment: good|neutral|evil vs lawful|neutral|chaotic
        heatmap? nested pie chart? I'm open to suggestions/challenges!
    histogram / distribution of HP / challenge rating / etc
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.patches import ConnectionPatch

FILE = "dnd5e_monsters.csv"

try:
    with open(FILE, 'r') as f:
       df = pd.read_csv(f)
except Exception as e:
    print(f"FILE NOT FOUND: {FILE}\n{e}")

# There's a lot of Data to parse here.. let's begin!

# First, parse "Race + alignment":
    # strip off the quotation marks
df['Race + alignment'] = df['Race + alignment'].str.strip('"')
    # split race and alignment to separate columns . . .
try: df[['Race', 'Alignment']] = df['Race + alignment'].str.split(',')
except Exception as e: print("ERROR:",e)
    # interestingly, the Were-beasts are making this difficult; see here:
def commas(string): return string.count(",")
werebeasts = df[df['Race + alignment'].apply(lambda x: commas(x)) >= 2]
print("\nList of Troublesome Data Monsters:")
print(werebeasts[['Name', 'Race + alignment']], end="\n\n")
    # The were-beasts, yes, but also the imp! A shape-changing devil-fiend
    # is causing an error in the code.. how apropos! 
    # ... so let's just split at the first comma from the right:
df[['Race', 'Alignment']] = df['Race + alignment'].str.rsplit(',',
                                                              n=1,
                                                              expand=True)
    # strip the leading space off alignment:
df['Alignment'] = df['Alignment'].str.strip()
    # Race and alignment are now isolated. 
del df['Race + alignment']

# Race itself kind of a mess too, let's see what we're dealing with:
races = df['Race'].value_counts().to_frame(name='Count').reset_index()
races.columns = ['Race', 'Count']
print("Races of creatures in D&D 5e (with complex data):")
print(races.to_string(index=False))
    # okay, that's some useful information, but there are too many out-lyers.
    # the sub-race and multi-race issues can be satisfied by removing anything
    # after the first word. But first, let's extract humanoid type data:
humanoids = df['Race'].loc[df['Race'].str.contains("humanoid")].reset_index(
    drop=True)
df['Race'] = df['Race'].apply(lambda x: x.split()[0])
races = df['Race'].value_counts().to_frame(name='Count').reset_index()
print(f"\nThere are {len(races)} primary types of creature listed:")
print(races, "\n")

    # not bad.. let's plot it! First, crunch that humanoid data:
        # distill the sub-race of each humanoid:
humanoids = humanoids.str[10:-1]
        # the were-beasts still plague us with their commas! how to sort
        # this data? Since we're counting the race types, I think they 
        # could count as both human and as shape-shifter, split to both:
humanoids = humanoids.str.split(', ').explode().str.strip().reset_index(drop=True)
        # now count it:
humanoids = humanoids.value_counts().reset_index(name='Count')
    # okay we have counts for each humanoid sub-race. 
print("Humanoid Sub-races and their counts:")
print(humanoids)
print("    Note that this does not include all *possible* types,",
      "only those specifically listed in the Monster Manual (5e).\n",
      sep="\n")

    # we'll do a bar-of-pie chart with the races and humanoid types:
# # # (adapted from matplotlib documentation)
# make figure and assign axis objects
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
fig.subplots_adjust(wspace=0)

# pie chart parameters
race_count = races['Count']
labels = races['Race']
# rotate so the humanoid wedge is split by the x-axis
explode = [0]*len(races)
explode[2] = .2
wedges, *_ = ax1.pie(race_count, labels=labels, 
                     startangle=170, explode=explode, 
                     shadow=True, counterclock=False,
                     autopct=lambda x: '%d' % round(x*sum(race_count)/100))
ax1.set_title("D&D 5e Creature Races")

# bar chart parameters
humanoid_count = humanoids['Count']
humanoid_label = humanoids['Race']
bottom = 1
width = .2

# Adding from the top matches the legend.
for j, (height, label) in enumerate(reversed([*zip(humanoid_count, humanoid_label)])):
    bottom -= height
    bc = ax2.bar(0, height, width, bottom=bottom, color=[0.1,.3,0], label=label,
                 alpha=(1/len(humanoid_count)) * j)
    ax2.bar_label(bc, labels=[f"{height}"], label_type='center')

ax2.set_title('Humanoid Sup-types')
ax2.legend()
ax2.axis('off')
ax2.set_xlim(- 2.5 * width, 2.5 * width)

# use ConnectionPatch to draw lines between the two plots
theta1, theta2 = wedges[2].theta2, wedges[2].theta1
center, r = wedges[2].center, wedges[2].r
bar_height = sum(humanoid_count)

# draw top connecting line
x = r * np.cos(np.pi / 180 * theta2) + center[0]
y = r * np.sin(np.pi / 180 * theta2) + center[1]
con = ConnectionPatch(xyA=(-width / 2, -bar_height+1), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
con.set_color([0, .25, 0])
con.set_linewidth(1)
ax2.add_artist(con)

# draw bottom connecting line
x = r * np.cos(np.pi / 180 * theta1) + center[0]
y = r * np.sin(np.pi / 180 * theta1) + center[1]
con = ConnectionPatch(xyA=(-width / 2, 1), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
con.set_color([0, .25, 0])
ax2.add_artist(con)
con.set_linewidth(1)

plt.text(-1.5,-50,"note: bar chart includes multi-type humanoids, accounting for higher total than in pie chart", size=10)
plt.show()
# # #

# Okay, now let's further parse through that alignment data we extracted earlier
    # First let's take a look at all our alignments and their counts:
alignments = df.Alignment.value_counts().reset_index(name='Count')
# print(alignments) 
    # okay, we've got all the standard ones, and a large number of unaligned...
    # but we've also got a lot of "Any Alignment", "Any Non-lawful", "Any Good",
    # and then there's Cloud Giants which are neither Lawful nor Chaotic, but
    # also always either Evil or Good (50% chance). This may be hard to parse.
    # First let's make a list of standard "normal" D&D alignments:
dnd_alignments = [
    "Lawful Good", "Neutral Good", "Chaotic Good",
    "Lawful Neutral", "Neutral", "Chaotic Neutral",
    "Lawful Evil", "Neutral Evil", "Chaotic Evil",
    "Unaligned",
]

non_std_align = df[~df['Alignment'].isin(dnd_alignments)].reset_index(drop=True)

print("List of creatures with non-specific alignments:")
print(non_std_align[['Name', 'Alignment']])
    # alright how to parse through these? Make an alignment chart?
alignment_chart = np.zeros([3,3])
    # okay load it up with the standard ones first:
alignment_chart[0,0] = len(df.loc[df.Alignment == 'Lawful Good'])
alignment_chart[1,0] = len(df.loc[df.Alignment == 'Lawful Neutral'])
alignment_chart[2,0] = len(df.loc[df.Alignment == 'Lawful Evil'])
alignment_chart[0,1] = len(df.loc[df.Alignment == 'Neutral Good'])
alignment_chart[1,1] = len(df.loc[df.Alignment == 'Neutral'])
alignment_chart[2,1] = len(df.loc[df.Alignment == 'Neutral Evil'])
alignment_chart[0,2] = len(df.loc[df.Alignment == 'Chaotic Good'])
alignment_chart[1,2] = len(df.loc[df.Alignment == 'Chaotic Neutral'])
alignment_chart[2,2] = len(df.loc[df.Alignment == 'Chaotic Evil'])
    # now add one to everything for "Any Alignment":
alignment_chart[:,:] += len(df.loc[df.Alignment == 'Any Alignment'])

print(alignment_chart)