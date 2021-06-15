# Julia Cuellar
# DSC 540
# Final project

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import urllib.request as urllib2
from bs4 import BeautifulSoup
import urllib3
import requests
import sqlite3


# Read csv file
def read_csv_file():
    evcp = pd.read_csv('2019 EVCP use Q1 and Q2.csv')
    print("Csv data:\n", evcp)


# Drop 1st column from csv file
def csv_drop():
    evcp = pd.read_csv('2019 EVCP use Q1 and Q2.csv')
    evcp.drop('Charging event', axis=1, inplace=True)
    print("Remove 1st column from csv data:\n", evcp)


# Check, replace, and recheck the nulls from csv file
def csv_cpr_null():
    evcp = pd.read_csv('2019 EVCP use Q1 and Q2.csv')
    evcp.drop('Charging event', axis=1, inplace=True)
    print("Display csv data with null:\n", evcp.isnull())
    print("Display counts of null from csv data:\n", evcp.isnull().sum())
    evcp = evcp.fillna(" ")
    print("Display csv data with replaced nulls:\n", evcp)
    print("Display recounts of null from csv data:\n", evcp.isnull().sum())


# Rename Model column from csv file
def csv_rename_col():
    evcp = pd.read_csv('2019 EVCP use Q1 and Q2.csv')
    evcp.drop('Charging event', axis=1, inplace=True)
    evcp = evcp.fillna(" ")
    evcp.rename(columns={'Model': 'Charge'}, inplace=True)
    print("Rename Model column from csv data:\n", evcp)


# Display count plot of Total kWh column from csv file
def csv_showCountplot_kWh():
    evcp = pd.read_csv('2019 EVCP use Q1 and Q2.csv')
    evcp.drop('Charging event', axis=1, inplace=True)
    evcp = evcp.fillna(" ")
    evcp.rename(columns={'Model': 'Charge'}, inplace=True)
    sns.countplot(x='Total kWh', data=evcp)
    plt.title('kWh')
    plt.show()


# Display count plot of Site column from csv file
def csv_showCountplot_Site():
    evcp = pd.read_csv('2019 EVCP use Q1 and Q2.csv')
    evcp.drop('Charging event', axis=1, inplace=True)
    evcp = evcp.fillna(" ")
    evcp.rename(columns={'Model': 'Charge'}, inplace=True)
    sns.countplot(x='Site', data=evcp)
    plt.title('Site')
    plt.show()


# Display count plot of Charge column from csv file
def csv_showCountplot_Charge():
    evcp = pd.read_csv('2019 EVCP use Q1 and Q2.csv')
    evcp.drop('Charging event', axis=1, inplace=True)
    evcp = evcp.fillna(" ")
    evcp.rename(columns={'Model': 'Charge'}, inplace=True)
    sns.countplot(x='Charge', data=evcp)
    plt.title('Charge')
    plt.show()


# Display final format of csv file
def read_csv_2():
    evcp = pd.read_csv('2019 EVCP use Q1 and Q2.csv')
    evcp.drop('Charging event', axis=1, inplace=True)
    evcp = evcp.fillna(" ")
    evcp.rename(columns={'Model': 'Charge'}, inplace=True)
    evcp.to_csv('2019 EVCP use Q1-Q2.csv')


# Read web data
def read_web():
    response = urllib2.urlopen('https://data.wa.gov/Transportation/Electric-Vehicle-Population-Data/f6w7-q2d2/data')
    html_doc = response.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    evcp = soup.prettify()
    print(evcp)
    evcp_web = pd.read_csv('Electric_Vehicle_Population_Data.csv')
    print("Web data:\n", evcp_web)


# Drop 1st column from web data
def web_drop():
    response = urllib2.urlopen('https://data.wa.gov/Transportation/Electric-Vehicle-Population-Data/f6w7-q2d2/data')
    html_doc = response.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    evcp = soup.prettify()
    evcp_web = pd.read_csv('Electric_Vehicle_Population_Data.csv')
    evcp_web.drop('VIN (1-10)', axis=1, inplace=True)
    print("Remove 1st column from web data:\n", evcp_web)


# Check, replace, and recheck the nulls from web data
def web_cpr_null():
    response = urllib2.urlopen('https://data.wa.gov/Transportation/Electric-Vehicle-Population-Data/f6w7-q2d2/data')
    html_doc = response.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    evcp = soup.prettify()
    evcp_web = pd.read_csv('Electric_Vehicle_Population_Data.csv')
    evcp_web.drop('VIN (1-10)', axis=1, inplace=True)
    print("Display web data with null:\n", evcp_web.isnull())
    print("Display counts of null from web data:\n", evcp_web.isnull().sum())
    evcp_web = evcp_web.fillna(" ")
    print("Display web data with replaced nulls:\n", evcp_web)
    print("Display recounts of null from web data:\n", evcp_web.isnull().sum())


# Rename Electric Vehicle Type column from web data
def web_rename_col():
    response = urllib2.urlopen('https://data.wa.gov/Transportation/Electric-Vehicle-Population-Data/f6w7-q2d2/data')
    html_doc = response.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    evcp = soup.prettify()
    evcp_web = pd.read_csv('Electric_Vehicle_Population_Data.csv')
    evcp_web.drop('VIN (1-10)', axis=1, inplace=True)
    evcp_web = evcp_web.fillna(" ")
    evcp_web.rename(columns={'Electric Vehicle Type': 'Charge'}, inplace=True)
    print("Rename Electric Vehicle Type column from web data:\n", evcp_web)


# Display count plot of Electric Range column from web data
def web_showCountplot_ER():
    response = urllib2.urlopen('https://data.wa.gov/Transportation/Electric-Vehicle-Population-Data/f6w7-q2d2/data')
    html_doc = response.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    evcp = soup.prettify()
    evcp_web = pd.read_csv('Electric_Vehicle_Population_Data.csv')
    evcp_web.drop('VIN (1-10)', axis=1, inplace=True)
    evcp_web = evcp_web.fillna(" ")
    evcp_web.rename(columns={'Electric Vehicle Type': 'Charge'}, inplace=True)
    sns.countplot(x='Electric Range', data=evcp_web)
    plt.title('ER')
    plt.show()


# Display count plot of County column from web data
def web_showCountplot_County():
    response = urllib2.urlopen('https://data.wa.gov/Transportation/Electric-Vehicle-Population-Data/f6w7-q2d2/data')
    html_doc = response.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    evcp = soup.prettify()
    evcp_web = pd.read_csv('Electric_Vehicle_Population_Data.csv')
    evcp_web.drop('VIN (1-10)', axis=1, inplace=True)
    evcp_web = evcp_web.fillna(" ")
    evcp_web.rename(columns={'Electric Vehicle Type': 'Charge'}, inplace=True)
    sns.countplot(x='County', data=evcp_web)
    plt.title('county')
    plt.show()


# Display count plot of Charge column from web data
def web_showCountplot_Charge():
    response = urllib2.urlopen('https://data.wa.gov/Transportation/Electric-Vehicle-Population-Data/f6w7-q2d2/data')
    html_doc = response.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    evcp = soup.prettify()
    evcp_web = pd.read_csv('Electric_Vehicle_Population_Data.csv')
    evcp_web.drop('VIN (1-10)', axis=1, inplace=True)
    evcp_web = evcp_web.fillna(" ")
    evcp_web.rename(columns={'Electric Vehicle Type': 'Charge'}, inplace=True)
    sns.countplot(x='Charge', data=evcp_web)
    plt.title('charge')
    plt.show()


# Display final format of web data
def read_web_2():
    response = urllib2.urlopen('https://data.wa.gov/Transportation/Electric-Vehicle-Population-Data/f6w7-q2d2/data')
    html_doc = response.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    evcp = soup.prettify()
    evcp_web = pd.read_csv('Electric_Vehicle_Population_Data.csv')
    evcp_web.drop('VIN (1-10)', axis=1, inplace=True)
    evcp_web = evcp_web.fillna(" ")
    evcp_web.rename(columns={'Electric Vehicle Type': 'Charge'}, inplace=True)
    evcp_web.to_csv('Electric Vehicle Pop Data.csv')


# Read api data
def read_api():
    res = requests.get('https://data.wa.gov/resource/rpr4-cgyd.json')
    print(res)
    evcp_api = pd.read_csv('Electric_Vehicle_Title_and_Registration_Activity.csv')
    print("API data:\n", evcp_api)


# Drop multiple columns from api data
def api_drop():
    res = requests.get('https://data.wa.gov/resource/rpr4-cgyd.json')
    evcp_api = pd.read_csv('Electric_Vehicle_Title_and_Registration_Activity.csv')
    evcp_api.drop(['VIN (1-10)', 'Sale Price', 'DOL Transaction Date', '2015 HB 2778 Exemption Eligibility',
                   'Sale Date', '2019 HB 2042 Clean Alternative Fuel Vehicle (CAFV) Eligibility',
                   'Meets 2019 HB 2042 Electric Range Requirement', 'Meets 2019 HB 2042 Sale Date Requirement',
                   'Meets 2019 HB 2042 Sale Price/Value Requirement', 'Odometer Reading', 'Odometer Code'],
                  axis=1, inplace=True)
    print("Removal of multiple columns from api data:\n", evcp_api)


# Check, replace, and recheck the nulls from api data
def api_cpr_null():
    res = requests.get('https://data.wa.gov/resource/rpr4-cgyd.json')
    evcp_api = pd.read_csv('Electric_Vehicle_Title_and_Registration_Activity.csv')
    evcp_api.drop(['VIN (1-10)', 'Sale Price', 'DOL Transaction Date', '2015 HB 2778 Exemption Eligibility',
                   'Sale Date', '2019 HB 2042 Clean Alternative Fuel Vehicle (CAFV) Eligibility',
                   'Meets 2019 HB 2042 Electric Range Requirement', 'Meets 2019 HB 2042 Sale Date Requirement',
                   'Meets 2019 HB 2042 Sale Price/Value Requirement', 'Odometer Reading', 'Odometer Code'],
                  axis=1, inplace=True)
    print("Display api data with null:\n", evcp_api.isnull())
    print("Display counts of null from api data:\n", evcp_api.isnull().sum())
    evcp_api = evcp_api.fillna(" ")
    print("Display api data with replaced nulls:\n", evcp_api)
    print("Display recounts of null from api data:\n", evcp_api.isnull().sum())


# Rename Clean Alternative Fuel Vehicle Type column from api data
def api_rename_col():
    res = requests.get('https://data.wa.gov/resource/rpr4-cgyd.json')
    evcp_api = pd.read_csv('Electric_Vehicle_Title_and_Registration_Activity.csv')
    evcp_api.drop(['VIN (1-10)', 'Sale Price', 'DOL Transaction Date', '2015 HB 2778 Exemption Eligibility',
                   'Sale Date', '2019 HB 2042 Clean Alternative Fuel Vehicle (CAFV) Eligibility',
                   'Meets 2019 HB 2042 Electric Range Requirement', 'Meets 2019 HB 2042 Sale Date Requirement',
                   'Meets 2019 HB 2042 Sale Price/Value Requirement', 'Odometer Reading', 'Odometer Code'],
                  axis=1, inplace=True)
    evcp_api = evcp_api.fillna(" ")
    evcp_api.rename(columns={'Clean Alternative Fuel Vehicle Type': 'Charge'}, inplace=True)
    print("Rename Clean Alternative Fuel Vehicle Type column from api data:\n", evcp_api)


# Display count plot of New or Used Vehicle column from api data
def api_showCountplot_NU():
    res = requests.get('https://data.wa.gov/resource/rpr4-cgyd.json')
    evcp_api = pd.read_csv('Electric_Vehicle_Title_and_Registration_Activity.csv')
    evcp_api.drop(['VIN (1-10)', 'Sale Price', 'DOL Transaction Date', '2015 HB 2778 Exemption Eligibility',
                   'Sale Date', '2019 HB 2042 Clean Alternative Fuel Vehicle (CAFV) Eligibility',
                   'Meets 2019 HB 2042 Electric Range Requirement', 'Meets 2019 HB 2042 Sale Date Requirement',
                   'Meets 2019 HB 2042 Sale Price/Value Requirement', 'Odometer Reading', 'Odometer Code'],
                  axis=1, inplace=True)
    evcp_api = evcp_api.fillna(" ")
    evcp_api.rename(columns={'Clean Alternative Fuel Vehicle Type': 'Charge'}, inplace=True)
    sns.countplot(x='New or Used Vehicle', data=evcp_api)
    plt.title('N/U')
    plt.show()


# Display count plot of Electric Vehicle Fee Paid column from api data
def api_showCountplot_Fee():
    res = requests.get('https://data.wa.gov/resource/rpr4-cgyd.json')
    evcp_api = pd.read_csv('Electric_Vehicle_Title_and_Registration_Activity.csv')
    evcp_api.drop(['VIN (1-10)', 'Sale Price', 'DOL Transaction Date', '2015 HB 2778 Exemption Eligibility',
                   'Sale Date', '2019 HB 2042 Clean Alternative Fuel Vehicle (CAFV) Eligibility',
                   'Meets 2019 HB 2042 Electric Range Requirement', 'Meets 2019 HB 2042 Sale Date Requirement',
                   'Meets 2019 HB 2042 Sale Price/Value Requirement', 'Odometer Reading', 'Odometer Code'],
                  axis=1, inplace=True)
    evcp_api = evcp_api.fillna(" ")
    evcp_api.rename(columns={'Clean Alternative Fuel Vehicle Type': 'Charge'}, inplace=True)
    sns.countplot(x='Electric Vehicle Fee Paid', data=evcp_api)
    plt.title('Fee')
    plt.show()


# Display count plot of Charge column from api data
def api_showCountplot_Charge():
    res = requests.get('https://data.wa.gov/resource/rpr4-cgyd.json')
    evcp_api = pd.read_csv('Electric_Vehicle_Title_and_Registration_Activity.csv')
    evcp_api.drop(['VIN (1-10)', 'Sale Price', 'DOL Transaction Date', '2015 HB 2778 Exemption Eligibility',
                   'Sale Date', '2019 HB 2042 Clean Alternative Fuel Vehicle (CAFV) Eligibility',
                   'Meets 2019 HB 2042 Electric Range Requirement', 'Meets 2019 HB 2042 Sale Date Requirement',
                   'Meets 2019 HB 2042 Sale Price/Value Requirement', 'Odometer Reading', 'Odometer Code'],
                  axis=1, inplace=True)
    evcp_api = evcp_api.fillna(" ")
    evcp_api.rename(columns={'Clean Alternative Fuel Vehicle Type': 'Charge'}, inplace=True)
    sns.countplot(x='Charge', data=evcp_api)
    plt.title('charge')
    plt.show()


# Display final format of api data
def read_api_2():
    res = requests.get('https://data.wa.gov/resource/rpr4-cgyd.json')
    evcp_api = pd.read_csv('Electric_Vehicle_Title_and_Registration_Activity.csv')
    evcp_api.drop(['VIN (1-10)', 'Sale Price', 'DOL Transaction Date', '2015 HB 2778 Exemption Eligibility',
                   'Sale Date', '2019 HB 2042 Clean Alternative Fuel Vehicle (CAFV) Eligibility',
                   'Meets 2019 HB 2042 Electric Range Requirement', 'Meets 2019 HB 2042 Sale Date Requirement',
                   'Meets 2019 HB 2042 Sale Price/Value Requirement', 'Odometer Reading', 'Odometer Code'],
                  axis=1, inplace=True)
    evcp_api = evcp_api.fillna(" ")
    evcp_api.rename(columns={'Clean Alternative Fuel Vehicle Type': 'Charge'}, inplace=True)
    evcp_api.to_csv('Electric Vehicle Title-Registration Activity.csv')


# Read db file
def read_db_file():
    conn = sqlite3.connect("EVCP")
    cur = conn.cursor()
    cur.execute("SELECT UserID, CPID, Connector, StartDate, StartTime, EndDate, EndTime, TotalkWh, Site, Charge FROM "
                "Q1Q2")
    table = cur.fetchall()

    for i in table:
        print(i)

    cur.execute("SELECT County, City, State, ZIPCode, ModelYear, Make, Model, Charge, CAFV, ElectricRange, BaseMSRP, "
                "LegislativeDistrict, DOLVehicleID, VehicleLocation FROM Pop")
    table2 = cur.fetchall()

    for i in table2:
        print(i)

    cur.execute("SELECT Charge, ModelYear, Make, Model, NewUsed, TransactionType, TransactionYear, FeePaid, County, "
                "City, Zip, ElectricRange, BaseMSRP, PrimaryUse, State, DOLVehicleID, LegislativeDistrict FROM "
                "TitleRegistration")
    table3 = cur.fetchall()

    for i in table3:
        print(i)


# Combine tables from db file
def db_merge():
    conn = sqlite3.connect("EVCP")
    cur = conn.cursor()
    cur.execute("SELECT UserID, CPID, Connector, StartDate, StartTime, EndDate, EndTime, TotalkWh, Site, Charge FROM "
                "Q1Q2")
    table = cur.fetchall()
    df = pd.read_csv('2019 EVCP use Q1-Q2.csv')
    print(df)
    cur.execute("SELECT County, City, State, ZIPCode, ModelYear, Make, Model, Charge, CAFV, ElectricRange, BaseMSRP, "
                "LegislativeDistrict, DOLVehicleID, VehicleLocation FROM Pop")
    table2 = cur.fetchall()
    df2 = pd.read_csv('Electric Vehicle Pop Data.csv')
    print(df2)
    cur.execute("SELECT Charge, ModelYear, Make, Model, NewUsed, TransactionType, TransactionYear, FeePaid, County, "
                "City, Zip, ElectricRange, BaseMSRP, PrimaryUse, State, DOLVehicleID, LegislativeDistrict FROM "
                "TitleRegistration")
    table3 = cur.fetchall()
    df3 = pd.read_csv('Electric Vehicle Title-Registration Activity.csv')
    print(df3)
    df_final = df.merge(df2, how='outer') \
        .merge(df3, how='outer')
    print("Database shape: ", df_final.shape)


# Plots of db file
def db_showPlots():
    conn = sqlite3.connect("EVCP")
    cur = conn.cursor()
    cur.execute("SELECT UserID, CPID, Connector, StartDate, StartTime, EndDate, EndTime, TotalkWh, Site, Charge FROM "
                "Q1Q2")
    table = cur.fetchall()
    df = pd.read_csv('2019 EVCP use Q1-Q2.csv')
    cur.execute("SELECT County, City, State, ZIPCode, ModelYear, Make, Model, Charge, CAFV, ElectricRange, BaseMSRP, "
                "LegislativeDistrict, DOLVehicleID, VehicleLocation FROM Pop")
    table2 = cur.fetchall()
    df2 = pd.read_csv('Electric Vehicle Pop Data.csv')
    cur.execute("SELECT Charge, ModelYear, Make, Model, NewUsed, TransactionType, TransactionYear, FeePaid, County, "
                "City, Zip, ElectricRange, BaseMSRP, PrimaryUse, State, DOLVehicleID, LegislativeDistrict FROM "
                "TitleRegistration")
    table3 = cur.fetchall()
    df3 = pd.read_csv('Electric Vehicle Title-Registration Activity.csv')
    df_final = df.merge(df2, how='outer') \
        .merge(df3, how='outer')
    db = pd.read_csv('EVCP.csv')
    print(db)
    sns.countplot(x='Charge', data=db)
    plt.title('charge')
    plt.show()
    sns.countplot(x='Electric Range', data=db)
    plt.title('ER')
    plt.show()
    sns.countplot(x='Base MSRP', data=db)
    plt.title('b MSRP')
    plt.show()
    sns.countplot(y='Make', data=db)
    plt.title('make')
    plt.show()
    sns.countplot(x='Model', data=db)
    plt.title('model')
    plt.show()


if __name__ == "__main__":
    read_csv_file()
    csv_drop()
    csv_cpr_null()
    csv_rename_col()
    csv_showCountplot_kWh()
    csv_showCountplot_Site()
    csv_showCountplot_Charge()
    read_web()
    web_drop()
    web_cpr_null()
    web_rename_col()
    web_showCountplot_ER()
    web_showCountplot_County()
    web_showCountplot_Charge()
    read_api()
    api_drop()
    api_cpr_null()
    api_rename_col()
    api_showCountplot_NU()
    api_showCountplot_Fee()
    api_showCountplot_Charge()
    read_db_file()
    db_merge()
    db_showPlots()
