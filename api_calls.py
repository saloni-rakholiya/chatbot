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

def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


@dataclass
class CountryInfo:
    id: Optional[int] = None
    iso2: Optional[str] = None
    iso3: Optional[str] = None
    lat: Optional[int] = None
    long: Optional[int] = None
    flag: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CountryInfo':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("_id"))
        iso2 = from_union([from_str, from_none], obj.get("iso2"))
        iso3 = from_union([from_str, from_none], obj.get("iso3"))
        lat = from_union([from_int, from_none], obj.get("lat"))
        long = from_union([from_int, from_none], obj.get("long"))
        flag = from_union([from_str, from_none], obj.get("flag"))
        return CountryInfo(id, iso2, iso3, lat, long, flag)

    def to_dict(self) -> dict:
        result: dict = {}
        result["_id"] = from_union([from_int, from_none], self.id)
        result["iso2"] = from_union([from_str, from_none], self.iso2)
        result["iso3"] = from_union([from_str, from_none], self.iso3)
        result["lat"] = from_union([from_int, from_none], self.lat)
        result["long"] = from_union([from_int, from_none], self.long)
        result["flag"] = from_union([from_str, from_none], self.flag)
        return result


@dataclass
class CountryStat:
    updated: Optional[int] = None
    country: Optional[str] = None
    country_info: Optional[CountryInfo] = None
    cases: Optional[int] = None
    today_cases: Optional[int] = None
    deaths: Optional[int] = None
    today_deaths: Optional[int] = None
    recovered: Optional[int] = None
    today_recovered: Optional[int] = None
    active: Optional[int] = None
    critical: Optional[int] = None
    cases_per_one_million: Optional[int] = None
    deaths_per_one_million: Optional[int] = None
    tests: Optional[int] = None
    tests_per_one_million: Optional[int] = None
    population: Optional[int] = None
    continent: Optional[str] = None
    one_case_per_people: Optional[int] = None
    one_death_per_people: Optional[int] = None
    one_test_per_people: Optional[int] = None
    active_per_one_million: Optional[float] = None
    recovered_per_one_million: Optional[float] = None
    critical_per_one_million: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CountryStat':
        assert isinstance(obj, dict)
        updated = from_union([from_int, from_none], obj.get("updated"))
        country = from_union([from_str, from_none], obj.get("country"))
        country_info = from_union([CountryInfo.from_dict, from_none], obj.get("countryInfo"))
        cases = from_union([from_int, from_none], obj.get("cases"))
        today_cases = from_union([from_int, from_none], obj.get("todayCases"))
        deaths = from_union([from_int, from_none], obj.get("deaths"))
        today_deaths = from_union([from_int, from_none], obj.get("todayDeaths"))
        recovered = from_union([from_int, from_none], obj.get("recovered"))
        today_recovered = from_union([from_int, from_none], obj.get("todayRecovered"))
        active = from_union([from_int, from_none], obj.get("active"))
        critical = from_union([from_int, from_none], obj.get("critical"))
        cases_per_one_million = from_union([from_int, from_none], obj.get("casesPerOneMillion"))
        deaths_per_one_million = from_union([from_int, from_none], obj.get("deathsPerOneMillion"))
        tests = from_union([from_int, from_none], obj.get("tests"))
        tests_per_one_million = from_union([from_int, from_none], obj.get("testsPerOneMillion"))
        population = from_union([from_int, from_none], obj.get("population"))
        continent = from_union([from_str, from_none], obj.get("continent"))
        one_case_per_people = from_union([from_int, from_none], obj.get("oneCasePerPeople"))
        one_death_per_people = from_union([from_int, from_none], obj.get("oneDeathPerPeople"))
        one_test_per_people = from_union([from_int, from_none], obj.get("oneTestPerPeople"))
        active_per_one_million = from_union([from_float, from_none], obj.get("activePerOneMillion"))
        recovered_per_one_million = from_union([from_float, from_none], obj.get("recoveredPerOneMillion"))
        critical_per_one_million = from_union([from_float, from_none], obj.get("criticalPerOneMillion"))
        return CountryStat(updated, country, country_info, cases, today_cases, deaths, today_deaths, recovered, today_recovered, active, critical, cases_per_one_million, deaths_per_one_million, tests, tests_per_one_million, population, continent, one_case_per_people, one_death_per_people, one_test_per_people, active_per_one_million, recovered_per_one_million, critical_per_one_million)

    def to_dict(self) -> dict:
        result: dict = {}
        result["updated"] = from_union([from_int, from_none], self.updated)
        result["country"] = from_union([from_str, from_none], self.country)
        result["countryInfo"] = from_union([lambda x: to_class(CountryInfo, x), from_none], self.country_info)
        result["cases"] = from_union([from_int, from_none], self.cases)
        result["todayCases"] = from_union([from_int, from_none], self.today_cases)
        result["deaths"] = from_union([from_int, from_none], self.deaths)
        result["todayDeaths"] = from_union([from_int, from_none], self.today_deaths)
        result["recovered"] = from_union([from_int, from_none], self.recovered)
        result["todayRecovered"] = from_union([from_int, from_none], self.today_recovered)
        result["active"] = from_union([from_int, from_none], self.active)
        result["critical"] = from_union([from_int, from_none], self.critical)
        result["casesPerOneMillion"] = from_union([from_int, from_none], self.cases_per_one_million)
        result["deathsPerOneMillion"] = from_union([from_int, from_none], self.deaths_per_one_million)
        result["tests"] = from_union([from_int, from_none], self.tests)
        result["testsPerOneMillion"] = from_union([from_int, from_none], self.tests_per_one_million)
        result["population"] = from_union([from_int, from_none], self.population)
        result["continent"] = from_union([from_str, from_none], self.continent)
        result["oneCasePerPeople"] = from_union([from_int, from_none], self.one_case_per_people)
        result["oneDeathPerPeople"] = from_union([from_int, from_none], self.one_death_per_people)
        result["oneTestPerPeople"] = from_union([from_int, from_none], self.one_test_per_people)
        result["activePerOneMillion"] = from_union([to_float, from_none], self.active_per_one_million)
        result["recoveredPerOneMillion"] = from_union([to_float, from_none], self.recovered_per_one_million)
        result["criticalPerOneMillion"] = from_union([to_float, from_none], self.critical_per_one_million)
        return result


def covid_stat_from_dict(s: Any) -> CountryStat:
    return CountryStat.from_dict(s)


def covid_stat_to_dict(x: CountryStat) -> Any:
    return to_class(CountryStat, x)


def get_country_data(s) -> CountryStat:
    response = requests.get("https://corona.lmao.ninja/v2/countries/"+s+"?yesterday=true&strict=false&query")
    if response.status_code == 200:
        return CountryStat.from_dict(response.json())


# if __name__ == "__main__":
#     india_stat = get_country_data()
#     print(india_stat)