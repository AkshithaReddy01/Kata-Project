"""Script to seed the database with Indian sweets"""
from app.database import SessionLocal, init_db
from app.models.sweet import Sweet

# Initialize database
init_db()

# Create database session
db = SessionLocal()

# Indian sweets data
indian_sweets = [
    {"name": "Gulab Jamun", "category": "Milk-based", "price": 25.00, "quantity": 50},
    {"name": "Rasgulla", "category": "Milk-based", "price": 20.00, "quantity": 60},
    {"name": "Kaju Katli", "category": "Dry Sweet", "price": 45.00, "quantity": 40},
    {"name": "Barfi", "category": "Milk-based", "price": 30.00, "quantity": 55},
    {"name": "Jalebi", "category": "Fried Sweet", "price": 15.00, "quantity": 80},
    {"name": "Ladoo", "category": "Dry Sweet", "price": 35.00, "quantity": 45},
    {"name": "Rasmalai", "category": "Milk-based", "price": 40.00, "quantity": 35},
    {"name": "Halwa", "category": "Halwa", "price": 28.00, "quantity": 50},
    {"name": "Peda", "category": "Milk-based", "price": 32.00, "quantity": 60},
    {"name": "Soan Papdi", "category": "Dry Sweet", "price": 22.00, "quantity": 70},
    {"name": "Besan Ladoo", "category": "Dry Sweet", "price": 30.00, "quantity": 55},
    {"name": "Kheer", "category": "Milk-based", "price": 35.00, "quantity": 40},
    {"name": "Gajar Halwa", "category": "Halwa", "price": 38.00, "quantity": 45},
    {"name": "Motichoor Ladoo", "category": "Dry Sweet", "price": 28.00, "quantity": 65},
    {"name": "Rabri", "category": "Milk-based", "price": 42.00, "quantity": 30},
    {"name": "Cham Cham", "category": "Milk-based", "price": 26.00, "quantity": 50},
    {"name": "Sandesh", "category": "Milk-based", "price": 33.00, "quantity": 55},
    {"name": "Kulfi", "category": "Frozen", "price": 20.00, "quantity": 75},
    {"name": "Malpua", "category": "Fried Sweet", "price": 18.00, "quantity": 60},
    {"name": "Gulab Jamun with Rabri", "category": "Milk-based", "price": 50.00, "quantity": 25},
    {"name": "Badam Halwa", "category": "Halwa", "price": 45.00, "quantity": 35},
    {"name": "Mysore Pak", "category": "Dry Sweet", "price": 40.00, "quantity": 40},
    {"name": "Kalakand", "category": "Milk-based", "price": 36.00, "quantity": 45},
    {"name": "Balushahi", "category": "Fried Sweet", "price": 24.00, "quantity": 55},
    {"name": "Imarti", "category": "Fried Sweet", "price": 16.00, "quantity": 70},
]

try:
    # Delete all existing sweets
    db.query(Sweet).delete()
    db.commit()
    print("Cleared existing sweets from database")
    
    added_count = 0
    
    for sweet_data in indian_sweets:
        new_sweet = Sweet(**sweet_data)
        db.add(new_sweet)
        added_count += 1
    
    db.commit()
    
    total_count = db.query(Sweet).count()
    print(f"\nSuccessfully added {added_count} Indian sweets!")
    print(f"   Total sweets in database: {total_count}")
    
    # Show categories
    categories = db.query(Sweet.category).distinct().all()
    print(f"\nCategories: {', '.join([c[0] for c in categories])}")
    
    # Show some examples
    print("\nSample sweets:")
    sweets = db.query(Sweet).limit(10).all()
    for sweet in sweets:
        print(f"  - {sweet.name} ({sweet.category}): Rs.{sweet.price:.2f} - Stock: {sweet.quantity}")
        
except Exception as e:
    print(f"Error adding sweets: {e}")
    import traceback
    traceback.print_exc()
    db.rollback()
finally:
    db.close()

