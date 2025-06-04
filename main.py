import pandas as pd
import matplotlib.pyplot as plt

callforservice_2024 = pd.read_csv('pd_calls_for_service_2024_datasd.csv')

callforservice_2024 ['DATE_TIME'] = pd.to_datetime(callforservice_2024['DATE_TIME'])
## print(callforservice_2024['DATE_TIME'].dtype)

## Filtering for July 1-7
july_week1_df = callforservice_2024 [
    (callforservice_2024 ['DATE_TIME'] >= '2024-07-01') &
    ( callforservice_2024 ['DATE_TIME'] <= '2024-07-7')
]

downtown_beats = [111, 112, 113, 114, 115]

# Filter July 1–7 calls to just Downtown beats
downtown_df = july_week1_df[july_week1_df['BEAT'].isin(downtown_beats)]

# Plot Downtown call volume
downtown_counts = downtown_df['BEAT'].value_counts().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
downtown_counts.plot(kind='bar', color='red')
plt.title('Call Frequency in Downtown San Diego (July 1–7, 2024)')
plt.xlabel('Beat Code')
plt.ylabel('Number of Calls')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

