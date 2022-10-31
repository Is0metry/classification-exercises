import seaborn as sns

tips = sns.load_dataset('tips')

total_bill_over_two = tips[tips.tip >=2]['total_bill']
print(total_bill_over_two)

tips = tips