"""
Author: Kaitlyn Clements
KID: 3072622
Date: 01/31
Assignment: MiniProject1
Description: Using Pandas and Altair to analyze and visualize a marathon dataset. 
Inputs: marathon_small.csv
"""

# Import Libraries
import pandas as pd
import altair as alt

"""
Step 1: Load and Explore the Data
"""
# Read dataset into a pandas DataFrame
data = pd.read_csv("data/marathon_small.csv")

# Print top 25 rows to get overview of data
print("Top 25 rows of dataset:")
print(data.head(25))

# Print shape of dataset (number of rows & columns)
print("\nDataset shape (rows, columns): ", data.shape)

"""
Step 2: Subset and Filter Data
"""
# Filter only male runners from dataset
males = data[data["sex"] == "male"]

# New dataframe with only the columns 'bmi' and 'km10_time_seconds'
males = males[["bmi", "km10_time_seconds"]]

# Remove rows where km10_time_seconds is missing
males = males.dropna(subset=["km10_time_seconds"])

"""
Step 3: Transform Data
"""
# Convert 10 km race time from seconds to minutes by dividing by 60
# Store results in new column, 'km10_time_minutes'
males["km10_time_minutes"] = males["km10_time_seconds"] / 60

"""
Step 4: Visualize the Relationship
"""
# Create Scatter plot using Altair. X-axis: bmi, Y-axis: kn10_time_minutes
scatter = (
    alt.Chart(males)
    .mark_circle(size=60)
    .encode(
        x=alt.X("bmi", title="Body Mass Index (BMI)"),
        y=alt.Y(
            "km10_time_minutes", title="10 km Race Time for Male Runners (minutes)"
        ),
    )
    .properties(title="Relationship between BMI and 10 km Race Time for Male Runners")
    .configure_axis(labelFontSize=12, titleFontSize=14)
)

# Render chart to save as an HTML file
scatter.save("scatter_plot.html")
# Display chart
scatter

# Altair won't display in regular Python script, so it is saved as an HTML to be opened in the browser
print(
    "Scatter chart saved to 'scatter_plot.html'. Open this file in a browser to view the visualization."
)

"""
Step 5: Interpret the Results
"""

# Define the interpretation in HTML format
interpretation_html = """<!DOCTYPE html>
<html>
<head>
    <title>Interpretation</title>
</head>
<body>
    <h1>Step 5: Interpret the Results</h1>
    <h2>Based on your visualization, answer the following question: What relationship do you observe between BMI and 10km race time?</h2>
    <h3>Answer: B - Positive correlation (Higher BMI → Longer race time)</h2>
    <p><strong>Explanation:</strong> The data visualization shows that as BMI increases, race time also increases for male runners. 
    This could be due to the fact that a higher body mass contributes to longer race completion times due to factors such as endurance and energy expenditure.</p>
</body>
</html>
"""

# Write the interpretation to an HTML file
with open("interpretation.html", "w") as file:
    file.write(interpretation_html)

print(
    "Interpretation saved to 'interpretation.html'. Open this file in a browser to view the formatted text."
)
