import networkx as nx
from pyvis.network import Network

# Load Gephi graph file
G = nx.read_graphml("sports.graphml")

# Create PyVis network
net = Network(height="800px", width="100%", directed=False, bgcolor="#000000", font_color="white")

net.set_options("""
var options = {
  "physics": {
    "forceAtlas2Based": {
      "gravitationalConstant": -100,
      "centralGravity": 0.005,
      "springLength": 20,
      "springConstant": 0.40,
      "damping": 0.6,
      "avoidOverlap": 0.5
    },
    "minVelocity": 0.5,
    "solver": "forceAtlas2Based",
    "timestep": 0.2,
    "stabilization": {
      "enabled": true,
      "iterations": 50
    }
  }
}
""")

type_sizes = {
   "league": 50,
   "team": 25,
   "owner": 10
}
default_size = 10

league_logo_urls = {
    "NBA": "https://upload.wikimedia.org/wikipedia/en/0/03/National_Basketball_Association_logo.svg",
    "NFL": "https://upload.wikimedia.org/wikipedia/en/a/a2/National_Football_League_logo.svg",
    "MLB": "https://brandlogos.net/wp-content/uploads/2024/02/major_league_baseball_mlb-logo_brandlogos.net_tswkl.png",
    "NHL": "https://upload.wikimedia.org/wikipedia/en/3/3a/05_NHL_Shield.svg"
}

team_logo_urls = {
    "49ers": "https://www.pikpng.com/pngl/b/244-2446534_green-bay-packers-helmet-clipart.png",
    "AC Milan": "https://upload.wikimedia.org/wikipedia/commons/d/d0/Logo_of_AC_Milan.svg",
    "Angels": "https://upload.wikimedia.org/wikipedia/commons/8/8b/Los_Angeles_Angels_of_Anaheim.svg",
    "Arsenal": "https://upload.wikimedia.org/wikipedia/hif/8/82/Arsenal_FC.png",
    "Aston Villa": "https://upload.wikimedia.org/wikipedia/en/9/9a/Aston_Villa_FC_new_crest.svg",
    "Astros": "https://upload.wikimedia.org/wikipedia/commons/6/6b/Houston-Astros-Logo.svg",
    "Atlanta Utd": "https://upload.wikimedia.org/wikipedia/en/b/bb/Atlanta_MLS.svg",
    "Athletics": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Oakland_A%27s_logo.svg",
    "Avalanche": "https://upload.wikimedia.org/wikipedia/en/4/45/Colorado_Avalanche_logo.svg",
    "Bears": "https://www.pikpng.com/pngl/b/20-204774_chicago-bears-helmet-clipart.png",
    "Bengals": "https://www.pikpng.com/pngl/b/86-862778_clipart-new-orleans-saints-helmet-png-download.png",
    "Bills": "https://static.wikia.nocookie.net/footbal/images/6/65/Buffalo_Bills_helmet_rightface.png",
    "Blackhawks": "https://upload.wikimedia.org/wikipedia/en/2/29/Chicago_Blackhawks_logo.svg",
    "Blazers": "https://upload.wikimedia.org/wikipedia/commons/3/33/Portland-Trail-Blazers-Logo-2002.png",
    "Blue Jackets": "https://upload.wikimedia.org/wikipedia/en/5/5d/Columbus_Blue_Jackets_logo.svg",
    "Blue Jays": "https://upload.wikimedia.org/wikipedia/de/e/e2/Logodertorontobluejays.svg",
    "Blues": "https://upload.wikimedia.org/wikipedia/en/e/ed/St._Louis_Blues_logo.svg",
    "Bournemouth": "https://upload.wikimedia.org/wikipedia/en/e/e5/AFC_Bournemouth_%282013%29.svg",
    "Brewers": "https://upload.wikimedia.org/wikipedia/en/b/b8/Milwaukee_Brewers_logo.svg",
    "Braves": "https://upload.wikimedia.org/wikipedia/en/f/f2/Atlanta_Braves.svg",
    "Broncos": "https://clipart-library.com/img/1383017.png",
    "Browns": "https://upload.wikimedia.org/wikipedia/en/d/d9/Cleveland_Browns_logo.svg",
    "Bruins": "https://upload.wikimedia.org/wikipedia/commons/1/12/Boston_Bruins.svg",
    "Bucks": "https://upload.wikimedia.org/wikipedia/en/4/4a/Milwaukee_Bucks_logo.svg",
    "Bucs": "https://clipart-library.com/img/1316969.png",
    "Bulls": "https://static.wikia.nocookie.net/logopedia/images/4/4d/Chicago_Bulls_Mascot.svg",
    "Canadiens": "https://upload.wikimedia.org/wikipedia/commons/6/69/Montreal_Canadiens.svg",
    "Canucks": "https://upload.wikimedia.org/wikipedia/en/3/3a/Vancouver_Canucks_logo.svg",
    "Cardinals": "https://upload.wikimedia.org/wikipedia/en/9/9d/St._Louis_Cardinals_logo.svg",
    "AZ Cardinals": "https://www.pikpng.com/pngl/b/133-1336692_helmet-clipart-arizona-cardinals-blank-white-football-helmet.png",
    "Capitals": "https://upload.wikimedia.org/wikipedia/en/7/73/Washington_Caps_Alternate.svg",
    "Cavaliers": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Cleveland_Cavaliers_logo.svg",
    "Celtics": "https://upload.wikimedia.org/wikipedia/en/8/8f/Boston_Celtics.svg",
    "Chargers": "https://www.pikpng.com/pngl/b/342-3423399_los-angeles-chargers-helmet-logo-clipart.png",
    "Charlotte FC": "https://upload.wikimedia.org/wikipedia/en/9/91/Charlotte_FC_logo.svg",
    "Chelsea FC": "https://upload.wikimedia.org/wikipedia/en/c/cc/Chelsea_FC.svg",
    "Chiefs": "https://clipart-library.com/data_images/261900.gif",
    "Clippers": "https://upload.wikimedia.org/wikipedia/en/e/ed/Los_Angeles_Clippers_%282024%29.svg",
    "CO Rapids": "https://upload.wikimedia.org/wikipedia/en/2/2b/Colorado_Rapids_logo.svg",
    "Colts": "https://www.pikpng.com/pngl/b/111-1115325_pitt-football-helmet-logo-clipart.png",
    "Commanders": "https://content.sportslogos.net/logos/7/6832/full/washington_commanders_logo_helmet_2022_sportslogosnet-9702.png",
    "Cowboys": "https://www.pikpng.com/pngl/b/116-1163734_dallas-cowboys-logo-dallas-cowboys-helmet-png-clipart.png",
    "Coyotes": "https://upload.wikimedia.org/wikipedia/en/9/9e/Arizona_Coyotes_logo_%282021%29.svg",
    "Crew": "https://upload.wikimedia.org/wikipedia/commons/9/98/Columbus_Crew_2_logo_white.png",
    "Cubs": "https://upload.wikimedia.org/wikipedia/commons/8/80/Chicago_Cubs_logo.svg",
    "D-Backs": "https://upload.wikimedia.org/wikipedia/commons/a/ac/Arizona_Diamondbacks_logo_teal.svg",
    "Devils": "https://loodibee.com/wp-content/uploads/New-Jersey-Devils-Symbol.png",
    "Dodgers": "https://upload.wikimedia.org/wikipedia/commons/f/f6/LA_Dodgers.svg",
    "Dolphins": "https://www.pikpng.com/pngl/b/261-2612762_dolphins-helmet-png-tennessee-football-helmet-logo-clipart.png",
    "Ducks": "https://upload.wikimedia.org/wikipedia/en/9/95/Anaheim_Ducks_logo_2024.svg",
    "Eagles": "https://www.pikpng.com/pngl/b/261-2612204_philadelphia-eagles-clipart-helmet-clipart-philadelphia-eagles-football.png",
    "Earthquakes": "https://upload.wikimedia.org/wikipedia/en/9/98/San_Jose_Earthquakes_2014.svg",
    "F1": "https://upload.wikimedia.org/wikipedia/commons/0/0d/F1_%28registered_trademark%29.svg",
    "Falcons": "https://assets.stickpng.com/thumbs/5895d6bbcba9841eabab6084.png",
    "FC Dallas": "https://upload.wikimedia.org/wikipedia/en/c/c9/FC_Dallas_logo.svg",
    "FL Panthers": "https://upload.wikimedia.org/wikipedia/en/4/43/Florida_Panthers_2016_logo.svg",
    "Flames": "https://upload.wikimedia.org/wikipedia/en/6/61/Calgary_Flames_logo.svg",
    "Flyers": "https://upload.wikimedia.org/wikipedia/commons/5/5b/Logo_Philadelphia_Flyers.svg",
    "G Knights": "https://upload.wikimedia.org/wikipedia/en/a/ac/Vegas_Golden_Knights_logo.svg",
    "Galaxy": "https://upload.wikimedia.org/wikipedia/commons/7/70/Los_Angeles_Galaxy_logo.svg",
    "Giants": "https://cdn.vox-cdn.com/uploads/chorus_asset/file/22680468/New_York_Giants_helmet_rightface.png",
    "Grizzlies": "https://logos-world.net/wp-content/uploads/2020/05/Memphis-Grizzlies-Emblem.png",
    "Guardians": "https://upload.wikimedia.org/wikipedia/en/a/a9/Guardians_winged_%22G%22.svg",
    "Hawks": "https://upload.wikimedia.org/wikipedia/en/2/24/Atlanta_Hawks_logo.svg",
    "Heat": "https://loodibee.com/wp-content/uploads/miami-heat-logo-vice-symbol.png",
    "Hornets": "https://upload.wikimedia.org/wikipedia/en/c/c4/Charlotte_Hornets_%282014%29.svg",
    "Hurricanes": "https://upload.wikimedia.org/wikipedia/en/3/32/Carolina_Hurricanes.svg",
    "Islanders": "https://upload.wikimedia.org/wikipedia/en/4/42/Logo_New_York_Islanders.svg",
    "Jazz": "https://static.wikia.nocookie.net/logopedia/images/5/5e/Utah_Jazz_logo.svg",
    "Jaguars": "https://www.pikpng.com/pngl/b/401-4019350_jacksonville-jaguars-helmet-logo-pittsburgh-steelers-logo-transparent.png",
    "Jets": "https://www.pikpng.com/pngl/b/494-4942586_new-york-jets-helmet-rightface-new-york-jets.png",
    "Kings": "https://upload.wikimedia.org/wikipedia/en/c/c7/SacramentoKings.svg",
    "Knicks": "https://upload.wikimedia.org/wikipedia/en/2/25/New_York_Knicks_logo.svg",
    "Kraken": "https://upload.wikimedia.org/wikipedia/en/4/48/Seattle_Kraken_official_logo.svg",
    "LAFC": "https://upload.wikimedia.org/wikipedia/commons/8/86/Los_Angeles_Football_Club.svg",
    "LA Kings": "https://upload.wikimedia.org/wikipedia/de/c/cb/Los_Angeles_Kings_Logo_%282011%29.svg",
    "Lakers": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Los_Angeles_Lakers_logo.svg",
    "Leeds Utd": "https://upload.wikimedia.org/wikipedia/en/5/54/Leeds_United_F.C._logo.svg",
    "Lightning": "https://www.pngmart.com/files/23/Tampa-Bay-Lightning-Logo-PNG-File.png",
    "Liverpool": "https://static.wikia.nocookie.net/logopedia/images/5/56/Liverpool_FC_logo_(1955-1968).gif",
    "Lions": "https://www.pikpng.com/pngl/b/62-620608_detroit-lions-helmet-chicago-bears-helmet-clipart.png",
    "Magic": "https://upload.wikimedia.org/wikipedia/en/1/10/Orlando_Magic_logo.svg",
    "Manchester Utd": "https://upload.wikimedia.org/wikipedia/en/7/7a/Manchester_United_FC_crest.svg",
    "Mariners": "https://upload.wikimedia.org/wikipedia/en/6/6d/Seattle_Mariners_logo_%28low_res%29.svg",
    "Marlins": "https://upload.wikimedia.org/wikipedia/en/f/fd/Marlins_team_logo.svg",
    "Maple Leafs": "https://upload.wikimedia.org/wikipedia/en/b/b6/Toronto_Maple_Leafs_2016_logo.svg",
    "Mavericks": "https://www.mavs.com/wp-content/themes/mavs/images/logo.svg",
    "Mets": "https://upload.wikimedia.org/wikipedia/en/7/7b/New_York_Mets.svg",
    "Minn Utd": "https://upload.wikimedia.org/wikipedia/en/e/e8/Minnesota_United_FC_%28MLS%29_Primary_logo.svg",
    "Nationals": "https://upload.wikimedia.org/wikipedia/commons/a/a3/Washington_Nationals_logo.svg",
    "Nets": "https://upload.wikimedia.org/wikipedia/commons/b/b5/Brooklyn_Nets_logo_primario_2024.png",
    "Nuggets": "https://upload.wikimedia.org/wikipedia/en/7/76/Denver_Nuggets.svg",
    "NYC FC": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Logo_New_York_City_FC_2025.svg",
    "Oilers": "https://upload.wikimedia.org/wikipedia/en/4/4d/Logo_Edmonton_Oilers.svg",
    "Orlando City": "https://upload.wikimedia.org/wikipedia/en/6/6a/Orlando_City_2014.svg",
    "Orioles": "https://upload.wikimedia.org/wikipedia/en/7/75/Baltimore_Orioles_cap.svg",
    "Pacers": "https://upload.wikimedia.org/wikipedia/en/thumb/1/1b/Indiana_Pacers.svg/1280px-Indiana_Pacers.svg.png",
    "Packers": "https://www.pikpng.com/pngl/b/393-3930619_green-bay-packers-helmets-through-the-years-images.png",
    "Padres": "https://upload.wikimedia.org/wikipedia/commons/c/cb/San_Diego_Padres_%282020%29_cap_logo.svg",
    "Panthers": "https://content.sportslogos.net/logos/7/174/full/345.gif",
    "Patriots": "https://www.pikpng.com/pngl/b/134-1349385_1024-x-853-4-patriots-football-helmet-png.png",
    "Pelicans": "https://cdn.freebiesupply.com/logos/large/2x/pelicans-logo-transparent.png",
    "Penguins": "https://upload.wikimedia.org/wikipedia/en/c/c0/Pittsburgh_Penguins_logo_%282016%29.svg",
    "Phillies": "https://upload.wikimedia.org/wikipedia/en/f/f0/Philadelphia_Phillies_%282019%29_logo.svg",
    "Pirates": "https://upload.wikimedia.org/wikipedia/it/a/a9/Pittsburgh_Pirates_Logo.png",
    "Pistons": "https://upload.wikimedia.org/wikipedia/commons/c/c9/Logo_of_the_Detroit_Pistons.svg",
    "Predators": "https://upload.wikimedia.org/wikipedia/en/9/9c/Nashville_Predators_Logo_%282011%29.svg",
    "R Sox": "https://upload.wikimedia.org/wikipedia/en/6/6d/RedSoxPrimary_HangingSocks.svg",
    "Rams": "https://upload.wikimedia.org/wikipedia/en/b/b7/NFL_Rams_Classical_Helmet.svg",
    "Rangers": "https://upload.wikimedia.org/wikipedia/commons/a/ae/New_York_Rangers.svg",
    "Raiders": "https://www.pikpng.com/pngl/b/158-1582210_oakland-raiders-revolution-speed-authentic-helmet-nfl-raiders.png",
    "Raptors": "https://upload.wikimedia.org/wikipedia/sco/3/36/Toronto_Raptors_logo.svg",
    "Ravens": "https://logohistory.net/wp-content/uploads/2023/01/Baltimore-Ravens-Helmet.png",
    "Rays": "https://upload.wikimedia.org/wikipedia/commons/5/52/Tampa_Bay_Rays_cap_logo.svg",
    "Red Wings": "https://www.khcsports.com/images/products/Detroit-Red-Wings-modern-disc-wall-sign.png",
    "Reds": "https://upload.wikimedia.org/wikipedia/commons/0/01/Cincinnati_Reds_Logo.svg",
    "Revolution": "https://upload.wikimedia.org/wikipedia/en/3/38/New_England_Revolution_%282021%29_logo.svg",
    "Rockets": "https://upload.wikimedia.org/wikipedia/it/archive/b/b9/20200923141106%21Houston_Rockets_logo.png",
    "Rockies": "https://logos-world.net/wp-content/uploads/2020/06/Colorado-Rockies-Emblem.png",
    "Royals": "https://upload.wikimedia.org/wikipedia/commons/7/78/Kansas_City_Royals_Primary_Logo.svg", 
    "Real Madrid": "https://upload.wikimedia.org/wikinews/en/b/bf/Real_Madrid_logo.png",
    "Sabres": "https://upload.wikimedia.org/wikipedia/en/9/9e/Buffalo_Sabres_Logo.svg",
    "Saints": "https://cdn.inspireuplift.com/uploads/images/seller_products/21338/iu_1712307942_1.png",
    "Seahawks": "https://www.pikpng.com/pngl/b/400-4000946_seahawks-helmet-cake-new-england-patriots-helm-clipart.png",
    "Senators": "https://upload.wikimedia.org/wikipedia/en/b/b2/Ottawa_Senators_2020-2021_logo.svg",
    "SF Giants": "https://upload.wikimedia.org/wikipedia/en/5/58/San_Francisco_Giants_Logo.svg",
    "Sharks": "https://upload.wikimedia.org/wikipedia/en/3/37/SanJoseSharksLogo.svg",
    "Sixers": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Philadelphia-76ers-Logo-1977-1996.png",
    "Sounders": "https://upload.wikimedia.org/wikipedia/en/2/27/Seattle_Sounders_FC.svg",
    "Spurs": "https://static.wikia.nocookie.net/sports-logos5931/images/a/ae/San_antonio_spurs_2003-present-aa.png",
    "Stars": "https://upload.wikimedia.org/wikipedia/en/c/ce/Dallas_Stars_logo_%282013%29.svg",
    "Steelers": "https://clipart-library.com/image_gallery/458887.png",
    "Suns": "https://static.wikia.nocookie.net/sports-logos5931/images/6/62/Phoenix_suns_2014-present-a.png",
    "T-wolves": "https://upload.wikimedia.org/wikipedia/en/c/c2/Minnesota_Timberwolves_logo.svg",
    "Texans": "https://operaglassnetworks.com/temp/NFL%20Logos/Team%20Logos/Texans/Logos/GIF/Helmets/tex-hel-34-rf-cl.gif",
    "Tigers": "https://www.pngall.com/wp-content/uploads/15/Detroit-Tigers-Logo-PNG-Photo.webp",
    "Titans": "https://www.pikpng.com/pngl/b/136-1367233_stellers-clipart-nfl-football-helmet-titans-football-helmet.png",
    "Thunder": "https://static.wikia.nocookie.net/sports-logos5931/images/9/96/Oklahoma_city_thunder_2009-present_p.png",
    "Twins": "https://upload.wikimedia.org/wikipedia/de/e/e3/Minnesota_Twins_Logo.svg",
    "TX Rangers": "https://upload.wikimedia.org/wikipedia/en/4/41/Texas_Rangers.svg",
    "Vikings": "https://clipart-library.com/images/dT4apGRTe.png",
    "Warriors": "https://upload.wikimedia.org/wikipedia/en/0/01/Golden_State_Warriors_logo.svg",
    "W Jets": "https://upload.wikimedia.org/wikipedia/en/9/93/Winnipeg_Jets_Logo_2011.svg",
    "W Sox": "https://images.squarespace-cdn.com/content/v1/60fcd40d5d1b740974b037ca/a181bfb4-48ca-43a7-a261-76503242904c/20220921+Chicago-White-Sox-Emblem.png",
    "Wild": "https://upload.wikimedia.org/wikipedia/en/1/1b/Minnesota_Wild.svg",
    "Wizards": "https://upload.wikimedia.org/wikipedia/en/0/02/Washington_Wizards_logo.svg",
    "Yankees": "https://upload.wikimedia.org/wikipedia/commons/f/fe/New_York_Yankees_Primary_Logo.svg"
}

positions = {
    'NFL': (0, 1000),
    'NBA': (-1000, 0),
    'MLB': (1000, 0),
    'NHL': (0, -1000)
}

for node, data in G.nodes(data=True):
    label = data.get("label", str(node))
    node_type = data.get("Type", "").strip().lower()

    # Default color based on type
    if node_type == "league":
        color = "#64c2ec"
    elif node_type == "team":
        color = "orange"
    else:
        r = data.get("r")
        g = data.get("g")
        b = data.get("b")
        if r and g and b:
            color = f"rgb({r},{g},{b})"
        else:
            color = "green"  # default fallback

    # Get size from type
    size = type_sizes.get(node_type, default_size)

    size_override = 100
    if label == "NBA":
      size_override = 65
    elif label == "MLB":
      size_override = 80


    # Conditionally use logo if available
    if label in league_logo_urls:
        x, y = positions.get(label, (None, None)) 
        net.add_node(
            node,
            label=" ",
            shape="image",
            image=league_logo_urls[label],
            size=size_override,
            x=x,
            y=y,
            fixed=False,
            shapeProperties={ 
                              "useImageSize": False,
                              "interpolation": False 
                            }
        )
    elif label in team_logo_urls:
        net.add_node(
            node,
            title=label,
            label=label,
            shape="image",
            image=team_logo_urls[label],
            size=20,
            shapeProperties={ 
                              "useImageSize": False,
                              "interpolation": False 
                            }
        )
    else:
        net.add_node(
            node,
            label=label,
            color=color,
            size=size
        )

# Add edges
import re
for source, target, data in G.edges(data=True):
    source_data = G.nodes[source]
    source_type = source_data.get("Type", "").strip().lower()
    
    raw_label = str(data.get("Edge Label", "")).strip()
    if re.match(r"^\d+%$", raw_label):
        edge_label = raw_label  # parses percentages
    else:
        edge_label = raw_label.title()
   
    weight = float(data.get("weight", 1))  # Default to 1 if not present
    spring_length = max(20, 100 - weight * 100)

    if source_type == "league":
        edge_color = "#64c2ec"  # light blue
        weight = 0.1
        spring_length = 300

    elif source_type == "owner":
        edge_color = "green"
        spring_length = 20

    elif source_type == "team":
        edge_color = "green"
        weight = 1

    else:
        edge_color = "green"
        weight = 1
        spring_length = 100

    # Add edge with defined styles
    net.add_edge(
        source,
        target,
        label=edge_label,
        font={'size': 10, 'color': 'white', 'strokeWidth': 0},
        title=edge_label,
        color=edge_color,
        width=weight,
        hover_width=3,
        length=spring_length
    )

# Show the network
net.show("index.html", notebook=False)


# Export
import json

def export_graph_to_d3(G, path):
    d3_data = {
        "nodes": [],
        "links": []
    }

    for node, attrs in G.nodes(data=True):
        d3_data["nodes"].append({
            "id": node,
            **attrs
        })

    for source, target, attrs in G.edges(data=True):
        d3_data["links"].append({
            "source": source,
            "target": target,
            **attrs
        })

    with open(path, 'w') as f:
        json.dump(d3_data, f, indent=2)

export_graph_to_d3(G, 'graph_data.json')
