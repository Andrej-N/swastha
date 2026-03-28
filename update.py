import re

def update_swastha():
    with open('e:/PROJECTS/swashta_website/swastha_2.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Import Montserrat
    content = content.replace(
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=Outfit:wght@200;300;400;500&display=swap" rel="stylesheet">',
        '<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@200;300;400;500&family=Outfit:wght@200;300;400;500&display=swap" rel="stylesheet">'
    )

    # Change all Cormorant Garamond to Montserrat
    content = content.replace("font-family: 'Cormorant Garamond', serif;", "font-family: 'Montserrat', sans-serif;")

    # Fix CSS for specific elements
    content = content.replace(
        ".nav-logo-text {\n            font-family: 'Cormorant Garamond', serif;\n            font-size: 1.6rem; font-weight: 500;\n            letter-spacing: 0.08em;\n        }",
        ".nav-logo-text {\n            font-family: 'Montserrat', sans-serif;\n            font-size: 1.4rem; font-weight: 300;\n            letter-spacing: 0.25em; text-transform: uppercase;\n        }"
    )

    content = content.replace(
        ".hero-title {\n            font-family: 'Cormorant Garamond', serif; font-size: clamp(3.5rem, 10vw, 9rem);\n            font-weight: 300; line-height: 0.95; letter-spacing: -0.02em;\n        }",
        ".hero-title {\n            font-family: 'Montserrat', sans-serif; font-size: clamp(3.5rem, 10vw, 9rem);\n            font-weight: 200; line-height: 0.95; letter-spacing: 0.05em; text-transform: uppercase;\n        }"
    )

    content = content.replace(
        ".footer-brand-text { font-family: 'Cormorant Garamond', serif; font-size: 2rem; font-weight: 300; }",
        ".footer-brand-text { font-family: 'Montserrat', sans-serif; font-size: 1.8rem; font-weight: 300; letter-spacing: 0.2em; text-transform: uppercase; }"
    )

    # Remove italic from philosophy to fit Montserrat better
    content = content.replace("font-weight: 300; line-height: 1.5; font-style: italic;", "font-weight: 300; line-height: 1.5;")
    content = content.replace("font-weight: 300; line-height: 1.6; font-style: italic;", "font-weight: 300; line-height: 1.6;")

    # Content replacements
    content = content.replace('Artisan Indian Catering', 'Corporate Healthy Meal Catering')
    content = content.replace('Nourish &nbsp;&middot; &nbsp;Celebrate &nbsp;&middot; &nbsp;Elevate', 'Nourish &nbsp;&middot; &nbsp;Energize &nbsp;&middot; &nbsp;Elevate')
    content = content.replace('Swastha Catering — Nourish. Celebrate. Elevate.', 'Swastha Catering — Nourish. Energize. Elevate.')

    # Using re.sub for multiline strings just in case
    content = re.sub(
        r'Every dish we craft is an ode to tradition.*?bringing people together around a table\.',
        'We believe that great work starts with the right fuel. Our meals are crafted with intention to nourish your team, boost productivity, and foster a healthy, thriving workplace culture.',
        content, flags=re.DOTALL
    )

    content = content.replace('Wedding Feasts', 'Daily Office Lunches')
    content = content.replace('Grand celebrations deserve extraordinary cuisine. Multi-course experiences that honour tradition while delighting the modern palate.', 'Wholesome, balanced meals crafted daily to keep your team energized and focused throughout the work day.')

    content = content.replace('Corporate Events', 'Executive Dining')
    content = content.replace('Elevate corporate gatherings with thoughtfully crafted menus. From board luncheons to milestone celebrations, every detail perfected.', 'Premium culinary experiences designed for board meetings, client pitches, and executive retreats.')

    content = content.replace('Intimate Gatherings', 'Team Wellness Programs')
    content = content.replace('Private dinners and home celebrations given the same reverence as grand affairs. Bespoke menus for birthdays, anniversaries, and milestones.', 'Comprehensive meal plans tailored for your team’s nutritional wellbeing, ensuring peak performance and health.')

    content = content.replace('Wedding Banquet', 'Corporate Buffet')
    content = content.replace('Live Counters', 'Healthy Salad Bars')
    content = content.replace('Plated Service', 'Boardroom Dining')
    content = content.replace('Dessert Curation', 'Wholesome Snacks')

    old_marquee = """<span class="marquee-item">Weddings <span class="marquee-dot"></span></span>
        <span class="marquee-item">Corporate <span class="marquee-dot"></span></span>
        <span class="marquee-item">Private Dining <span class="marquee-dot"></span></span>
        <span class="marquee-item">Festivals <span class="marquee-dot"></span></span>
        <span class="marquee-item">Anniversaries <span class="marquee-dot"></span></span>
        <span class="marquee-item">Cultural Events <span class="marquee-dot"></span></span>
        <span class="marquee-item">Weddings <span class="marquee-dot"></span></span>
        <span class="marquee-item">Corporate <span class="marquee-dot"></span></span>
        <span class="marquee-item">Private Dining <span class="marquee-dot"></span></span>
        <span class="marquee-item">Festivals <span class="marquee-dot"></span></span>
        <span class="marquee-item">Anniversaries <span class="marquee-dot"></span></span>
        <span class="marquee-item">Cultural Events <span class="marquee-dot"></span></span>"""
    
    new_marquee = """<span class="marquee-item">Corporate Catering <span class="marquee-dot"></span></span>
        <span class="marquee-item">Healthy Lunches <span class="marquee-dot"></span></span>
        <span class="marquee-item">Workplace Wellness <span class="marquee-dot"></span></span>
        <span class="marquee-item">Team Gatherings <span class="marquee-dot"></span></span>
        <span class="marquee-item">Nutritious Meals <span class="marquee-dot"></span></span>
        <span class="marquee-item">Office Dining <span class="marquee-dot"></span></span>
        <span class="marquee-item">Corporate Catering <span class="marquee-dot"></span></span>
        <span class="marquee-item">Healthy Lunches <span class="marquee-dot"></span></span>
        <span class="marquee-item">Workplace Wellness <span class="marquee-dot"></span></span>
        <span class="marquee-item">Team Gatherings <span class="marquee-dot"></span></span>
        <span class="marquee-item">Nutritious Meals <span class="marquee-dot"></span></span>
        <span class="marquee-item">Office Dining <span class="marquee-dot"></span></span>"""
    content = content.replace(old_marquee, new_marquee)

    content = content.replace('Events Catered', 'Corporate Clients')
    content = content.replace('Years of Craft', 'Years in Business')
    content = content.replace('Signature Dishes', 'Healthy Recipes')
    content = content.replace('Happy Families', 'Meals Delivered')

    content = content.replace(
        '"Swastha transformed our wedding into an unforgettable culinary journey. Every dish told a story, every course was a revelation. Our guests still talk about it."',
        '"Swastha completely elevated our workplace. The daily healthy lunches keep our team energized and productive. It has been a fantastic addition to our company culture."'
    )
    content = content.replace('&mdash; Priya & Arjun, Chennai', '&mdash; Sarah T., HR Director')

    content = content.replace("Let's Craft Your<br>Perfect Celebration", "Let's Fuel<br>Your Team")
    content = content.replace("Every event begins with a conversation. Tell us your vision, and we'll bring it to life through flavour, artistry, and care.", "Every great workday starts with the right nutrition. Tell us about your team, and we will cater a plan that fosters health and productivity.")

    with open('e:/PROJECTS/swashta_website/swastha_2.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("Successfully updated swastha_2.html")

if __name__ == "__main__":
    update_swastha()
