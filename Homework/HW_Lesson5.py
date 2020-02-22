movie =     {
    "total_results": 4,
    "results": [
        {
            "popularity": 512.119,
            "vote_count": 460,
            "video": False,
            "poster_path": "https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg",
            "id": 475557,
            "adult": False,
            "backdrop_path": "https://image.tmdb.org/t/p/w500/f5F4cRhQdUbyVbB5lTNCwUzD6BP.jpg",
            "original_language": "en",
            "original_title": "Joker",
            "genres": [
                80,
                18,
                53
            ],
            "title": "Joker",
            "vote_average": 8.8,
            "overview": "During the 1980s, a failed stand-up comedian is driven insane and turns to a life of crime and chaos in Gotham City while becoming an infamous psychopathic crime figure.",
            "release_date": "2019-10-04"
        },
        {
            "popularity": 241.402,
            "vote_count": 598,
            "video": False,
            "poster_path": "https://image.tmdb.org/t/p/w500/a4BfxRK8dBgbQqbRxPs8kmLd8LG.jpg",
            "id": 429203,
            "adult": False,
            "backdrop_path": "https://image.tmdb.org/t/p/w500/6X2YjjYcs8XyZRDmJAHNDlls7L4.jpg",
            "original_language": "en",
            "original_title": "The Old Man & the Gun",
            "genres": [
                35,
                80,
                18
            ],
            "title": "The Old Man & the Gun",
            "vote_average": 6.3,
            "overview": "The true story of Forrest Tucker, from his audacious escape from San Quentin at the age of 70 to an unprecedented string of heists that confounded authorities and enchanted the public. Wrapped up in the pursuit are a detective, who becomes captivated with Forrest’s commitment to his craft, and a woman, who loves him in spite of his chosen profession.",
            "release_date": "2018-09-28"
        },
        {
            "popularity": 233.735,
            "vote_count": 4139,
            "video": False,
            "poster_path": "https://image.tmdb.org/t/p/w500/lcq8dVxeeOqHvvgcte707K0KVx5.jpg",
            "id": 429617,
            "adult": False,
            "backdrop_path": "https://image.tmdb.org/t/p/w500/5myQbDzw3l8K9yofUXRJ4UTVgam.jpg",
            "original_language": "en",
            "original_title": "Spider-Man: Far from Home",
            "genres": [
                28,
                12,
                878
            ],
            "title": "Spider-Man: Far from Home",
            "vote_average": 7.6,
            "overview": "Peter Parker and his friends go on a summer trip to Europe. However, they will hardly be able to rest - Peter will have to agree to help Nick Fury uncover the mystery of creatures that cause natural disasters and destruction throughout the continent.",
            "release_date": "2019-07-02"
        },
        {
            "popularity": 158.333,
            "vote_count": 323,
            "video": False,
            "poster_path": "https://image.tmdb.org/t/p/w500/kTQ3J8oTTKofAVLYnds2cHUz9KO.jpg",
            "id": 522938,
            "adult": False,
            "backdrop_path": "https://image.tmdb.org/t/p/w500/spYx9XQFODuqEVoPpvaJI1ksAVt.jpg",
            "original_language": "en",
            "original_title": "Rambo: Last Blood",
            "genres": [
                28,
                53
            ],
            "title": "Rambo: Last Blood",
            "vote_average": 6.1,
            "overview": "When John Rambo's niece travels to Mexico to find the father that abandoned her and her mother, she finds herself in the grasps of Calle Mexican sex traffickers. When she doesn't return home as expected, John learns she's crossed into Mexico and sets out to get her back and make them pay.",
            "release_date": "2019-09-20"
        }
    ]
}

# print('movie count:',movie['total_results'])
# print(end="\n")

# for k,v in movie['results'][0].items():
#     print(k+':',v)
# print(end="\n")

# for x in ['title', 'vote_average', 'genres']:
#     print(x+':',movie['results'][0][x])
# print(end="\n")

# for i in range (movie['total_results']):
#     for x in ['title', 'vote_average', 'genres']:
#         print(x+':',movie['results'][i][x])
#     print(end= "\n")

#DICTIONARY_PRACTICE
#PART1
# #1.
computer = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}
# #2.
# print('Số lượng MACBOOK trong kho:', computer['MACBOOK'])

# #3.
# computer_lookup = input('Nhập hãng máy tính cần tra cứu số lượng: ')
# print(f'Số lượng {computer_lookup} trong kho:', computer[computer_lookup])

# #PART2
# #4.
# computer['TOSHIBA'] = 10

# #5.
# update_k = input('Nhập hãng máy tính mới: ')
# update_v = int(input('Nhập số lượng máy tính mới: '))
# computer[update_k] = update_v

# #6.
# computer['DELL'] += 10
# computer['MACBOOK'] = 2

# #PART3
# #7
# for k,v in computer.items():
#     print(k+':', v)

# #8
# print('Tổng số máy tính trong kho:', sum(computer.values()))

# #9
computer['FUJITSU'] = 15
computer['ALIENWARE'] = 5

# #10
# for k,v in computer.items():
#     print(k+':', v)

# #PART4
# #1.
price = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 12000,
    'ASUS': 400,
    'ACER': 350,
    'TOSHIBA': 600,
    'FUJITSU': 900,
    'ALIENWARE': 1000
}
# #2. 
# print('Giá 1 máy ASUS:', price['ASUS'])

# #3.
# price_lookup = input('Nhập hãng máy tính cần tra cứu giá:')
# print(price[price_lookup])

#PART5
#4.
print('Tổng giá trị đơn hàng gồm 5 máy tính ASUS: ',5*price['ASUS'])

#5.
caculate_k = input('Nhập hãng máy tính trong đơn hàng: ')
caculate_v = int(input('Nhập số lượng máy tính trong đơn hàng: '))
print(f'Tổng giá trị hóa đơn gồm {caculate_v} máy tính {caculate_k}:', caculate_v*price[caculate_k])

#6.
computer[caculate_k] -= caculate_v

#7.
for k,v in computer.items():
    print(k+':', v)

#PART6
#8.
for c in computer.keys():
    print(f'Tổng giá trị của máy tính loại {c} là:', computer[c]*price[c])

#9.
total_price = 0
for c in computer.keys():
    total_price += computer[c]*price[c]
print(f'Tổng giá trị của toàn bộ máy tính trong kho là:', total_price)