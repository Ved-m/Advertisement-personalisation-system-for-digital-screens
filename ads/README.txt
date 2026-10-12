HOW TO ORGANIZE YOUR ADVERTISEMENT IMAGES
==========================================

FOLDER STRUCTURE:
----------------
ads/
  ├── male/
  │   ├── 0-10/        ← Kids & pre-teens (0-4, 4-10 age groups)
  │   ├── 18-28/       ← Young adults
  │   ├── 30-40/       ← Adults
  │   ├── 40-50/       ← Middle-aged
  │   └── 50-75/       ← Seniors
  │
  └── female/
      ├── 0-10/        ← Kids & pre-teens (0-4, 4-10 age groups)
      ├── 18-28/       ← Young adults
      ├── 30-40/       ← Adults
      ├── 40-50/       ← Middle-aged
      └── 50-75/       ← Seniors


HOW TO ADD YOUR IMAGES:
-----------------------
1. Copy images into appropriate folders:
   - Male headphones ad for 18-28 → male/18-28/headphones1.jpg
   - Female earrings ad for 18-28 → female/18-28/earrings1.jpg
   - Kids toys → male/0-10/toys1.jpg (or female/0-10/toys1.jpg)

2. In populate_ads.py, add:
   insert_ad_image('Male', '(18-28)', 'Headphones', 
                   'ads/male/18-28/headphones1.jpg', 
                   'https://amazon.in/headphones')

   insert_ad_image('Female', '(18-28)', 'Earrings', 
                   'ads/female/18-28/earrings1.jpg', 
                   'https://tanishq.in/earrings')

   insert_ad_image('Male', '(0-4)', None, 
                   'ads/male/0-10/toys1.jpg', 
                   'https://hamleys.in/toys')


AGE GROUP MAPPING:
-----------------
Database uses these exact age categories:
- '(0-4)' and '(4-10)' → Use 0-10 folder (kids)
- '(18-28)' → Use 18-28 folder
- '(30-40)' → Use 30-40 folder
- '(40-50)' → Use 40-50 folder
- '(50-75)' → Use 50-75 folder

FASHION TYPES (for targeted ads):
---------------------------------
- Shirt, Mobile_phone, Glasses, Headphones
- Watch, Necklace, Earrings, Jeans
- Coat, Tie, Pen, Human_beard
- Use None for general ads (no fashion filter)

SUPPORTED IMAGE FORMATS:
------------------------
JPG, PNG, BMP, GIF

IMAGE REQUIREMENTS:
-------------------
- Recommended: 800x600 pixels or larger
- Clear, high-quality product images
- Match target demographic

NEXT STEPS:
-----------
1. Copy image files into appropriate folders (male/18-28/, female/30-40/, etc.)
2. Edit populate_ads.py and add your insert_ad_image() calls
3. Run: python populate_ads.py
4. Images stored in database → You can delete ads/ folder after
