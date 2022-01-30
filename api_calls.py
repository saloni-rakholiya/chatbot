from urllib import response
import requests
from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast


T = TypeVar("T")

mainlist=[
    "updated",
    "country",
    "country info",
    "cases",
    "today cases",
    "deaths",
    "today deaths",
    "recovered",
    "today recovered",
    "active",
    "critical",
    "cases per one million",
    "deaths per one million",
    "tests",
    "tests per one million",
    "population",
    "continent",
    "one case per people",
    "one death per people",
    "one test per people",
    "active per one million",
    "recovered per one million",
    "critical per one million"
]
countries=[
    'united states',
'afghanistan',
'albania',
'algeria',
'american samoa',
'andorra',
'angola',
'anguilla',
'antarctica',
'antigua and barbuda',
'argentina',
'armenia',
'aruba',
'australia',
'austria',
'azerbaijan',
'bahamas',
'bahrain',
'bangladesh',
'barbados',
'belarus',
'belgium',
'belize',
'benin',
'bermuda',
'bhutan',
'bolivia',
'bosnia and herzegowina',
'botswana',
'bouvet island',
'brazil',
'brunei darussalam',
'bulgaria',
'burkina faso',
'burundi',
'cambodia',
'cameroon',
'canada',
'cape verde',
'cayman islands',
'central african rep',
'chad',
'chile',
'china',
'christmas island',
'cocos islands',
'colombia',
'comoros',
'congo',
'cook islands',
'costa rica',
'cote d`ivoire',
'croatia',
'cuba',
'cyprus',
'czech republic',
'denmark',
'djibouti',
'dominica',
'dominican republic',
'east timor',
'ecuador',
'egypt',
'el salvador',
'equatorial guinea',
'eritrea',
'estonia',
'ethiopia',
'falkland islands',
'faroe islands',
'fiji',
'finland',
'france',
'french guiana',
'french polynesia',
'french s. territories',
'gabon',
'gambia',
'georgia',
'germany',
'ghana',
'gibraltar',
'greece',
'greenland',
'grenada',
'guadeloupe',
'guam',
'guatemala',
'guinea',
'guinea-bissau',
'guyana',
'haiti',
'honduras',
'hong kong',
'hungary',
'iceland',
'india',
'indonesia',
'iran',
'iraq',
'ireland',
'israel',
'italy',
'jamaica',
'japan',
'jordan',
'kazakhstan',
'kenya',
'kiribati',
'korea (north)',
'korea (south)',
'kuwait',
'kyrgyzstan',
'laos',
'latvia',
'lebanon',
'lesotho',
'liberia',
'libya',
'liechtenstein',
'lithuania',
'luxembourg',
'macau',
'macedonia',
'madagascar',
'malawi',
'malaysia',
'maldives',
'mali',
'malta',
'marshall islands',
'martinique',
'mauritania',
'mauritius',
'mayotte',
'mexico',
'micronesia',
'moldova',
'monaco',
'mongolia',
'montserrat',
'morocco',
'mozambique',
'myanmar',
'namibia',
'nauru',
'nepal',
'netherlands',
'new caledonia',
'new zealand',
'nicaragua',
'niger',
'nigeria',
'niue',
'norfolk island',
'northern mariana islands',
'norway',
'oman',
'pakistan',
'palau',
'panama',
'papua new guinea',
'paraguay',
'peru',
'philippines',
'pitcairn',
'poland',
'portugal',
'puerto rico',
'qatar',
'reunion',
'romania',
'russian federation',
'rwanda',
'saint kitts and nevis',
'saint lucia',
'st vincent/grenadines',
'samoa',
'san marino',
'sao tome',
'saudi arabia',
'senegal',
'seychelles',
'sierra leone',
'singapore',
'slovakia',
'slovenia',
'solomon islands',
'somalia',
'south africa',
'spain',
'sri lanka',
'st. helena',
'st.pierre',
'sudan',
'suriname',
'swaziland',
'sweden',
'switzerland',
'syrian arab republic',
'taiwan',
'tajikistan',
'tanzania',
'thailand',
'togo',
'tokelau',
'tonga',
'trinidad and tobago',
'tunisia',
'turkey',
'turkmenistan',
'tuvalu',
'uganda',
'ukraine',
'united arab emirates',
'united kingdom',
'uruguay',
'uzbekistan',
'vanuatu',
'vatican city state',
'venezuela',
'vietnam',
'western sahara',
'yemen',
'yugoslavia',
'zaire',
'zambia',
'zimbabwe',
]
def get_country_data(s):
    response = requests.get("https://corona.lmao.ninja/v2/countries/"+s+"?yesterday=true&strict=false&query")
    if response.status_code == 200:
        print(response.json())
        return response.json()


# if __name__ == "__main__":
#     india_stat = get_country_data()
#     print(india_stat)