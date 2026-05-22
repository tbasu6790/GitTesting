def format_date(date_str):
    parts = date_str.split("-")
    return f"{parts[2]}/{parts[1]}/{parts[0]}"

def slugify(text):
    return text.lower().replace(" ", "-")
