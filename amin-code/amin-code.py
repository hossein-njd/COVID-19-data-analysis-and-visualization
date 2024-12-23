import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. بارگذاری داده‌ها از API یا فایل آنلاین
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
data = pd.read_csv(url)

# 2. انتخاب و پاکسازی داده‌ها
columns_of_interest = ["location", "date", "total_cases", "new_cases", "total_deaths", "new_deaths"]
data = data[columns_of_interest]
data['date'] = pd.to_datetime(data['date'])
data = data.dropna()

# 3. تحلیل داده‌ها
latest_data = data[data['date'] == data['date'].max()]
top_countries = latest_data.sort_values(by='total_cases', ascending=False).head(10)

print("Top 10 countries with highest total cases:")
print(top_countries[['location', 'total_cases']])

# 4. مصورسازی داده‌ها
plt.figure(figsize=(14, 8))
sns.barplot(x='total_cases', y='location', data=top_countries, palette='viridis')
plt.title("Top 10 countries with highest total COVID-19 cases")
plt.xlabel("Total Cases")
plt.ylabel("Country")
plt.show()

# روند کلی موارد جدید در سطح جهانی
world_data = data[data['location'] == 'World']
plt.figure(figsize=(14, 8))
plt.plot(world_data['date'], world_data['new_cases'], label='New Cases', color='orange')
plt.title("Global New COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.legend()
plt.show()
