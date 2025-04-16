from app import db, Products  # Importing from your existing app
import ollama

def get_competitor_prices(product_name):
    """Fetch all seller prices for a given product"""
    product = Products.query.filter_by(product_name=product_name).first()
    if product:
        return [product.price]  # Since `Products` already stores price
    return []

def suggest_dynamic_price(product_name, farmer_price):
    """Use AI to suggest a competitive price"""
    competitor_prices = get_competitor_prices(product_name)
    
    if not competitor_prices:
        return farmer_price  # No competitors, keep farmer's price

    avg_price = sum(competitor_prices) / len(competitor_prices)
    lowest_price = min(competitor_prices)

    prompt = f"""
    The current lowest price for {product_name} is ₹{lowest_price}/kg.
    The average price is ₹{avg_price}/kg.
    A new farmer wants to set a price of ₹{farmer_price}/kg.
    Suggest an optimal price that is competitive but profitable.
    """
    
    response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
    
    return response['message']['content']

if __name__ == "__main__":
    product_name = "Wheat"
    farmer_price = 45.0  # Example price set by farmer
    suggested_price = suggest_dynamic_price(product_name, farmer_price)
    print(f"💡 Suggested Price for {product_name}: ₹{suggested_price}/kg")
