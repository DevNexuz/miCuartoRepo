import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/DCcomics")
def get_dc_comics():
    rows = ["Superman", "Batman", "Flash", "Linterna Verde", "Mujer Maravilla", "Aquaman", "Shazam", "Cyborg"]
    return rows


@app.get("/MarvelComics")
def get_marvel_comics():
    rows = ["Spider-Man", "Iron Man", "Thor", "Hulk", "Black Widow", "Doctor Strange", "Black Panther", "Captain America"]
    return rows


@app.get("/EclipseComics_LOTR")
def get_eclipse_comics_lotr():
    rows = ["Frodo", "Sam", "Gandalf", "Aragorn", "Legolas", "Gimli", "Boromir", "Gollum", "El anillo"]
    return rows


@app.get("/StarWarsComics")
def get_starwars_comics():
    rows = ["Obiwan", "Mace Windu", "Darth Vader", "Qui-Gon Jinn", "Yoda"]
    return rows


@app.get("/DynamiteEntertainment_GOT")
def get_dynamite_entertainment_got():
    rows = ["Jon Snow", "Daenerys Targaryen", "Arya Stark", "Tyrion Lannister", "Cersei Lannister", "Jaime Lannister", "Bran Stark", "Sansa Stark"]
    return rows


@app.get("/TopCow")
def get_top_cow():
    rows = ["Witchblade", "The Darkness", "Cyberforce", "Magdalena", "Aphrodite IX"]
    return rows


@app.get("/DarkHorse")
def get_dark_horse():
    rows = ["Hellboy", "The Mask", "Sin City", "The Umbrella Academy", "Abe Sapien"]
    return rows


@app.get("/VertigoComics")
def get_vertigo_comics():
    rows = ["Morpheus (The Sandman)", "John Constantine", "V (V for Vendetta)", "Spider Jerusalem", "Jesse Custer"]
    return rows


@app.get("/IDWPublishing")
def get_idw_publishing():
    rows = ["Teenage Mutant Ninja Turtles", "Locke & Key", "Usagi Yojimbo", "Sonic the Hedgehog", "Transformers"]
    return rows


@app.get("/BoomStudios")
def get_boom_studios():
    rows = ["Erica Slaughter", "Lumberjanes", "Irredeemable", "Klaus", "Once & Future"]
    return rows


@app.get("/ImageComics")
def get_image_comics():
    rows = ["Spawn", "Invincible", "Savage Dragon", "Rick Grimes", "Marko", "Alana"]
    return rows


@app.get("/ChaosComics")
def get_chaos_comics():
    rows = ["Lady Death", "Evil Ernie", "Purgatori", "Chastity", "Cremator"]
    return rows


@app.get("/AlternaComics")
def get_alterna_comics():
    # Alterna es genial por sus títulos indie, así que puse nombres de sus obras/personajes
    rows = ["The Chair", "Mr. Crypt", "Blood Realm", "Trespasser", "It Came Out on a Wednesday"]
    return rows
