import csv 
import random


# Define the list of post types
post_types = ["Live Video",
              "Text Post",
              "IGTV",
              "Story", 
              "Short Video", 
              "Reel", 
              "Static", 
              "Quiz", 
              "Poll", 
              "Carousel"
            ]

# Generate 350 rows of random social media data
rows = []
for _ in range(500):
    post_type = random.choice(post_types)
    likes = random.randint(50, 350)
    shares = random.randint(10, 110)
    comments = random.randint(5, 80)
    rows.append([post_type, likes, shares, comments])

# Write the generated data to a CSV file
with open('data_generated.csv', mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Post_Type', 'Likes', 'Shares', 'Comments'])
    writer.writerows(rows)

print("Generated 500 rows of social media data in social_media_data_generated.csv")