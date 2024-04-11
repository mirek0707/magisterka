from pymongo import MongoClient

uri = ""
# Create a new client and connect to the server
client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["db"]
pipeline = [
    {
        "$group": {
            "_id": "$isbn",
            "title": {
                "$push": {
                    "$switch": {
                        "branches": [
                            {"case": {"$eq": ["$title", ""]}, "then": "$$REMOVE"},
                            {"case": {"$isArray": "$title"}, "then": "$title"},
                        ],
                        "default": ["$title"],
                    }
                }
            },
            "author": {
                "$push": {
                    "$switch": {
                        "branches": [
                            {"case": {"$eq": ["$author", ""]}, "then": "$$REMOVE"},
                            {"case": {"$isArray": "$author"}, "then": "$author"},
                        ],
                        "default": ["$author"],
                    }
                }
            },
            "pages": {
                "$push": {
                    "$switch": {
                        "branches": [
                            {"case": {"$eq": ["$pages", ""]}, "then": "$$REMOVE"},
                            {"case": {"$isArray": "$pages"}, "then": "$pages"},
                        ],
                        "default": ["$pages"],
                    }
                }
            },
            "publisher": {
                "$push": {
                    "$switch": {
                        "branches": [
                            {"case": {"$eq": ["$publisher", ""]}, "then": "$$REMOVE"},
                            {"case": {"$isArray": "$publisher"}, "then": "$publisher"},
                        ],
                        "default": ["$publisher"],
                    }
                }
            },
            "original_title": {
                "$push": {
                    "$switch": {
                        "branches": [
                            {
                                "case": {"$eq": ["$original_title", ""]},
                                "then": "$$REMOVE",
                            },
                            {
                                "case": {"$isArray": "$original_title"},
                                "then": "$original_title",
                            },
                        ],
                        "default": ["$original_title"],
                    }
                }
            },
            "release_date": {
                "$push": {
                    "$switch": {
                        "branches": [
                            {
                                "case": {"$eq": ["$release_date", ""]},
                                "then": "$$REMOVE",
                            },
                            {
                                "case": {"$isArray": "$release_date"},
                                "then": "$release_date",
                            },
                        ],
                        "default": ["$release_date"],
                    }
                }
            },
            "release_year": {
                "$push": {
                    "$switch": {
                        "branches": [
                            {
                                "case": {"$eq": ["$release_year", ""]},
                                "then": "$$REMOVE",
                            },
                            {
                                "case": {"$isArray": "$release_year"},
                                "then": "$release_year",
                            },
                        ],
                        "default": ["$release_year"],
                    }
                }
            },
            "polish_release_date": {
                "$push": {
                    "$switch": {
                        "branches": [
                            {
                                "case": {"$eq": ["$polish_release_date", ""]},
                                "then": "$$REMOVE",
                            },
                            {
                                "case": {"$isArray": "$polish_release_date"},
                                "then": "$polish_release_date",
                            },
                        ],
                        "default": ["$polish_release_date"],
                    }
                }
            },
            "rating_lc": {
                "$push": {
                    "$switch": {
                        "branches": [
                            {"case": {"$eq": ["$rating_lc", ""]}, "then": "$$REMOVE"},
                            {"case": {"$isArray": "$rating_lc"}, "then": "$rating_lc"},
                        ],
                        "default": ["$rating_lc"],
                    }
                }
            },
            "ratings_lc_number": {
                "$push": {
                    "$switch": {
                        "branches": [
                            {
                                "case": {"$eq": ["$ratings_lc_number", ""]},
                                "then": "$$REMOVE",
                            },
                            {
                                "case": {"$isArray": "$ratings_lc_number"},
                                "then": "$ratings_lc_number",
                            },
                        ],
                        "default": ["$ratings_lc_number"],
                    }
                }
            },
            "rating_tk": {
                "$push": {
                    "$switch": {
                        "branches": [
                            {"case": {"$eq": ["$rating_tk", ""]}, "then": "$$REMOVE"},
                            {"case": {"$isArray": "$rating_tk"}, "then": "$rating_tk"},
                        ],
                        "default": ["$rating_tk"],
                    }
                }
            },
            "ratings_tk_number": {
                "$push": {
                    "$switch": {
                        "branches": [
                            {
                                "case": {"$eq": ["$ratings_tk_number", ""]},
                                "then": "$$REMOVE",
                            },
                            {
                                "case": {"$isArray": "$ratings_tk_number"},
                                "then": "$ratings_tk_number",
                            },
                        ],
                        "default": ["$ratings_tk_number"],
                    }
                }
            },
            "rating_gr": {
                "$push": {
                    "$switch": {
                        "branches": [
                            {"case": {"$eq": ["$rating_gr", ""]}, "then": "$$REMOVE"},
                            {"case": {"$isArray": "$rating_gr"}, "then": "$rating_gr"},
                        ],
                        "default": ["$rating_gr"],
                    }
                }
            },
            "ratings_gr_number": {
                "$push": {
                    "$switch": {
                        "branches": [
                            {
                                "case": {"$eq": ["$ratings_gr_number", ""]},
                                "then": "$$REMOVE",
                            },
                            {
                                "case": {"$isArray": "$ratings_gr_number"},
                                "then": "$ratings_gr_number",
                            },
                        ],
                        "default": ["$ratings_gr_number"],
                    }
                }
            },
            "img_src": {
                "$push": {
                    "$switch": {
                        "branches": [
                            {"case": {"$eq": ["$img_src", ""]}, "then": "$$REMOVE"},
                            {"case": {"$isArray": "$img_src"}, "then": "$img_src"},
                        ],
                        "default": ["$img_src"],
                    }
                }
            },
            "description": {
                "$push": {
                    "$switch": {
                        "branches": [
                            {"case": {"$eq": ["$description", ""]}, "then": "$$REMOVE"},
                            {
                                "case": {"$isArray": "$description"},
                                "then": "$description",
                            },
                        ],
                        "default": ["$description"],
                    }
                }
            },
            "genre": {
                "$push": {
                    "$switch": {
                        "branches": [
                            {"case": {"$eq": ["$genre", ""]}, "then": "$$REMOVE"},
                            {"case": {"$isArray": "$genre"}, "then": "$genre"},
                        ],
                        "default": ["$genre"],
                    }
                }
            },
            "id": {"$first": "$_id"},
            "rating": {
                "$push": {
                    "$switch": {
                        "branches": [
                            {"case": {"$eq": ["$rating", ""]}, "then": "$$REMOVE"},
                            {"case": {"$isArray": "$rating"}, "then": "$rating"},
                        ],
                        "default": ["$rating"],
                    }
                }
            },
            "ratings_number": {
                "$push": {
                    "$switch": {
                        "branches": [
                            {
                                "case": {"$eq": ["$ratings_number", ""]},
                                "then": "$$REMOVE",
                            },
                            {
                                "case": {"$isArray": "$ratings_number"},
                                "then": "$ratings_number",
                            },
                        ],
                        "default": ["$ratings_number"],
                    }
                }
            },
        }
    },
    {
        "$project": {
            "_id": "$_id",
            "title": {
                "$reduce": {
                    "input": "$title",
                    "initialValue": [],
                    "in": {"$setUnion": ["$$value", "$$this"]},
                }
            },
            "author": {
                "$reduce": {
                    "input": "$author",
                    "initialValue": [],
                    "in": {"$setUnion": ["$$value", "$$this"]},
                }
            },
            "pages": {
                "$reduce": {
                    "input": "$pages",
                    "initialValue": [],
                    "in": {"$setUnion": ["$$value", "$$this"]},
                }
            },
            "publisher": {
                "$reduce": {
                    "input": "$publisher",
                    "initialValue": [],
                    "in": {"$setUnion": ["$$value", "$$this"]},
                }
            },
            "original_title": {
                "$reduce": {
                    "input": "$original_title",
                    "initialValue": [],
                    "in": {"$setUnion": ["$$value", "$$this"]},
                }
            },
            "release_date": {
                "$reduce": {
                    "input": "$release_date",
                    "initialValue": [],
                    "in": {"$setUnion": ["$$value", "$$this"]},
                }
            },
            "release_year": {
                "$reduce": {
                    "input": "$release_year",
                    "initialValue": [],
                    "in": {"$setUnion": ["$$value", "$$this"]},
                }
            },
            "polish_release_date": {
                "$reduce": {
                    "input": "$polish_release_date",
                    "initialValue": [],
                    "in": {"$setUnion": ["$$value", "$$this"]},
                }
            },
            "rating_lc": {
                "$reduce": {
                    "input": "$rating_lc",
                    "initialValue": [],
                    "in": {"$setUnion": ["$$value", "$$this"]},
                }
            },
            "ratings_lc_number": {
                "$reduce": {
                    "input": "$ratings_lc_number",
                    "initialValue": [],
                    "in": {"$setUnion": ["$$value", "$$this"]},
                }
            },
            "rating_tk": {
                "$reduce": {
                    "input": "$rating_tk",
                    "initialValue": [],
                    "in": {"$setUnion": ["$$value", "$$this"]},
                }
            },
            "ratings_tk_number": {
                "$reduce": {
                    "input": "$ratings_tk_number",
                    "initialValue": [],
                    "in": {"$setUnion": ["$$value", "$$this"]},
                }
            },
            "rating_gr": {
                "$reduce": {
                    "input": "$rating_gr",
                    "initialValue": [],
                    "in": {"$setUnion": ["$$value", "$$this"]},
                }
            },
            "ratings_gr_number": {
                "$reduce": {
                    "input": "$ratings_gr_number",
                    "initialValue": [],
                    "in": {"$setUnion": ["$$value", "$$this"]},
                }
            },
            "img_src": {
                "$reduce": {
                    "input": "$img_src",
                    "initialValue": [],
                    "in": {"$setUnion": ["$$value", "$$this"]},
                }
            },
            "description": {
                "$reduce": {
                    "input": "$description",
                    "initialValue": [],
                    "in": {"$setUnion": ["$$value", "$$this"]},
                }
            },
            "genre": {
                "$reduce": {
                    "input": "$genre",
                    "initialValue": [],
                    "in": {"$setUnion": ["$$value", "$$this"]},
                }
            },
            "id": "$id",
            "rating": {
                "$reduce": {
                    "input": "$rating",
                    "initialValue": [],
                    "in": {"$setUnion": ["$$value", "$$this"]},
                }
            },
            "ratings_number": {
                "$reduce": {
                    "input": "$ratings_number",
                    "initialValue": [],
                    "in": {"$setUnion": ["$$value", "$$this"]},
                }
            },
        }
    },
    {
        "$addFields": {
            "_id": "$_id",
            "title": {
                "$filter": {
                    "input": "$title",
                    "as": "d",
                    "cond": {"$ne": ["$$d", None]},
                }
            },
            "author": {
                "$filter": {
                    "input": "$author",
                    "as": "d",
                    "cond": {"$ne": ["$$d", None]},
                }
            },
            "pages": {
                "$filter": {
                    "input": "$pages",
                    "as": "d",
                    "cond": {"$ne": ["$$d", None]},
                }
            },
            "publisher": {
                "$filter": {
                    "input": "$publisher",
                    "as": "d",
                    "cond": {"$ne": ["$$d", None]},
                }
            },
            "original_title": {
                "$filter": {
                    "input": "$original_title",
                    "as": "d",
                    "cond": {"$ne": ["$$d", None]},
                }
            },
            "release_date": {
                "$filter": {
                    "input": "$release_date",
                    "as": "d",
                    "cond": {"$ne": ["$$d", None]},
                }
            },
            "release_year": {
                "$filter": {
                    "input": "$release_year",
                    "as": "d",
                    "cond": {"$ne": ["$$d", None]},
                }
            },
            "polish_release_date": {
                "$filter": {
                    "input": "$polish_release_date",
                    "as": "d",
                    "cond": {"$ne": ["$$d", None]},
                }
            },
            "rating_lc": {
                "$filter": {
                    "input": "$rating_lc",
                    "as": "d",
                    "cond": {"$ne": ["$$d", None]},
                }
            },
            "ratings_lc_number": {
                "$filter": {
                    "input": "$ratings_lc_number",
                    "as": "d",
                    "cond": {"$ne": ["$$d", None]},
                }
            },
            "rating_tk": {
                "$filter": {
                    "input": "$rating_tk",
                    "as": "d",
                    "cond": {"$ne": ["$$d", None]},
                }
            },
            "ratings_tk_number": {
                "$filter": {
                    "input": "$ratings_tk_number",
                    "as": "d",
                    "cond": {"$ne": ["$$d", None]},
                }
            },
            "rating_gr": {
                "$filter": {
                    "input": "$rating_gr",
                    "as": "d",
                    "cond": {"$ne": ["$$d", None]},
                }
            },
            "ratings_gr_number": {
                "$filter": {
                    "input": "$ratings_gr_number",
                    "as": "d",
                    "cond": {"$ne": ["$$d", None]},
                }
            },
            "img_src": {
                "$filter": {
                    "input": "$img_src",
                    "as": "d",
                    "cond": {"$ne": ["$$d", None]},
                }
            },
            "description": {
                "$filter": {
                    "input": "$description",
                    "as": "d",
                    "cond": {"$ne": ["$$d", None]},
                }
            },
            "genre": {
                "$filter": {
                    "input": "$genre",
                    "as": "d",
                    "cond": {"$ne": ["$$d", None]},
                }
            },
            "id": "$id",
            "rating": {
                "$filter": {
                    "input": "$rating",
                    "as": "d",
                    "cond": {"$ne": ["$$d", None]},
                }
            },
            "ratings_number": {
                "$filter": {
                    "input": "$ratings_number",
                    "as": "d",
                    "cond": {"$ne": ["$$d", None]},
                }
            },
        }
    },
    {
        "$replaceRoot": {
            "newRoot": {
                "_id": "$id",
                "title": "$title",
                "author": "$author",
                "isbn": "$_id",
                "pages": "$pages",
                "publisher": "$publisher",
                "original_title": "$original_title",
                "release_date": "$release_date",
                "release_year": "$release_year",
                "polish_release_date": "$polish_release_date",
                "rating_lc": {
                    "$switch": {
                        "branches": [
                            {
                                "case": {"$eq": [{"$size": "$rating_lc"}, 1]},
                                "then": {"$arrayElemAt": ["$rating_lc", 0]},
                            },
                            {
                                "case": {"$eq": [{"$size": "$rating_lc"}, 0]},
                                "then": None,
                            },
                        ],
                        "default": "$rating_lc",
                    }
                },
                "ratings_lc_number": {
                    "$switch": {
                        "branches": [
                            {
                                "case": {"$eq": [{"$size": "$ratings_lc_number"}, 1]},
                                "then": {"$arrayElemAt": ["$ratings_lc_number", 0]},
                            },
                            {
                                "case": {"$eq": [{"$size": "$ratings_lc_number"}, 0]},
                                "then": None,
                            },
                        ],
                        "default": "$ratings_lc_number",
                    }
                },
                "rating_tk": {
                    "$switch": {
                        "branches": [
                            {
                                "case": {"$eq": [{"$size": "$rating_tk"}, 1]},
                                "then": {"$arrayElemAt": ["$rating_tk", 0]},
                            },
                            {
                                "case": {"$eq": [{"$size": "$rating_tk"}, 0]},
                                "then": None,
                            },
                        ],
                        "default": "$rating_tk",
                    }
                },
                "ratings_tk_number": {
                    "$switch": {
                        "branches": [
                            {
                                "case": {"$eq": [{"$size": "$ratings_tk_number"}, 1]},
                                "then": {"$arrayElemAt": ["$ratings_tk_number", 0]},
                            },
                            {
                                "case": {"$eq": [{"$size": "$ratings_tk_number"}, 0]},
                                "then": None,
                            },
                        ],
                        "default": "$ratings_tk_number",
                    }
                },
                "rating_gr": {
                    "$switch": {
                        "branches": [
                            {
                                "case": {"$eq": [{"$size": "$rating_gr"}, 1]},
                                "then": {"$arrayElemAt": ["$rating_gr", 0]},
                            },
                            {
                                "case": {"$eq": [{"$size": "$rating_gr"}, 0]},
                                "then": None,
                            },
                        ],
                        "default": "$rating_gr",
                    }
                },
                "ratings_gr_number": {
                    "$switch": {
                        "branches": [
                            {
                                "case": {"$eq": [{"$size": "$ratings_gr_number"}, 1]},
                                "then": {"$arrayElemAt": ["$ratings_gr_number", 0]},
                            },
                            {
                                "case": {"$eq": [{"$size": "$ratings_gr_number"}, 0]},
                                "then": None,
                            },
                        ],
                        "default": "$ratings_gr_number",
                    }
                },
                "img_src": "$img_src",
                "description": {
                    "$switch": {
                        "branches": [
                            {
                                "case": {"$eq": [{"$size": "$description"}, 1]},
                                "then": {"$arrayElemAt": ["$description", 0]},
                            },
                            {
                                "case": {"$eq": [{"$size": "$description"}, 0]},
                                "then": "",
                            },
                        ],
                        "default": "$description",
                    }
                },
                "genre": {
                    "$switch": {
                        "branches": [
                            {
                                "case": {"$eq": [{"$size": "$genre"}, 1]},
                                "then": {"$arrayElemAt": ["$genre", 0]},
                            },
                            {"case": {"$eq": [{"$size": "$genre"}, 0]}, "then": ""},
                        ],
                        "default": "$genre",
                    }
                },
                "rating": {
                    "$switch": {
                        "branches": [
                            {
                                "case": {"$eq": [{"$size": "$rating"}, 1]},
                                "then": {"$arrayElemAt": ["$rating", 0]},
                            },
                            {"case": {"$eq": [{"$size": "$rating"}, 0]}, "then": None},
                        ],
                        "default": "$rating",
                    }
                },
                "ratings_number": {
                    "$switch": {
                        "branches": [
                            {
                                "case": {"$eq": [{"$size": "$ratings_number"}, 1]},
                                "then": {"$arrayElemAt": ["$ratings_number", 0]},
                            },
                            {
                                "case": {"$eq": [{"$size": "$ratings_number"}, 0]},
                                "then": None,
                            },
                        ],
                        "default": "$ratings_number",
                    }
                },
            }
        }
    },
    {"$out": "books2"},
]
result = db["books"].aggregate(pipeline, allowDiskUse=True)
