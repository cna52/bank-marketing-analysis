import pandas as pd
import matplotlib.pyplot as plt

def plot_target_distribution(df, target='deposit'):
    counts = df[target].value_counts()
    plt.bar(counts.index, counts.values)
    plt.title('Target Class Distribution')
    plt.xlabel(target)
    plt.ylabel('Count')
    plt.show()

def plot_numeric_histograms(df, cols):
    for c in cols:
        plt.figure()
        df[c].hist(bins=30)
        plt.title(f'Distribution of {c}')
        plt.xlabel(c)
        plt.ylabel('Frequency')
        plt.show()

def boxplot_numeric_by_target(df, num_col, target='deposit'):
    groups = [df[df[target]==v][num_col] for v in sorted(df[target].unique())]
    plt.boxplot(groups, labels=sorted(df[target].unique()))
    plt.title(f'{num_col} by {target}')
    plt.xlabel(target)
    plt.ylabel(num_col)
    plt.show()

def correlation_heatmap(df):
    corr = df.corr(numeric_only=True)
    plt.imshow(corr, cmap='coolwarm', aspect='auto')
    plt.title('Correlation Heatmap')
    plt.colorbar()
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.show()

def monthly_deposit_rate(df):
    tmp = df.copy()
    tmp['deposit_num'] = tmp['deposit'].map({'yes':1, 'no':0})
    order = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    tmp['month'] = pd.Categorical(tmp['month'], categories=order, ordered=True)
    rates = tmp.groupby('month')['deposit_num'].mean()
    rates.plot(kind='bar', title='Deposit Rate by Month')
    plt.ylabel('Subscription Rate')
    plt.show()
    return rates
