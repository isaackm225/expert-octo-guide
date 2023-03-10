import csv

def log(name, email, timestamp, password, b):
    try:
        with open("creds.csv","x") as f:
            sheet = csv.writer(f)
            sheet.writerow([name,email,timestamp,password,b])#email,t
    except:
        with open("creds.csv","a") as f:
            sheet = csv.writer(f)
            sheet.writerow([name,email,timestamp,password,b])#name,email,t,pwd


TITLE = ["Sleep like a baby on our high-quality mattresses with delivery!", "Sleep like a baby with our comfortable, budget-friendly mattress"]


DESCRIPTIONS=[
"Looking for a comfortable and affordable mattress? Look no further! Our mattresses are designed for a good night's sleep. Contact us today at +13438055399 to learn more.",
"Say goodbye to restless nights and hello to the comfort of our mattresses! Affordable and comfortable, they're the perfect addition to any bedroom. Call us today at +13438055399 to learn more.",
"A good night's sleep is essential for a productive day. Our comfortable and affordable mattresses will give you just that! Contact us at +13438055399 to get your hands on one.",
"Don't sacrifice comfort for price. Our mattresses offer both! Get the sleep you deserve with our affordable and comfortable options. Call us today at +13438055399 to learn more.",
"If you're in need of a good night's sleep, we've got you covered. Our comfortable and affordable mattresses will have you sleeping soundly in no time. Contact us at +13438055399 to learn more.",
"Are you tired of waking up feeling exhausted? Our mattresses are designed for optimal comfort and affordability, so you can wake up feeling refreshed and ready for the day ahead. Contact us at +13438055399 to learn more.",
"A comfortable mattress shouldn't break the bank. Our affordable options offer the same level of comfort as the expensive brands. Call us today at +13438055399 to get your hands on one.",
"Your sleep quality can greatly affect your daily life. Improve your sleep with our comfortable and affordable mattresses. Contact us at +13438055399 to learn more.",
"Why pay more for a good night's sleep? Our mattresses offer the same level of comfort as the expensive brands, without the hefty price tag. Call us today at +13438055399 to learn more.",
"Getting a good night's sleep shouldn't be a luxury. Our affordable and comfortable mattresses make it possible for everyone to get the rest they deserve. Contact us at +13438055399 to learn more.",
"Say goodbye to restless nights and hello to a good night's sleep with our affordable and comfortable mattresses. Contact us at +13438055399 to get yours today.",
"Our mattresses are designed with your comfort in mind. Affordable and high-quality, they're the perfect addition to any bedroom. Call us today at +13438055399 to learn more.",
"If you're looking for a comfortable and affordable mattress, look no further. Our options are designed to provide the perfect night's sleep. Contact us at +13438055399 to learn more.",
"Don't settle for an uncomfortable and overpriced mattress. Our affordable options offer the same level of comfort without breaking the bank. Call us today at +13438055399 to learn more.",
"Upgrade your sleep game with our comfortable and affordable mattresses. You won't regret it! Contact us at +13438055399 to learn more.",
"If you're tired of waking up feeling groggy and unrested, it's time to upgrade your mattress. Our affordable and comfortable options are just what you need. Call us today at +13438055399 to learn more.",
"Your bed is where you spend a third of your life. Make it a comfortable experience with our affordable and high-quality mattresses. Contact us at +13438055399 to learn more.",
"Don't let an uncomfortable mattress ruin your sleep. Our affordable options will have you sleeping like a baby in no time. Contact us at +13438055399 to learn more.",
"A good night's sleep should be accessible to everyone. Our affordable and comfortable mattresses make it possible. Call us today at +13438055399 to get yours."
]

TAGS= [
"hypoallergenic mattresses",
"mattresses",
"affordable mattresses",
"comfortable mattresses",
"high-quality mattresses",
"memory foam mattresses",
"pillow-top mattresses",
"foam mattresses",
"spring mattresses",
"king-size mattresses",
"queen-size mattresses",
"twin-size mattresses",
"double-size mattresses",
"mattress sale",
"mattress discount",
"mattress clearance",
"mattress delivery",
"bedding",
"bedroom furniture",
"home decor",
"sleep solutions",
"back pain relief",
"sleep comfort",
"luxury mattresses",
"budget mattresses",
"orthopedic mattresses",
"hybrid mattresses",
"gel-infused mattresses",
"firm mattresses",
"soft mattresses",
"Euro-top mattresses",
"plush mattresses",
"pocketed coil mattresses",
"natural latex mattresses",
"eco-friendly mattresses",
"adjustable beds",
"box springs",
"mattress protectors",
"mattress toppers",
"custom mattresses",
"quality mattresses",
"sleep health",
"premium mattresses",
"firmness levels",
"sleep technology",
"sleep accessories",
"mattress financing",
"luxury bedding",
"sleep innovations",
"comfortable sleep"
]

ZIP = "Montreal, QC H3G"

PHONES = ["343 805 5399"]


PRICES = ["200","250","300","350","400","450","500"]

