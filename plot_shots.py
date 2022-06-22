import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_distance(player, df, distance=189, season=0):
    df = df[df['full_shooter_name'] == player]
    df = df[df['shot_distance'] <= distance]
    if season != 0:
        df = df[df['season'] == season]
    colors = np.where(df['event'] == 'Goal', 'g', 'r')

    f = plt.figure(figsize=(19,10))

    circle1 = plt.Circle((69, 22), 15, color='b', fill=False)
    circle2 = plt.Circle((69, -22), 15, color='b', fill=False)
    rect = plt.Rectangle(xy=(89,-3), width=3.33, height=6, alpha=0.5)
    plt.gca().add_patch(circle1)
    plt.gca().add_patch(circle2)
    plt.gca().add_patch(rect)
    plt.axvline(x=25, color='b')
    plt.axvline(x=89, color='b')
    plt.axvline(x=0, color='r')
    pos_x = np.arange(85, 89, 0.1)
    pos_y = np.sqrt(16 - (pos_x - 89)**2)
    plt.plot(pos_x, pos_y, color='b')
    neg_y = -pos_y
    plt.plot(pos_x, neg_y, color='b')
    plt.title('{0} Shots From {1} feet Away'.format(player, distance), fontsize=20)

    plt.scatter(x=df['st_x'], y=df['st_y'], s=14, c=colors, alpha=0.35)
    #plt.show()
    total_shots = len(df)
    total_goals = len(df[df['event'] == 'Goal'])
    shot_pct = total_goals / total_shots
    info_text = """Total shots: {}
Total goals: {}
Shot Percentage: {}""".format(total_shots, total_goals, shot_pct)
    return f, info_text