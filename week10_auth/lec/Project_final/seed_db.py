from travel import db, create_app, encoder
from travel.models import Destination
import json

#SEED = False # this will create an empty database with no data
SEED = True # this will also put sample data into the database
image_path = "/static/image/"

# This function populates the database
def populate_database_with_sample_data():
    destinations = [
        {
            "name": "Japan",
            "currency": "Japanese Yen (JPY)",
            "image": "Japan.jpeg",
            "description": "Japan combines ancient traditions with cutting-edge technology. Visitors can explore historic temples in Kyoto, experience the vibrant nightlife of Tokyo, relax in natural hot springs, and enjoy world-famous cuisine including sushi and ramen. Popular activities include cherry blossom viewing, hiking mountain trails, visiting cultural festivals, and shopping in modern entertainment districts."
        },
        {
            "name": "Australia",
            "currency": "Australian Dollar (AUD)",
            "image": "Australia.jpeg",
            "description": "Australia offers diverse travel experiences ranging from tropical beaches and coral reefs to rugged deserts and cosmopolitan cities. Travellers can snorkel the Great Barrier Reef, explore national parks, encounter unique wildlife such as kangaroos and koalas, and enjoy outdoor adventures including hiking, surfing, and camping in spectacular natural landscapes."
        },
        {
            "name": "Italy",
            "currency": "Euro (EUR)",
            "image": "Italy.jpeg",
            "description": "Italy is renowned for its rich history, art, architecture, and cuisine. Visitors can discover ancient Roman landmarks, explore Renaissance museums, dine on authentic pasta and pizza, and enjoy picturesque coastal villages. Activities include wine tasting, sightseeing in historic cities, visiting archaeological sites, and experiencing local cultural traditions."
        },
        {
            "name": "New Zealand",
            "currency": "New Zealand Dollar (NZD)",
            "image": "New_Zealand.jpeg",
            "description": "New Zealand attracts travellers seeking breathtaking scenery and outdoor adventure. Visitors can enjoy mountain hiking, glacier tours, scenic drives, and water sports in pristine natural environments. Popular activities include exploring national parks, visiting volcanic regions, experiencing Māori culture, and participating in adventure sports such as bungee jumping and kayaking."
        },
        {
            "name": "Thailand",
            "currency": "Thai Baht (THB)",
            "image": "Thailand.jpeg",
            "description": "Thailand is famous for tropical islands, vibrant street markets, ornate temples, and flavourful cuisine. Travellers can relax on sandy beaches, explore bustling night markets, visit cultural landmarks, and enjoy activities such as island hopping, scuba diving, boat tours, and cooking classes featuring traditional Thai dishes."
        },
        {
            "name": "Switzerland",
            "currency": "Swiss Franc (CHF)",
            "image": "Switzerland.jpeg",
            "description": "Switzerland offers stunning alpine scenery, charming villages, and excellent outdoor recreation opportunities. Visitors can ride scenic railways through mountain regions, ski world-class slopes, hike picturesque trails, and enjoy crystal-clear lakes. The country is also known for luxury travel experiences, fine chocolate, and historic European towns."
        },
        {
            "name": "Egypt",
            "currency": "Egyptian Pound (EGP)",
            "image": "Egypt.jpeg",
            "description": "Egypt attracts travellers interested in ancient history and archaeological wonders. Visitors can explore the pyramids, cruise along the Nile River, visit temples and museums, and learn about one of the world's oldest civilisations. Popular activities include desert tours, cultural sightseeing, photography, and exploring historic monuments."
        },
        {
            "name": "Canada",
            "currency": "Canadian Dollar (CAD)",
            "image": "Canada.jpeg",
            "description": "Canada offers vast wilderness, vibrant cities, and exceptional outdoor experiences. Travellers can visit spectacular national parks, observe wildlife, hike mountain trails, ski in winter resorts, and explore multicultural urban destinations. Popular activities include canoeing, camping, wildlife watching, and scenic road trips through forests and lakes."
        },
        {
            "name": "France",
            "currency": "Euro (EUR)",
            "image": "France.jpeg",
            "description": "France combines iconic cultural attractions, sophisticated cuisine, and diverse regional experiences. Visitors can admire historic architecture, explore world-famous museums, enjoy wine regions, and relax in charming countryside villages. Activities include culinary tours, shopping, sightseeing, cycling, and exploring coastal and mountain destinations."
        },
        {
            "name": "Costa Rica",
            "currency": "Costa Rican Colón (CRC)",
            "image": "Costa_Rica.jpeg",
            "description": "Costa Rica is a leading destination for ecotourism and nature-based travel. Visitors can explore rainforests, observe wildlife, relax on tropical beaches, and experience sustainable tourism attractions. Popular activities include zip-lining, volcano tours, bird watching, surfing, hiking, and guided wildlife excursions in protected national parks."
        },
    ]

    if Destination.query.count() == 0:
        for destination in destinations:
            embedding = encoder.encode(destination["description"])
            embedding_text = json.dumps(embedding.tolist())

            db.session.add(
                Destination(
                    name=destination["name"],
                    currency=destination["currency"],
                    description=destination["description"],
                    description_embedding=embedding_text,
                    image=image_path + destination["image"],
                )
            )
        db.session.commit()
        print("Database populated - did you copy the sample images into the package subfolder:",image_path,"?")
    else:
            print ("Aborted as destinations table is not empty")
  


# ############################################################
# Create (and potentially seed) the database
# ############################################################

if __name__ == "__main__": # so it can be run from the terminal
    app = create_app()
    with app.app_context():
        db.create_all()
        if SEED:
            populate_database_with_sample_data()