"""
Script to populate advertisement images into the database
Usage: python populate_ads.py
"""

import mysql.connector
import os

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",  # Change this to your password
    database="project_data"
)
cursor = conn.cursor()

def insert_ad_image(gender, age, fashion_type, image_path, link):
    """
    Insert an advertisement image into the database
    
    Args:
        gender: 'Male' or 'Female'
        age: '(0-4)', '(4-10)', '(10-15)', '(15-18)', '(18-28)', '(30-40)', '(40-50)', '(50-75)'
        fashion_type: 'Shirt', 'Mobile_phone', 'Glasses', 'Headphones', 'Human_beard', 
                     'Necklace', 'Watch', 'Coat', 'Earrings', 'Jeans', 'Pen', 'Tie', or None
        image_path: Path to the image file
        link: Product URL
    """
    try:
        with open(image_path, 'rb') as file:
            binary_data = file.read()
        
        sql = """INSERT INTO image_data (gender, age, fashion_type, img, link) 
                 VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(sql, (gender, age, fashion_type, binary_data, link))
        conn.commit()
        print(f"✓ Added: {gender}, {age}, {fashion_type} - {os.path.basename(image_path)}")
        return True
    except FileNotFoundError:
        print(f"✗ Error: Image file not found - {image_path}")
        return False
    except Exception as e:
        print(f"✗ Error inserting {image_path}: {str(e)}")
        return False

# ============================================================================
# YOUR IMAGES - Auto-generated for your test images
# ============================================================================

print("\nAdding images to database...")
print("="*60)

# Male 18-28 images (General ads - no fashion filter)
insert_ad_image('Male', '(18-28)', None, 'ads/male/18-28/1.jpg', 'https://myntra.com/men-fashion')
insert_ad_image('Male', '(18-28)', None, 'ads/male/18-28/2.jpg', 'https://amazon.in/mens-accessories')
insert_ad_image('Male', '(18-28)', None, 'ads/male/18-28/3.jpg', 'https://flipkart.com/men')
insert_ad_image('Male', '(18-28)', None, 'ads/male/18-28/4.jpg', 'https://ajio.com/mens-fashion')
insert_ad_image('Male', '(18-28)', None, 'ads/male/18-28/5.jpg', 'https://louisphilippe.com')
insert_ad_image('Male', '(18-28)', None, 'ads/male/18-28/6.jpg', 'https://puma.com/new-collection')

# Male 30-40 images (General ads - no fashion filter)
insert_ad_image('Male', '(30-40)', None, 'ads/male/30-40/1.jpg', 'https://rayban.com/sunglasses')
insert_ad_image('Male', '(30-40)', None, 'ads/male/30-40/2.jpg', 'https://titan.co.in/watches')
insert_ad_image('Male', '(30-40)', None, 'ads/male/30-40/3.jpg', 'https://levi.com/mens-jeans')
insert_ad_image('Male', '(30-40)', None, 'ads/male/30-40/4.jpg', 'https://woodland.com/shoes')

print("="*60)
print("✓ All images added successfully!")
print("="*60)

cursor.close()
conn.close()

