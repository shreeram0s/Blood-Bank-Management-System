import streamlit as st

# Set the page title
st.set_page_config(page_title="BLOOD BUDDY", page_icon="🩸")

# Header Section
st.title("Start Saving Lives")
st.image("Images/bb_logo(white).png", width=200)

# Video Section (Streamlit does not support video backgrounds directly)
st.video("video/homevideo1.mp4")

# About Us Section
st.header("What is this all about?")
st.write("We solve the problem of blood emergencies by connecting blood donors directly with people in blood need.")

# About Us Content
about_content = [
    {
        "title": "What we do?",
        "description": "We connect blood donors with recipients, without any intermediary such as blood banks, for an efficient and seamless process.",
        "image": "Images/drop.png"
    },
    {
        "title": "Innovative",
        "description": "Blood Buddy is an innovative approach to address global health. We provide immediate access to blood donors.",
        "image": "Images/innovation.png"
    },
    {
        "title": "Network",
        "description": "Blood Buddy is one of several community organizations working together as a network that responds to emergencies in an efficient manner.",
        "image": "Images/netwotk.png"
    },
    {
        "title": "Get notified",
        "description": "Blood Buddy Connect works with network partners to connect blood donors and recipients through an automated SMS service and a mobile app.",
        "image": "Images/noti.png"
    },
    {
        "title": "Totally Free",
        "description": "Blood Buddy's ultimate goal is to provide an easy-to-use, easy-to-access, fast, efficient, and reliable way to get life-saving blood, totally Free of cost.",
        "image": "Images/cost.png"
    },
    {
        "title": "Save Life",
        "description": "We are a non-profit foundation and our main objective is to make sure that everything is done to protect vulnerable persons. Help us by making a gift!",
        "image": "Images/save.png"
    }
]

for item in about_content:
    st.image(item["image"], width=100)
    st.subheader(item["title"])
    st.write(item["description"])

# Volunteer Section
st.header("Our Super Heroes")
volunteers = [
    {"name": "Garvit", "location": "Delhi, India", "blood_group": "O+"},
    {"name": "Mehere Kaur", "location": "Ghaziabad, Uttar Pradesh", "blood_group": "B+"},
    {"name": "Kenny", "location": "Kerela, India", "blood_group": "AB+"},
    {"name": "Sarah", "location": "Tamil Nadu, India", "blood_group": "A+"},
    {"name": "Kenneth", "location": "Ayodhya, Uttar Pradesh", "blood_group": "O+"},
    {"name": "Ritika", "location": "Ramnagar, Uttarakhand", "blood_group": "O+"},
    {"name": "Krish Maurya", "location": "Surat, Gujarat", "blood_group": "O-"},
    {"name": "Tushkar", "location": "Bengaluru, Karnataka", "blood_group": "AB+"},
    {"name": "Nitin", "location": "Lucknow", "blood_group": "AB-"},
    {"name": "Riya", "location": "Delhi, India", "blood_group": "B+"},
]

for volunteer in volunteers:
    st.write(f"*Name:* {volunteer['name']}, *Location:* {volunteer['location']}, *Blood Group:* {volunteer['blood_group']}")

# Testimonials Section
st.header("Testimonials")
testimonials = [
    {
        "text": "Blood Buddy is just awesome! I just donated for the first time and it could not have been easier. Blood Buddy is doing a very important work and I'm happy that I could contribute. It's hygienic, safe and convenient, I recommend it to everyone!",
        "name": "Esha Puri",
        "image": "Images/review-3.PNG"
    },
    {
        "text": "I found Blood Buddy at a time that my mother was in urgent need of blood. Blood Buddy arranged the required amount in no time. It saved us a lot of hassle and worry especially in such a trying time. Thank you Blood Buddy!",
        "name": "Amit Mangal",
        "image": "Images/review-2.PNG"
    },
    {
        "text": "I have been a part of this organization for quite some time and each time I'm amazed by the seamless and efficient system in place. The importance of timely care especially in the recent times is known and having Blood Buddy takes a load off my mind.",
        "name": "Dr. Kabir Khatri",
        "image": "Images/review-1.PNG"
    }
]

for testimonial in testimonials:
    st.image(testimonial["image"], width=50)
    st.write(f"{testimonial['name']}: {testimonial['text']}")

# Footer Section
st.write("2021 © All rights reserved.")
st.write("JOIN OUR CAUSE")
st.write("Donating blood or platelets can be intimidating and even scary. Time to put those hesitations and fears aside. Learn from Blood Buddy and platelet donors how simple and easy it is to roll up a sleeve and help save lives.")

# Social Media Links
st.write("Follow us on:")
st.markdown("[Facebook](https://www.facebook.com/givebloodnhs/) | [Instagram](https://www.instagram.com/indiablooddonation/?hl=en) | [Website](http://nbtc.naco.gov.in/)")
