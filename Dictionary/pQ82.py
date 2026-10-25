"""
create a dictionary mapping five countries to their capital cities.
Iterate through this dictionary using the items() method and print each pair in the format: 
Country --> Capital
"""
dic = {
    "Pakistan": "Islamabad",
    "Japan": "Tokyo",
    "France": "Paris",
    "Candana": "Ottawa",
    "Egypt": "Cairo"
}
for country, capital in dic.items():
    print(f"Country = {country}, Capital = {capital}")