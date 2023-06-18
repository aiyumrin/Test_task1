import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
class StatisticPlot(object):
    def __init__(self, data):
        self.data = data

    def plots(self):
        colors = sns.color_palette(n_colors=10, palette='deep')
        self.plt_paths= []
        for col in self.data.columns[3:]:
            plt.figure(figsize=(15, 5), dpi=80)
            c = 0
            for corner in sorted(self.data['rb_corners'].unique()):
                plt_data = self.data.query('rb_corners == @corner')
                if plt_data.shape[0] > 1:
                    sns.kdeplot(plt_data.loc[:,col], fill=True, label=f'{corner} corners', color=colors[c])
                    c += 1
                else:
                    plt.axvline(plt_data.loc[:,col].values[0], 0, 1, label=f'{corner} corners', color=colors[c])
                    c += 1
    
            plt.title(f'{col} statistics')
            plt.legend()
            PLT_PATH = f'plots\{col}.png'
            self.plt_paths.append(PLT_PATH)
            plt.savefig(PLT_PATH)
            plt.show;

def draw_plots(json_path):
    data = pd.read_json(json_path, orient='columns')
    p = StatisticPlot(data)
    p.plots()
    print('Пути сохранения графиков:')
    for i in p.plt_paths:
        print(i)
    return p.plt_paths