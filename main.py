#Imports
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Initial Datasets
hostnames=[]
dataset=[]
df=None

#Functions
def set_hostnames(number_of_hosts:int)->None:
    host_letter=['L']*4+['S']*3+['A']*2+['H']*1
    stage=['D']*10+['I']*10+['T']*25+['S']*25+['P']*30
    country=['NOR']*6+['FRA']*9+['ITA']*16+['ESP']*16+['DEU']*23+['IRL']*30
    grupo_alpha=[]
    
    for i in range (number_of_hosts):
        hostname=random.choice(host_letter)
        stage_choice=random.choice(stage)
        country_choice=random.choice(country)
        hostname += stage_choice
        hostname += country_choice
        grupo_alpha.append(hostname)
        hostname += str(grupo_alpha.count(hostname)).zfill(3)
        hostnames.append(hostname)

def get_os(hostname:str)->str:
    if hostname.startswith('L'):
        return 'Linux'
    elif hostname.startswith('S'):
        return 'Solaris'
    elif hostname.startswith('A'):
        return 'AIX'
    elif hostname.startswith('H'):
        return 'HP-UX'
    else:
        return 'Unknown'
    
def get_enviroment(hostname:str)->str:
    if hostname[1]=='D':
        return 'Development'
    elif hostname[1]=='I':
        return 'Integration'
    elif hostname[1]=='T':
        return 'Testing'
    elif hostname[1]=='S':
        return 'Staging'
    elif hostname[1]=='P':
        return 'Production'
    else:
        return 'Unkown'
    
def get_country(hostname:str)->str:
    if hostname[2:5]=='NOR':
        return 'Norway'
    elif hostname[2:5]=='FRA':
        return 'France'
    elif hostname[2:5]=='ITA':
        return 'Italy'
    elif hostname[2:5]=='ESP':
        return 'Spain'
    elif hostname[2:5]=='DEU':
        return 'Germany'
    elif hostname[2:5]=='IRL':
        return 'Irland'
    else:
        return 'Unknown'
    
def set_dataframe(count:int)->None:
    global df
    set_hostnames(count)
    for hostname in hostnames:
        dataset.append({
            'hostname':hostname,
            'os':get_os(hostname),
            'enviroment':get_enviroment(hostname),
            'country':get_country(hostname),
            'node':int(hostname[-3:])
        })
        
    df=pd.DataFrame(dataset)

#DataFrame from pandas
set_dataframe(1500)
print(df)
print('-------------------------------------------------------------')

#CSV of DataFrame from pandas
df.to_csv(
    'hosts.csv',
    header=True,
    index=False
)
hosts_df =pd.read_csv('hosts.csv')
print(hosts_df)
print('-------------------------------------------------------------')

#Graph countries & enviroment
country_enviroment=hosts_df.groupby( [hosts_df['country'], 'enviroment'] ).size()
country_enviroment.unstack().plot(kind='bar')
plt.show();

print('-------------------------------------------------------------')

#4 Executive graphs
figura, ejes = plt.subplots(2, 2, figsize=(12, 8))

country_os = hosts_df.groupby(['country', 'os']).size()
country_os.unstack().plot(kind='barh', ax=ejes[0, 0])
ejes[0, 0].set_title('Type of OS grouped by country')
ejes[0, 0].set_xlabel('Number of Hosts')
ejes[0, 0].set_ylabel('Country')

total_os = hosts_df['os'].value_counts()
porcentajes = total_os / total_os.sum() * 100
def func(pct, allvals):
    absolute = int(pct/100.*sum(allvals))
    return absolute
ejes[0, 1].pie(total_os, labels=[f'{os} ({porcentaje:.2f}%)' for os, porcentaje in zip(total_os.index, porcentajes)],
               autopct=lambda pct: func(pct, total_os))
ejes[0, 1].set_title('Total Operating Systems')
ejes[0, 1].legend(loc='upper right', bbox_to_anchor=(1.5, 1))

hosts_country = hosts_df['country'].value_counts()
paleta_colores = sns.color_palette("viridis", len(hosts_country))
ejes[1, 0].barh(hosts_country.index, hosts_country, color=paleta_colores)
ejes[1, 0].set_title('Total hosts by country')
ejes[1, 0].set_xlabel('Number of hosts')
ejes[1, 0].set_ylabel('Country')
for i, v in enumerate(hosts_country):
    ejes[1, 0].text(v + 10, i, str(v), color='black', va='center')
max_x = hosts_country.max() + 100
ejes[1, 0].set_xlim(0, max_x)

hosts_por_pais_y_entorno = hosts_df.groupby(['country', 'enviroment']).size().unstack(0)
hosts_por_pais_y_entorno.plot(kind='bar', ax=ejes[1, 1])
ejes[1, 1].set_title('Hosts by country grouped by enviroment')
ejes[1, 1].set_ylabel('Number of hosts')
ejes[1, 1].legend(loc='upper right', bbox_to_anchor=(.27, 1))

figura.tight_layout()
plt.show();