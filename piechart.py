import matplotlib.pyplot as plt

labels = ["A", "B", "C", "D"]
sizes = [15, 30, 45, 10]

plt.pie(sizes, labels=labels,
        autopct="%1.1f%%", startangle=140)

centre_circle = plt.Circle((0,0),0.70,fc="white")
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis("equal")
plt.title("Basic Donut Chart")
plt.show()