import matplotlib.pyplot as plt
import numpy as np
import time

def get_pie_path(stats, labels):
    x = np.char.array(labels)
    y = np.array([stats[label] for label in x])
    colors = ['yellowgreen','red','gold','lightskyblue','white','lightcoral','blue','pink', 'darkgreen','yellow','grey','violet','magenta','cyan']
    porcent = 100.*y/y.sum()

    patches, texts = plt.pie(y, colors=colors, startangle=90, radius=1.2)
    labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(x, porcent)]

    sort_legend = True
    if sort_legend:
        patches, labels, dummy =  zip(*sorted(zip(patches, labels, y),
                                            key=lambda x: x[2],
                                            reverse=True))

    plt.legend(patches, labels, loc='center left', bbox_to_anchor=(-0.1, 1.),
            fontsize=8)

    file_name = f'charts/{time.time()}_piechart.png'
    plt.savefig(file_name)
    return file_name

def get_chart_path(stats):
    try:
        all_time_pie = get_pie_path(stats, ['recovered', 'deaths', 'active', 'critical'])
    except:
        all_time_pie = None
    try:
        daily_pie = get_pie_path(stats, ['todayCases', 'todayDeaths', 'todayRecovered'])
    except:
        daily_pie = None
    return all_time_pie, daily_pie

if __name__ == "__main__":
    stats = {
    "updated": 1643521013631,
    "country": "India",
    "countryInfo": {
        "_id": 356,
        "iso2": "IN",
        "iso3": "IND",
        "lat": 20,
        "long": 77,
        "flag": "https://disease.sh/assets/img/flags/in.png"
    },
    "cases": 41092522,
    "todayCases": 234281,
    "deaths": 494110,
    "todayDeaths": 892,
    "recovered": 38713494,
    "todayRecovered": 352784,
    "active": 1884918,
    "critical": 8944,
    "casesPerOneMillion": 29323,
    "deathsPerOneMillion": 353,
    "tests": 727390698,
    "testsPerOneMillion": 519052,
    "population": 1401383801,
    "continent": "Asia",
    "oneCasePerPeople": 34,
    "oneDeathPerPeople": 2836,
    "oneTestPerPeople": 2,
    "activePerOneMillion": 1345.04,
    "recoveredPerOneMillion": 27625.19,
    "criticalPerOneMillion": 6.38
    }
    get_chart_path(stats)
