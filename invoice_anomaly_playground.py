import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv("invoice_anomaly_playground.csv")
df["DATE"] = pd.to_datetime(df["CAL_YEAR_MONTH"], format="%Y%m")

df = df.groupby(["DATE"]).sum().reset_index()


# Create a list of all the months between the minimum and maximum dates in the dataframe
min_date = df["DATE"].min().replace(day=1)
max_date = df["DATE"].max().replace(day=1) + pd.offsets.MonthEnd()
all_months = pd.date_range(min_date, max_date, freq="MS")

# Create a new dataframe with all the months and merge it with the original dataframe
all_months_df = pd.DataFrame({"DATE": all_months})
df = pd.merge(all_months_df, df, on="DATE", how="left")

# Calculate the mean
mean_price = df["INVOICE"].mean()

df["DIFF_FROM_MEAN"] = (df["INVOICE"] - mean_price) / 1500


# Plot the scatter plot using the new dataframe
# plt.scatter(merged_df["DATE"], merged_df["INVOICE"])

fig, ax = plt.subplots()
ax.scatter(df["DATE"], df["DIFF_FROM_MEAN"])

locator = mdates.MonthLocator()  # show every month
formatter = mdates.DateFormatter("%Y-%m")  # format the labels as 'YYYY-MM'
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

plt.xticks(rotation=45)

# Show the plot
plt.show()
