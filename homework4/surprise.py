# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def names(dictionary):
    for key in dictionary:
        print(key)
names(targets)
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def name_and_spectraltype(dictionary):
    for key in dictionary:
        print(f"{key}, Spectral Type: {dictionary[key]["Spectral Type"]}")
name_and_spectraltype(targets)
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def stars_mag_greater_than(x,dictionary):
    print(f"Stars with magnitude greater than {x} mag:")
    for key in dictionary:
        if (dictionary[key]["Magnitude"]) > x:
            print(key)
stars_mag_greater_than(0.1, targets)
# 4) Look up another target, add all the necessary information to the targets list. 
targets["Procyon"]={"RA": "07h 39m 18.1s", "Dec": "+5° 13′ 30″", "Magnitude": 0.34, "Spectral Type": "F5 IV-V"}
print(targets)
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.

def declination_vector(declination): # This function changes the declination string into a vector (list)
    vec_dec = []                     # i.e., "+38° 47′ 01″" becomes [38, 47, 1]
    degrees = declination.split("°")
    if "+" in degrees[0]:
        vec_dec.append(int(degrees[0][1:]))
    else:
        vec_dec.append(-int(degrees[0][1:]))
    minutes = degrees[1]
    minutes_and_sec = minutes.split("′")
    vec_dec.append(int(minutes_and_sec[0]))
    vec_dec.append(int(minutes_and_sec[1][:-1]))
    return(vec_dec)

# def dec_difference_from(x, dictionary):
#     for key in dictionary:
#         key_dec = declination_vector(dictionary[key]["Dec"])
#         key_dec_difference = abs(key_dec[0] -x)
#         # print(f"{key}, {key_dec}, {key_dec_difference}")
#         return(key_dec_difference)

def difference_from(x, star, dictionary): # This function computes the distance from a given star's declination to 20°
    star_dec = declination_vector(dictionary[star]["Dec"])
    star_dec_diff = abs(star_dec[0] - x)
    return(star_dec_diff)

# for key in targets:
#     print(f"{key}")
#     print(targets[key]["Dec"])
#     print(declination_vector(targets[key]["Dec"]))
#     print(difference_from(20, key, targets))

def star_with_declination_closest_to(x, dictionary): # This function prints the star with declination closest to x (= 20°)
    star = "Vega"
    for key in dictionary:       
        if difference_from(x, key, dictionary) < difference_from(x, star, dictionary):
            star = key
    return(f"The star with declination closest to {x}° is {star}")

print(star_with_declination_closest_to(20, targets))

# 6) What is your favorite constellation?
# My favorite constellation is the Big Dipper !!!