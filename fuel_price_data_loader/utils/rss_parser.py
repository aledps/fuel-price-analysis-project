import xml.etree.ElementTree as ET

def parse_rss_feed(rss_data):
    root = ET.fromstring(rss_data)
    items = root.findall('.//item')

    data = []
    for item in items:
        title = item.find('title').text
        description = item.find('description').text
        brand = item.find('brand').text
        date = item.find('date').text
        price = float(item.find('price').text)
        trading_name = item.find('trading-name').text
        location = item.find('location').text
        address = item.find('address').text
        phone = item.find('phone').text
        latitude = float(item.find('latitude').text)
        longitude = float(item.find('longitude').text)
        site_features = item.find('site-features').text

        data.append((title, description, brand, date, price, trading_name, location, address, phone, latitude, longitude, site_features))

    return data