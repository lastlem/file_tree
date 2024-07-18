import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def add_labels(x, y, names):
    for i in range(len(x)):
        plt.text(i, y[i], names[i], ha='center', fontsize=8)


def draw_plot(df: pd.DataFrame) -> None:
    df = df.sort_values('Space bytes', ascending=False).head(5)
    plt.figure(num=None, figsize=(10, 8), dpi=80, facecolor='w', edgecolor='r')
    ax = sns.barplot(x="name", y="Space bytes", hue=df['name'], data=df, orient='v')
    plt.xticks(rotation=15)
    for i, v in enumerate(df['Space']):
        ax.text(i, list(df['Space bytes'])[i] + 2, str(v), ha='center')
    plt.yticks([])
    plt.tight_layout()
    plt.show()


# import matplotlib.pyplot as plt
# import pandas as pd
#
#
# def add_labels(x, y, names):
#     for i in range(len(x)):
#         plt.text(i, y[i], names[i], ha='center', fontsize=8)
#
#
# def draw_plot(df: pd.DataFrame) -> None:
#     df = df.sort_values('Space bytes')
#     x, y = df['name'], df['Space bytes']
#
#     plt.bar(x, y, width=0.6)
#     # plt.yticks(y, df['Space'])
#     add_labels(x, list(y), list(df['Space']))
#     plt.xticks(rotation=15, fontsize=8)
#     plt.yticks(fontsize=8)
#     plt.show()
