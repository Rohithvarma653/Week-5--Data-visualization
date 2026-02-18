# Importing required library
import pandas as pd
import matplotlib.pyplot as plt

# Reading Titanic dataset
titanic_data = pd.read_csv("C:\\Datascience\\Data Visualization\\Week-5\\titanic (1).csv")

# -----------------------------
# 1. Bar Chart – Survival by Gender
# -----------------------------
gender_survival = titanic_data.groupby("sex")["survived"].sum()

fig, ax = plt.subplots()
ax.bar(gender_survival.index, gender_survival.values)

ax.set_title("Survival Count by Gender")
ax.set_xlabel("Gender")
ax.set_ylabel("Number of Survivors")

plt.show()


# -----------------------------
# 2. Box Plot – Age Distribution by Survival
# -----------------------------
survived = titanic_data[titanic_data["survived"] == 1]["age"].dropna()
not_survived = titanic_data[titanic_data["survived"] == 0]["age"].dropna()

fig, ax = plt.subplots()
ax.boxplot([not_survived, survived],
           labels=["Not Survived", "Survived"])

ax.set_title("Age Distribution by Survival")
ax.set_ylabel("Age")

plt.show()


# -----------------------------
# 3. Histogram – Age Distribution
# -----------------------------
fig, ax = plt.subplots()
ax.hist(titanic_data["age"].dropna(), bins=20)

ax.set_title("Age Distribution of Passengers")
ax.set_xlabel("Age")
ax.set_ylabel("Number of Passengers")

plt.show()


# -----------------------------
# 4. Scatter Plot – Age vs Fare
# -----------------------------
fig, ax = plt.subplots()
ax.scatter(titanic_data["age"], titanic_data["fare"])

ax.set_title("Age vs Fare")
ax.set_xlabel("Age")
ax.set_ylabel("Fare")

plt.show()
