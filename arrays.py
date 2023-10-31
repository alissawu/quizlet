#MATH
def get_DERIV():
    return [["d/dx sin(x)", "cos(x)"], ["d/dx cos(x)", "-sin(x)"],
            ["d/dx tan(x)", "sec^2(x)"], ["d/dx cot(x)", "-csc^2(x)"],
            ["d/dx sec(x)", "sec(x)tan(x)"], ["d/dx csc(x)", "-csc(x)cot(x)"],
            ["d/dx arcsin(x)", "1/sqrt(1-x^2)"],
            ["d/dx arccos(x)", "-1/sqrt(1-x^2)"],
            ["d/dx arctan(x)", "1/(1+x^2)"], ["d/dx arccot(x)", "-1/(1+x^2)"],
            ["d/dx arcsec(x)", "1/|x|sqrt(x^2-1)"],
            ["d/dx arccsc(x)", "-1/|x|sqrt(x^2-1)"], ["d/dx e^x", "e^x"],
            ["d/dx a^x", "a^xln(a)"], ["d/dx ln(x)", "1/x"],
            ["d/dx log_a[f(x)]", "f'(x) / f(x)ln(a)"],
            ["d/dx log_a(x)", "1/xln(a)"]]


#APAH
#APAH
def get_CONTEMPORARY():
    return [
        [
            "The Gates (author, medium, date)",
            "Christo and Jeanne-Claude, 1979-2005 CE, mixed-media"
        ],
        [
            "Vietnam Veterans Memorial (author, date, medium)",
            "Maya Lin, 1982 CE, Granite"
        ],
        [
            "A Book From The Sky (author, date, medium)",
            "Xu Bing, 1987-1991 CE, Paper + Print Press"
        ],
        [
            "No Crying in the Barbershop (author, date, medium)",
            "Pepon Osorio, 1994 CE, Mixed Media Installation"
        ],
        [
            "Guggenheim Museum (Bilbao) (author, date, medium)",
            "Frank Gehry, 1997 CE, titanium/glass/limestone"
        ],
        [
            "Darkytown Rebellion (author, date, medium)",
            "Kara Walker, 2001 CE, paper/wall projection"
        ],
        [
            "Shibboleth (author, date, medium)",
            "Doris Salcedo, 2008 CE, Installation"
        ],
        [
            "MAXXI National Museum of XXI Century Arts (author, date, medium)",
            "Zaha Hadid, 2009 CE, Glass/steel/cement"
        ],
        [
            "Sunflower Seeds (author, date, medium)",
            "Ai Wei Wei, 2011 CE, Sculpted and painted porcelain"
        ],
        [
            "Horn Players (author, date, medium)",
            "Jean-Michel Basquiat, 1983 CE, Acrylic/oil paint stick on triptych"
        ],
        [
            "Summer Trees (author, date, medium)",
            "Song Su-nam, 1983 CE, Ink on paper"
        ],
        [
            "Androgyn III (author, date, medium)",
            "Abakanowicz, 1985 CE, Burlap, resin, wood, nails, string"
        ],
        [
            "Pink Panther (author, date, medium)",
            "Jeff Koons, 1988 CE, Glazed Porcelain"
        ],
        [
            "Untitled #228 (author, date, medium)",
            "Cindy Sherman, 1990 CE, Photograph"
        ],
        [
            "Dancing at the Louvre (author, date, medium)",
            " Ringgold, 1991 CE, acrylic on canvas, tie-dyed pierced fabric border"
        ],
        [
            "Trade (Gifts for Trading Land with White People) (author, date, medium)",
            "Jaune Smith, 1992 CE, Oil and mixed media on canvas"
        ],
        [
            "Earth's Creation (artist, date, medium)",
            " Kngwarreye, 1994 CE, Synthetic polymer paint on canvas"
        ],
        [
            "Rebellious Silence (artist, date, medium)",
            "Shirin Neshat, 1994 CE, Ink on photograph"
        ],
        [
            "Pisupo Lua Afe (artist, date, medium)",
            "Michel Tuffrey, 1994 CE, Mixed Media"
        ],
        [
            "Electronic Superhighway (artist, date, medium)",
            "Nam June Paik, 1995, Mixed-media installation"
        ],
        [
            "The Crossing (artist, date, medium)",
            "Bill Viola, 1996 CE, Video/sound installation"
        ],
        [
            "Pure Land (artist, date, medium)",
            "Mariko Mori, 1998 CE, Color photograph on glass screenshot of 3D video"
        ],
        [
            "Lying with the Wolf (author, date, medium)",
            "Kiki Smith, 2001 CE, Ink and pencil on Paper"
        ],
        [
            "The Swing (artist, date, medium)",
            "Yinka Shonibare, 2001, Mixed-media installation"
        ],
        [
            "Old Man's Cloth (artist, date, medium)",
            "El Anatsui, 2003 CE, Aluminum and copper wire"
        ],
        [
            "Stadia II (artist, date, medium)",
            "Julie Mehretu, 2004 CE, Ink and acrylic on canvas"
        ],
        [
            "Preying Mantra (artist, date, medium)",
            "Wangechi Mutu, 2006 CE, Mixed media on mylar"
        ]
    ]

def get_PREHISTORIC_CULTURE():
  print("Choices: ", "Assyrian", "Babylonian", "Persian", "Sumerian", "Old", "New")
  return[["White Temple and Ziggurat","Sumerian"], ["Votive Figures", "Sumerian"],["Standard of Ur", "Sumerian"],["Law Code Stele of King Hammurabi", "Babylonian"],["Lamassu from the Citadel of Sargon II", "Assyrian"], ["Royal Apadana of Darius and Xerxes", "Persian"],["Palette of Narmer", "Predynastic"], ["Seated Scribe", "Old Kingdom"],["Great Pyramids of Giza", "Old Kingdom"], ["King Menkaure and his Wife", "Old Kingdom"], ["Pylon Temple of Amun-Re", "New Kingdom"], ["Mortuary Temple of Hatshepsut", "New Kingdom"], ["Akhenaten, Nefertiti, and Three Daughters", "Amarna"], ["King Tut's Tomb", "New Kingdom"], ["Last Judgement of Hu-Nefer", "New Kingdom"]]