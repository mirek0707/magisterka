from pymongo import MongoClient
collection_name = "test"
uri = ""
# Create a new client and connect to the server
client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['books']
result = client['books']['test'].aggregate([
    {
        '$group': {
            '_id': '$isbn', 
            'title': {
                '$addToSet': {
                    '$cond': {
                        'if': {
                            '$eq': [
                                '$title', ''
                            ]
                        }, 
                        'then': '$$REMOVE', 
                        'else': '$title'
                    }
                }
            }, 
            'author': {
                '$addToSet': {
                    '$cond': {
                        'if': {
                            '$eq': [
                                '$author', ''
                            ]
                        }, 
                        'then': '$$REMOVE', 
                        'else': '$author'
                    }
                }
            }, 
            'pages': {
                '$addToSet': {
                    '$cond': {
                        'if': {
                            '$eq': [
                                '$pages', ''
                            ]
                        }, 
                        'then': '$$REMOVE', 
                        'else': '$pages'
                    }
                }
            }, 
            'publisher': {
                '$addToSet': {
                    '$cond': {
                        'if': {
                            '$eq': [
                                '$publisher', ''
                            ]
                        }, 
                        'then': '$$REMOVE', 
                        'else': '$publisher'
                    }
                }
            }, 
            'original_title': {
                '$addToSet': {
                    '$cond': {
                        'if': {
                            '$eq': [
                                '$original_title', ''
                            ]
                        }, 
                        'then': '$$REMOVE', 
                        'else': '$original_title'
                    }
                }
            }, 
            'release_date': {
                '$addToSet': {
                    '$cond': {
                        'if': {
                            '$eq': [
                                '$release_date', ''
                            ]
                        }, 
                        'then': '$$REMOVE', 
                        'else': '$release_date'
                    }
                }
            }, 
            'release_year': {
                '$addToSet': {
                    '$cond': {
                        'if': {
                            '$eq': [
                                '$release_year', ''
                            ]
                        }, 
                        'then': '$$REMOVE', 
                        'else': '$release_year'
                    }
                }
            }, 
            'polish_release_date': {
                '$addToSet': {
                    '$cond': {
                        'if': {
                            '$eq': [
                                '$polish_release_date', ''
                            ]
                        }, 
                        'then': '$$REMOVE', 
                        'else': '$polish_release_date'
                    }
                }
            }, 
            'rating_lc': {
                '$addToSet': {
                    '$cond': {
                        'if': {
                            '$eq': [
                                '$rating_lc', ''
                            ]
                        }, 
                        'then': '$$REMOVE', 
                        'else': '$rating_lc'
                    }
                }
            }, 
            'ratings_lc_number': {
                '$addToSet': {
                    '$cond': {
                        'if': {
                            '$eq': [
                                '$ratings_lc_number', ''
                            ]
                        }, 
                        'then': '$$REMOVE', 
                        'else': '$ratings_lc_number'
                    }
                }
            }, 
            'rating_tk': {
                '$addToSet': {
                    '$cond': {
                        'if': {
                            '$eq': [
                                '$rating_tk', ''
                            ]
                        }, 
                        'then': '$$REMOVE', 
                        'else': '$rating_tk'
                    }
                }
            }, 
            'ratings_tk_number': {
                '$addToSet': {
                    '$cond': {
                        'if': {
                            '$eq': [
                                '$ratings_tk_number', ''
                            ]
                        }, 
                        'then': '$$REMOVE', 
                        'else': '$ratings_tk_number'
                    }
                }
            }, 
            'description': {
                '$addToSet': {
                    '$cond': {
                        'if': {
                            '$eq': [
                                '$description', ''
                            ]
                        }, 
                        'then': '$$REMOVE', 
                        'else': '$description'
                    }
                }
            }, 
            'id': {
                '$first': '$_id'
            }
        }
    }, {
        '$replaceRoot': {
            'newRoot': {
                '_id': '$id', 
                'title': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$title'
                                        }, 1
                                    ]
                                }, 
                                'then': {
                                    '$arrayElemAt': [
                                        '$title', 0
                                    ]
                                }
                            }, {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$title'
                                        }, 0
                                    ]
                                }, 
                                'then': ''
                            }
                        ], 
                        'default': '$title'
                    }
                }, 
                'author': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$author'
                                        }, 1
                                    ]
                                }, 
                                'then': {
                                    '$arrayElemAt': [
                                        '$author', 0
                                    ]
                                }
                            }, {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$author'
                                        }, 0
                                    ]
                                }, 
                                'then': ''
                            }
                        ], 
                        'default': '$author'
                    }
                }, 
                'isbn': '$_id', 
                'pages': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$pages'
                                        }, 1
                                    ]
                                }, 
                                'then': {
                                    '$arrayElemAt': [
                                        '$pages', 0
                                    ]
                                }
                            }, {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$pages'
                                        }, 0
                                    ]
                                }, 
                                'then': ''
                            }
                        ], 
                        'default': '$pages'
                    }
                }, 
                'publisher': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$publisher'
                                        }, 1
                                    ]
                                }, 
                                'then': {
                                    '$arrayElemAt': [
                                        '$publisher', 0
                                    ]
                                }
                            }, {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$publisher'
                                        }, 0
                                    ]
                                }, 
                                'then': ''
                            }
                        ], 
                        'default': '$publisher'
                    }
                }, 
                'original_title': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$original_title'
                                        }, 1
                                    ]
                                }, 
                                'then': {
                                    '$arrayElemAt': [
                                        '$original_title', 0
                                    ]
                                }
                            }, {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$original_title'
                                        }, 0
                                    ]
                                }, 
                                'then': ''
                            }
                        ], 
                        'default': '$original_title'
                    }
                }, 
                'release_date': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$release_date'
                                        }, 1
                                    ]
                                }, 
                                'then': {
                                    '$arrayElemAt': [
                                        '$release_date', 0
                                    ]
                                }
                            }, {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$release_date'
                                        }, 0
                                    ]
                                }, 
                                'then': ''
                            }
                        ], 
                        'default': '$release_date'
                    }
                }, 
                'release_year': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$release_year'
                                        }, 1
                                    ]
                                }, 
                                'then': {
                                    '$arrayElemAt': [
                                        '$release_year', 0
                                    ]
                                }
                            }, {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$release_year'
                                        }, 0
                                    ]
                                }, 
                                'then': ''
                            }
                        ], 
                        'default': '$release_year'
                    }
                }, 
                'polish_release_date': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$polish_release_date'
                                        }, 1
                                    ]
                                }, 
                                'then': {
                                    '$arrayElemAt': [
                                        '$polish_release_date', 0
                                    ]
                                }
                            }, {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$polish_release_date'
                                        }, 0
                                    ]
                                }, 
                                'then': ''
                            }
                        ], 
                        'default': '$polish_release_date'
                    }
                }, 
                'rating_lc': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$rating_lc'
                                        }, 1
                                    ]
                                }, 
                                'then': {
                                    '$arrayElemAt': [
                                        '$rating_lc', 0
                                    ]
                                }
                            }, {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$rating_lc'
                                        }, 0
                                    ]
                                }, 
                                'then': ''
                            }
                        ], 
                        'default': '$rating_lc'
                    }
                }, 
                'ratings_lc_number': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$ratings_lc_number'
                                        }, 1
                                    ]
                                }, 
                                'then': {
                                    '$arrayElemAt': [
                                        '$ratings_lc_number', 0
                                    ]
                                }
                            }, {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$ratings_lc_number'
                                        }, 0
                                    ]
                                }, 
                                'then': ''
                            }
                        ], 
                        'default': '$ratings_lc_number'
                    }
                }, 
                'rating_tk': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$rating_tk'
                                        }, 1
                                    ]
                                }, 
                                'then': {
                                    '$arrayElemAt': [
                                        '$rating_tk', 0
                                    ]
                                }
                            }, {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$rating_tk'
                                        }, 0
                                    ]
                                }, 
                                'then': ''
                            }
                        ], 
                        'default': '$rating_tk'
                    }
                }, 
                'ratings_tk_number': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$ratings_tk_number'
                                        }, 1
                                    ]
                                }, 
                                'then': {
                                    '$arrayElemAt': [
                                        '$ratings_tk_number', 0
                                    ]
                                }
                            }, {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$ratings_tk_number'
                                        }, 0
                                    ]
                                }, 
                                'then': ''
                            }
                        ], 
                        'default': '$ratings_tk_number'
                    }
                }, 
                'description': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$description'
                                        }, 1
                                    ]
                                }, 
                                'then': {
                                    '$arrayElemAt': [
                                        '$description', 0
                                    ]
                                }
                            }, {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$description'
                                        }, 0
                                    ]
                                }, 
                                'then': ''
                            }
                        ], 
                        'default': '$description'
                    }
                }
            }
        }
    }, {
        '$out': 'test'
    }
])

