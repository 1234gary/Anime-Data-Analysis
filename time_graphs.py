import seaborn as sns
import pandas as pd
import inspect
import os
import matplotlib.pyplot as plt
sns.set()
#sns.set_style("whitegrid")
tips = sns.load_dataset("tips")

module_path = inspect.getfile(inspect.currentframe())
module_dir = os.path.realpath(os.path.dirname(module_path))

data = pd.read_csv(module_dir+"/my_csv.csv", encoding = "ISO-8859-1")
data = data.set_index("ID")
print(list(data.columns.values))

data[['Score','Popularity']] = data[['Score','Popularity']].apply(pd.to_numeric,errors='coerce')
tv_data = data[data["Type"] == "TV"]
ova_data = data[data["Type"] == "OVA"]
combined_data = pd.concat([tv_data, ova_data])

non_h_combined_data = combined_data[combined_data["Rating"] != "Rx - Hentai"]

#how have genres changed over the years
#how has scoring changed over the years 
#how has source changed over the years 

#genre vs score
#source vs score
#genre vs popularity
#rating vs popularity

#genre/score/popularity for each studio (box plot chart for genres, diff graph per studio)

#histograms? beanplots?


def studio_vs_ratings():
    
    all_studio_data = []
    
    for studio in (non_h_combined_data.Studios.unique()):
        if ("," not in studio) and (studio != "None found, add some") and ((non_h_combined_data['Studios'] == studio).sum() > 20):
            studio_data = non_h_combined_data[non_h_combined_data['Studios'].str.contains(studio)]
            (studio_data.loc[:,['Studios']]) = studio 
            all_studio_data.append(studio_data)
        
    result = pd.concat(all_studio_data)

    ax = sns.boxplot(x="Studios", y="Score", data=result)
    plt.xticks(rotation=90)
    plt.tight_layout()
    sns.plt.show()
    
def studio_vs_popularity():
    
    all_studio_data = []
    
    for studio in (non_h_combined_data.Studios.unique()):
        if ("," not in studio) and (studio != "None found, add some") and ((non_h_combined_data['Studios'] == studio).sum() > 20):
            studio_data = non_h_combined_data[non_h_combined_data['Studios'].str.contains(studio)]
            (studio_data.loc[:,['Studios']]) = studio 
            all_studio_data.append(studio_data)
        
    result = pd.concat(all_studio_data)

    ax = sns.boxplot(x="Studios", y="Popularity", data=result)
    plt.xticks(rotation=90)
    plt.tight_layout()
    sns.plt.show()
    
def source_vs_ratings():
    
    all_source_data = []
    source_means = []
    source_stddev = []
    
    for source in (non_h_combined_data.Source.unique()):
        source_data = non_h_combined_data[non_h_combined_data['Source'] == source] 
        all_source_data.append(source_data)
        source_means.append(round(float(source_data.loc[:,["Score"]].mean()),2))
        source_stddev.append(round(float(source_data.loc[:,["Score"]].std()),2))
    result = pd.concat(all_source_data)
    
    ax = sns.boxplot(x="Source", y="Score", data=result)
    plt.xticks(rotation=45)
    plt.tight_layout()
    sns.plt.show()

def testing():
    #print((non_h_combined_data.Source.value_counts()))
    return
    
if __name__ == "__main__":
    source_vs_ratings()
    testing()
    