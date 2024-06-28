# <p align="center"> **Persona Compendium API**</p>

<p align="center">
    <i>I am thou... Thou art I...</i>
</p>
<p align="center">
  <a>
    <img src="https://i.imgur.com/GRSrswl.gif" height=100/>
  </a>
</p>


Table of Contents
======================================
1. [Overview](#overview)
2. [Features](#features)
3. [Tech Used](#tech-used)
4. [How to Use](#how-to-use)
5. [API Endpoints](#api-endpoints)

<a id ="overview"></a>
## ♠️ Overview

**Persona Compendium** is a read-only API that provides various informations about all the personas from *<strong>Persona 3 Reload</strong>*, the most recent game in the series to date. 

In its essence, it serves as a mirror of the compendium present in the game, responding the user's requests with a json containing **key characteristics from each persona**, such as its arcana, description, image, stats, resistances and more. 

It currently does not contain fusion possibilities nor price, those being possible future additions for the project.

### About the Data
The data which this API is based on was gathered from the following sources:
- [Megaten Database](https://github.com/aqiu384/megaten-database) is a open source database which contains a immense amount of data for the *Megami Tensei* games, including in-game stats, descriptions and more. Props to [aqiu384](https://github.com/aqiu384) for that!

- Images for the personas were taken directly from the [Megami Tensei Wiki](https://megatenwiki.com/wiki/Main_Page).

- And of course, literally all of the content is ripped from the *Megami Tensei/Persona* games developed by [Atlus Co., Ltd.](https://atlus.com/)

With that in mind, the API was created with the intention of being an **easy accessable source of persona information**, basically some kind of *"persona encyclopedia"*. This can help enthusiasts such as me to make their own projects related to the games!

<h6><em>
(Persona Compendium was made for study purposes only, as such, it has no copyright infringement intended. Persona and Megami Tensei are properties of Atlus Co., Ltd. and so all the content present in this API belong to their rightful owners)
</em></h6>

<a id ="features"></a>
## ♥️ Features
- List **all** personas in *Persona 3 Reload*, along with their respective information.
- Query for a **specific persona** from the game.
- Easily **customizable code** and endpoints.
- **TSV file** containing all the info present in the database.
<p align="right">
  <a>
    <img src="https://static.wikia.nocookie.net/megamitensei/images/4/46/Elizabeth_Idle_Stance_%28P4A%29.gif/" height=200/>
  </a>
</p>

<a id ="tech-used"></a>
## ♣️ Tech Used
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"></a>

<a href="https://fastapi.tiangolo.com/"><img src="https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white"></a>

<a href="https://www.postgresql.org/"><img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white"></a>

<a href="https://www.sqlalchemy.org/"><img src="https://img.shields.io/badge/SQLAlchemy-D71F00.svg?style=for-the-badge&logo=SQLAlchemy&logoColor=white"></a>

<a href="https://render.com/"><img src="https://img.shields.io/badge/Render-000000.svg?style=for-the-badge&logo=Render&logoColor=white"></a>

<a id ="how-to-use"></a>
## ♦️ How to Use
As a read-only API, the only HTTP methods you can use are *GET* requests, in order to obtain a json as a response. For that, all you need to do is simply **write down one of the API's endpoints** in your browser/tool and you will get your desired json file. 

You can either specify which persona you want to check or simply get a list of all the personas. 

Here's an example of the API being used. Note that you need to type the persona's name in **all lowercase**, with **dashes (-) instead of spaces**.

``/personas/jack-frost/``
```json
{
  "id": 16,
  "name": "Jack Frost",
  "arcana": "Magician",
  "level": 8,
  "description": "A winter fairy of European descent. He leaves ice patterns on windows and nips people's noses. Though normally an innocent creature, he will freeze his victims to death if provoked.",
  "image": "https://megatenwiki.com/images/3/3a/P5X_Jack_Frost_Artwork.png",
  "strength": 5,
  "magic": 9,
  "endurance": 8,
  "agility": 6,
  "luck": 4,
  "weak": [
    "Fire"
  ],
  "resists": [],
  "reflects": [],
  "absorbs": [],
  "nullifies": [
    "Ice"
  ],
  "dlc": 0,
  "query": "jack-frost"
}
```

Below, a brief explanation of what each element in the json means: 
- <u>**id:**</u> The persona's ID in the database.
- <u>**name:**</u> The persona's name in English.
- <u>**arcana:**</u> Corresponding arcana.
- <u>**level:**</u> Starting level.
- <u>**description:**</u> In-game description.
- <u>**image:**</u> Transparent image, usually from most recent games.
- <u>**strength, magic, endurance, agility, luck:**</u> Base stats (lowest level).
- <u>**weak, resists, reflects, absorbs, nullifies:**</u> Type relations, stored in a string array.
- <u>**dlc:**</u> Whether the persona comes from a DLC or not (0 for true, 1 for false).
- <u>**query:**</u> String used for querying the persona in the API.

<a id ="api-endpoints"></a>
## 👁️‍🗨️ API Endpoints
There are two types of request you can use with this API:

### **/personas/**
Will return a list with all of the personas' individual jsons, ordered by ID.<br>

``/personas/``
```json
[
  {
    "id": 1,
    "name": "Orpheus",
    "arcana": "Fool",
    "level": 1,
    "description": "A poet of Greek mythology skilled with the lyre. He tried to retrieve his wife from Hades, but she vanished when he looked upon her before reaching the surface.",
    "image": "https://megatenwiki.com/images/b/b3/P3_Orpheus_Artwork.png",
    "strength": 3,
    ...
    "query": "orpheus"
  },
  {
    "id": 2,
    "name": "Slime",
    "arcana": "Fool",
    "level": 12,
    "description": "A primitive monster with a viscous body. There are various theories as to its origin, but it is still under debate. Said to compulsively collect shiny objects.",
    "image": "https://megatenwiki.com/images/7/70/P5X_Slime_Artwork.png",
    ...
    "query": "slime"
  },
  ...
  ...
  ...
  {
    "id": 213,
    "name": "Metatron",
    "arcana": "Aeon",
    "level": 87,
    "description": "The greatest angel in Judeo-Christian legend. He is known as the Voice of God or the Angel of Contracts. Despite his duty to maintain the world's order, he shows no mercy towards humanity.",
    "image": "https://megatenwiki.com/images/2/26/DeSum_Metatron_Artwork.png",
    ...
    "query": "metatron"
  }
]
```
### **/personas/{persona-name}/**
Returns a specific persona's file.
<br>

``/personas/orpheus/``
```json
{
  "id": 1,
  "name": "Orpheus",
  "arcana": "Fool",
  "level": 1,
  "description": "A poet of Greek mythology skilled with the lyre. He tried to retrieve his wife from Hades, but she vanished when he looked upon her before reaching the surface.",
  "image": "https://megatenwiki.com/images/b/b3/P3_Orpheus_Artwork.png",
  "strength": 3,
  "magic": 1,
  "endurance": 2,
  "agility": 3,
  "luck": 1,
  "weak": [
    "Electric",
    "Dark"
  ],
  "resists": [
    "Fire"
  ],
  "reflects": [],
  "absorbs": [],
  "nullifies": [],
  "dlc": 0,
  "query": "orpheus"
}
```
---
<p align="center">
  <a>
    <img src="https://www.fightersgeneration.com/nz4/char/margaret-p4u2-float.gif" height=300/>
  </a>
</p>
