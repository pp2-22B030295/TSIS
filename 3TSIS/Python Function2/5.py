def average_by_categories(m):
    st , sac , sad , sd , sr , sw , sc , ss = 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0
    ct , cac , cad , cd , cr , cw , cc , cs = 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0
    for i in m:
        if i["category"] == "Thriller":
            st += i["imdb"]
            ct += 1
        elif i["category"] == "Action":
            sac += i["imdb"]
            cac += 1
        elif i["category"] == "Adventure":
            sad += i["imdb"]
            cad += 1
        elif i["category"] == "Drama":
            sd += i["imdb"]
            cd += 1
        elif i["category"] == "Romance":
            sr += i["imdb"]
            cr += 1
        elif i["category"] == "War":
            sw += i["imdb"]
            cw += 1
        elif i["category"] == "Crime":
            sc += i["imdb"]
            cc += 1
        elif i["category"] == "Suspense":
            ss += i["imdb"]
            cs += 1
    print("Thriller" , st / ct)
    print("Action" , sac / cac)
    print("Adventure" , sad / cad)
    print("Drama" , sd / cd)
    print("Romance" , sr / cr)
    print("War" , sw / cw)
    print("Crime" , sc / cc)
    print("Suspence", ss / cs)

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

average_by_categories(movies)