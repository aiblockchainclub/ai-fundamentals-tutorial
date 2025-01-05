import matplotlib.pyplot as plt

# Data for the timeline
events = [
    ("1956", "Dartmouth AI Conference"),
    ("1966", "ELIZA, the first chatbot"),
    ("1997", "Deep Blue defeats chess champion"),
    ("2012", "AlexNet revolutionizes deep learning"),
    ("2020", "GPT-3 released by OpenAI")
]
years, descriptions = zip(*events)

# Plot the timeline
plt.figure(figsize=(10, 6))
plt.plot(years, [1]*len(years), 'ro', markersize=10)  # Markers
for i, desc in enumerate(descriptions):
    plt.text(years[i], 1.1, desc, rotation=45, ha='right')

plt.title("Timeline of AI Advancements")
plt.yticks([])
plt.show()
