from pymongo import MongoClient
uri = ""
# Create a new client and connect to the server
client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['db']
pipeline = [
    {
        '$addFields': {
            'id': '$id', 
            'title': '$title', 
            'author': '$author', 
            'pages': {
                '$convert': {
                    'input': '$pages', 
                    'to': 'int'
                }
            }, 
            'isbn': '$isbn', 
            'publisher': '$publisher', 
            'original_title': '$original_title', 
            'release_date': {
                '$dateFromString': {
                    'dateString': '$release_date', 
                    'timezone': 'Europe/Samara'
                }
            }, 
            'release_year': {
                '$convert': {
                    'input': '$release_year', 
                    'to': 'int'
                }
            }, 
            'polish_release_date': {
                '$dateFromString': {
                    'dateString': '$polish_release_date', 
                    'timezone': 'Europe/Samara'
                }
            }, 
            'rating_lc': {
                '$convert': {
                    'input': {
                        '$replaceAll': {
                            'input': '$rating_lc', 
                            'find': ',', 
                            'replacement': '.'
                        }
                    }, 
                    'to': 'double'
                }
            }, 
            'ratings_lc_number': {
                '$convert': {
                    'input': '$ratings_lc_number', 
                    'to': 'int'
                }
            }, 
            'rating_tk': {
                '$convert': {
                    'input': {
                        '$replaceAll': {
                            'input': '$rating_tk', 
                            'find': ',', 
                            'replacement': '.'
                        }
                    }, 
                    'to': 'double'
                }
            }, 
            'ratings_tk_number': {
                '$convert': {
                    'input': '$ratings_tk_number', 
                    'to': 'int'
                }
            }, 
            'rating_gr': {
                '$convert': {
                    'input': {
                        '$replaceAll': {
                            'input': '$rating_gr', 
                            'find': ',', 
                            'replacement': '.'
                        }
                    }, 
                    'to': 'double'
                }
            }, 
            'ratings_gr_number': {
                '$convert': {
                    'input': '$ratings_gr_number', 
                    'to': 'int'
                }
            }, 
            'img_source': '$img_source', 
            'description': '$description'
        }
    }, {
        '$group': {
            '_id': '$isbn', 
            'title': {
                '$push': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        '$title', ''
                                    ]
                                }, 
                                'then': '$$REMOVE'
                            }, {
                                'case': {
                                    '$isArray': '$title'
                                }, 
                                'then': '$title'
                            }
                        ], 
                        'default': [
                            '$title'
                        ]
                    }
                }
            }, 
            'author': {
                '$push': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        '$author', ''
                                    ]
                                }, 
                                'then': '$$REMOVE'
                            }, {
                                'case': {
                                    '$isArray': '$author'
                                }, 
                                'then': '$author'
                            }
                        ], 
                        'default': [
                            '$author'
                        ]
                    }
                }
            }, 
            'pages': {
                '$push': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        '$pages', ''
                                    ]
                                }, 
                                'then': '$$REMOVE'
                            }, {
                                'case': {
                                    '$isArray': '$pages'
                                }, 
                                'then': '$pages'
                            }
                        ], 
                        'default': [
                            '$pages'
                        ]
                    }
                }
            }, 
            'publisher': {
                '$push': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        '$publisher', ''
                                    ]
                                }, 
                                'then': '$$REMOVE'
                            }, {
                                'case': {
                                    '$isArray': '$publisher'
                                }, 
                                'then': '$publisher'
                            }
                        ], 
                        'default': [
                            '$publisher'
                        ]
                    }
                }
            }, 
            'original_title': {
                '$push': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        '$original_title', ''
                                    ]
                                }, 
                                'then': '$$REMOVE'
                            }, {
                                'case': {
                                    '$isArray': '$original_title'
                                }, 
                                'then': '$original_title'
                            }
                        ], 
                        'default': [
                            '$original_title'
                        ]
                    }
                }
            }, 
            'release_date': {
                '$push': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        '$release_date', ''
                                    ]
                                }, 
                                'then': '$$REMOVE'
                            }, {
                                'case': {
                                    '$isArray': '$release_date'
                                }, 
                                'then': '$release_date'
                            }
                        ], 
                        'default': [
                            '$release_date'
                        ]
                    }
                }
            }, 
            'release_year': {
                '$push': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        '$release_year', ''
                                    ]
                                }, 
                                'then': '$$REMOVE'
                            }, {
                                'case': {
                                    '$isArray': '$release_year'
                                }, 
                                'then': '$release_year'
                            }
                        ], 
                        'default': [
                            '$release_year'
                        ]
                    }
                }
            }, 
            'polish_release_date': {
                '$push': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        '$polish_release_date', ''
                                    ]
                                }, 
                                'then': '$$REMOVE'
                            }, {
                                'case': {
                                    '$isArray': '$polish_release_date'
                                }, 
                                'then': '$polish_release_date'
                            }
                        ], 
                        'default': [
                            '$polish_release_date'
                        ]
                    }
                }
            }, 
            'rating_lc': {
                '$push': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        '$rating_lc', ''
                                    ]
                                }, 
                                'then': '$$REMOVE'
                            }, {
                                'case': {
                                    '$isArray': '$rating_lc'
                                }, 
                                'then': '$rating_lc'
                            }
                        ], 
                        'default': [
                            '$rating_lc'
                        ]
                    }
                }
            }, 
            'ratings_lc_number': {
                '$push': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        '$ratings_lc_number', ''
                                    ]
                                }, 
                                'then': '$$REMOVE'
                            }, {
                                'case': {
                                    '$isArray': '$ratings_lc_number'
                                }, 
                                'then': '$ratings_lc_number'
                            }
                        ], 
                        'default': [
                            '$ratings_lc_number'
                        ]
                    }
                }
            }, 
            'rating_tk': {
                '$push': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        '$rating_tk', ''
                                    ]
                                }, 
                                'then': '$$REMOVE'
                            }, {
                                'case': {
                                    '$isArray': '$rating_tk'
                                }, 
                                'then': '$rating_tk'
                            }
                        ], 
                        'default': [
                            '$rating_tk'
                        ]
                    }
                }
            }, 
            'ratings_tk_number': {
                '$push': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        '$ratings_tk_number', ''
                                    ]
                                }, 
                                'then': '$$REMOVE'
                            }, {
                                'case': {
                                    '$isArray': '$ratings_tk_number'
                                }, 
                                'then': '$ratings_tk_number'
                            }
                        ], 
                        'default': [
                            '$ratings_tk_number'
                        ]
                    }
                }
            }, 
            'rating_gr': {
                '$push': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        '$rating_gr', ''
                                    ]
                                }, 
                                'then': '$$REMOVE'
                            }, {
                                'case': {
                                    '$isArray': '$rating_gr'
                                }, 
                                'then': '$rating_gr'
                            }
                        ], 
                        'default': [
                            '$rating_gr'
                        ]
                    }
                }
            }, 
            'ratings_gr_number': {
                '$push': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        '$ratings_gr_number', ''
                                    ]
                                }, 
                                'then': '$$REMOVE'
                            }, {
                                'case': {
                                    '$isArray': '$ratings_gr_number'
                                }, 
                                'then': '$ratings_gr_number'
                            }
                        ], 
                        'default': [
                            '$ratings_gr_number'
                        ]
                    }
                }
            }, 
            'img_src': {
                '$push': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        '$img_src', ''
                                    ]
                                }, 
                                'then': '$$REMOVE'
                            }, {
                                'case': {
                                    '$isArray': '$img_src'
                                }, 
                                'then': '$img_src'
                            }
                        ], 
                        'default': [
                            '$img_src'
                        ]
                    }
                }
            }, 
            'description': {
                '$push': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        '$description', ''
                                    ]
                                }, 
                                'then': '$$REMOVE'
                            }, {
                                'case': {
                                    '$isArray': '$description'
                                }, 
                                'then': '$description'
                            }
                        ], 
                        'default': [
                            '$description'
                        ]
                    }
                }
            }, 
            'id': {
                '$first': '$_id'
            }
        }
    }, {
        '$project': {
            '_id': '$_id', 
            'title': {
                '$reduce': {
                    'input': '$title', 
                    'initialValue': [], 
                    'in': {
                        '$setUnion': [
                            '$$value', '$$this'
                        ]
                    }
                }
            }, 
            'author': {
                '$reduce': {
                    'input': '$author', 
                    'initialValue': [], 
                    'in': {
                        '$setUnion': [
                            '$$value', '$$this'
                        ]
                    }
                }
            }, 
            'pages': {
                '$reduce': {
                    'input': '$pages', 
                    'initialValue': [], 
                    'in': {
                        '$setUnion': [
                            '$$value', '$$this'
                        ]
                    }
                }
            }, 
            'publisher': {
                '$reduce': {
                    'input': '$publisher', 
                    'initialValue': [], 
                    'in': {
                        '$setUnion': [
                            '$$value', '$$this'
                        ]
                    }
                }
            }, 
            'original_title': {
                '$reduce': {
                    'input': '$original_title', 
                    'initialValue': [], 
                    'in': {
                        '$setUnion': [
                            '$$value', '$$this'
                        ]
                    }
                }
            }, 
            'release_date': {
                '$reduce': {
                    'input': '$release_date', 
                    'initialValue': [], 
                    'in': {
                        '$setUnion': [
                            '$$value', '$$this'
                        ]
                    }
                }
            }, 
            'release_year': {
                '$reduce': {
                    'input': '$release_year', 
                    'initialValue': [], 
                    'in': {
                        '$setUnion': [
                            '$$value', '$$this'
                        ]
                    }
                }
            }, 
            'polish_release_date': {
                '$reduce': {
                    'input': '$polish_release_date', 
                    'initialValue': [], 
                    'in': {
                        '$setUnion': [
                            '$$value', '$$this'
                        ]
                    }
                }
            }, 
            'rating_lc': {
                '$reduce': {
                    'input': '$rating_lc', 
                    'initialValue': [], 
                    'in': {
                        '$setUnion': [
                            '$$value', '$$this'
                        ]
                    }
                }
            }, 
            'ratings_lc_number': {
                '$reduce': {
                    'input': '$ratings_lc_number', 
                    'initialValue': [], 
                    'in': {
                        '$setUnion': [
                            '$$value', '$$this'
                        ]
                    }
                }
            }, 
            'rating_tk': {
                '$reduce': {
                    'input': '$rating_tk', 
                    'initialValue': [], 
                    'in': {
                        '$setUnion': [
                            '$$value', '$$this'
                        ]
                    }
                }
            }, 
            'ratings_tk_number': {
                '$reduce': {
                    'input': '$ratings_tk_number', 
                    'initialValue': [], 
                    'in': {
                        '$setUnion': [
                            '$$value', '$$this'
                        ]
                    }
                }
            }, 
            'rating_gr': {
                '$reduce': {
                    'input': '$rating_gr', 
                    'initialValue': [], 
                    'in': {
                        '$setUnion': [
                            '$$value', '$$this'
                        ]
                    }
                }
            }, 
            'ratings_gr_number': {
                '$reduce': {
                    'input': '$ratings_gr_number', 
                    'initialValue': [], 
                    'in': {
                        '$setUnion': [
                            '$$value', '$$this'
                        ]
                    }
                }
            }, 
            'img_src': {
                '$reduce': {
                    'input': '$img_src', 
                    'initialValue': [], 
                    'in': {
                        '$setUnion': [
                            '$$value', '$$this'
                        ]
                    }
                }
            }, 
            'description': {
                '$reduce': {
                    'input': '$description', 
                    'initialValue': [], 
                    'in': {
                        '$setUnion': [
                            '$$value', '$$this'
                        ]
                    }
                }
            }, 
            'id': '$id'
        }
    }, {
        '$addFields': {
            '_id': '$_id', 
            'title': {
                '$filter': {
                    'input': '$title', 
                    'as': 'd', 
                    'cond': {
                        '$ne': [
                            '$$d', None
                        ]
                    }
                }
            }, 
            'author': {
                '$filter': {
                    'input': '$author', 
                    'as': 'd', 
                    'cond': {
                        '$ne': [
                            '$$d', None
                        ]
                    }
                }
            }, 
            'pages': {
                '$filter': {
                    'input': '$pages', 
                    'as': 'd', 
                    'cond': {
                        '$ne': [
                            '$$d', None
                        ]
                    }
                }
            }, 
            'publisher': {
                '$filter': {
                    'input': '$publisher', 
                    'as': 'd', 
                    'cond': {
                        '$ne': [
                            '$$d', None
                        ]
                    }
                }
            }, 
            'original_title': {
                '$filter': {
                    'input': '$original_title', 
                    'as': 'd', 
                    'cond': {
                        '$ne': [
                            '$$d', None
                        ]
                    }
                }
            }, 
            'release_date': {
                '$filter': {
                    'input': '$release_date', 
                    'as': 'd', 
                    'cond': {
                        '$ne': [
                            '$$d', None
                        ]
                    }
                }
            }, 
            'release_year': {
                '$filter': {
                    'input': '$release_year', 
                    'as': 'd', 
                    'cond': {
                        '$ne': [
                            '$$d', None
                        ]
                    }
                }
            }, 
            'polish_release_date': {
                '$filter': {
                    'input': '$polish_release_date', 
                    'as': 'd', 
                    'cond': {
                        '$ne': [
                            '$$d', None
                        ]
                    }
                }
            }, 
            'rating_lc': {
                '$filter': {
                    'input': '$rating_lc', 
                    'as': 'd', 
                    'cond': {
                        '$ne': [
                            '$$d', None
                        ]
                    }
                }
            }, 
            'ratings_lc_number': {
                '$filter': {
                    'input': '$ratings_lc_number', 
                    'as': 'd', 
                    'cond': {
                        '$ne': [
                            '$$d', None
                        ]
                    }
                }
            }, 
            'rating_tk': {
                '$filter': {
                    'input': '$rating_tk', 
                    'as': 'd', 
                    'cond': {
                        '$ne': [
                            '$$d', None
                        ]
                    }
                }
            }, 
            'ratings_tk_number': {
                '$filter': {
                    'input': '$ratings_tk_number', 
                    'as': 'd', 
                    'cond': {
                        '$ne': [
                            '$$d', None
                        ]
                    }
                }
            }, 
            'rating_gr': {
                '$filter': {
                    'input': '$rating_gr', 
                    'as': 'd', 
                    'cond': {
                        '$ne': [
                            '$$d', None
                        ]
                    }
                }
            }, 
            'ratings_gr_number': {
                '$filter': {
                    'input': '$ratings_gr_number', 
                    'as': 'd', 
                    'cond': {
                        '$ne': [
                            '$$d', None
                        ]
                    }
                }
            }, 
            'img_src': {
                '$filter': {
                    'input': '$img_src', 
                    'as': 'd', 
                    'cond': {
                        '$ne': [
                            '$$d', None
                        ]
                    }
                }
            }, 
            'description': {
                '$filter': {
                    'input': '$description', 
                    'as': 'd', 
                    'cond': {
                        '$ne': [
                            '$$d', None
                        ]
                    }
                }
            }, 
            'id': '$id'
        }
    }, {
        '$redact': {
            '$cond': {
                'if': {
                    '$or': [
                        {
                            '$gt': [
                                {
                                    '$size': '$rating_lc'
                                }, 1
                            ]
                        }, {
                            '$gt': [
                                {
                                    '$size': '$rating_gr'
                                }, 1
                            ]
                        }, {
                            '$gt': [
                                {
                                    '$size': '$rating_tk'
                                }, 1
                            ]
                        }, {
                            '$gt': [
                                {
                                    '$size': '$ratings_lc_number'
                                }, 1
                            ]
                        }, {
                            '$gt': [
                                {
                                    '$size': '$ratings_gr_number'
                                }, 1
                            ]
                        }, {
                            '$gt': [
                                {
                                    '$size': '$ratings_tk_number'
                                }, 1
                            ]
                        }, {
                            '$gt': [
                                {
                                    '$size': '$title'
                                }, 4
                            ]
                        }, {
                            '$eq': [
                                {
                                    '$size': '$title'
                                }, 0
                            ]
                        }, {
                            '$gt': [
                                {
                                    '$size': '$pages'
                                }, 4
                            ]
                        }, {
                            '$gt': [
                                {
                                    '$size': '$original_title'
                                }, 4
                            ]
                        }, {
                            '$gt': [
                                {
                                    '$size': '$release_year'
                                }, 4
                            ]
                        }, {
                            '$gt': [
                                {
                                    '$size': '$release_date'
                                }, 4
                            ]
                        }, {
                            '$gt': [
                                {
                                    '$size': '$polish_release_date'
                                }, 4
                            ]
                        }, {
                            '$gt': [
                                {
                                    '$size': '$description'
                                }, 4
                            ]
                        }
                    ]
                }, 
                'then': '$$PRUNE', 
                'else': '$$DESCEND'
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
                'rating_gr': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$rating_gr'
                                        }, 1
                                    ]
                                }, 
                                'then': {
                                    '$arrayElemAt': [
                                        '$rating_gr', 0
                                    ]
                                }
                            }, {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$rating_gr'
                                        }, 0
                                    ]
                                }, 
                                'then': ''
                            }
                        ], 
                        'default': '$rating_gr'
                    }
                }, 
                'ratings_gr_number': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$ratings_gr_number'
                                        }, 1
                                    ]
                                }, 
                                'then': {
                                    '$arrayElemAt': [
                                        '$ratings_gr_number', 0
                                    ]
                                }
                            }, {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$ratings_gr_number'
                                        }, 0
                                    ]
                                }, 
                                'then': ''
                            }
                        ], 
                        'default': '$ratings_gr_number'
                    }
                }, 
                'img_src': {
                    '$switch': {
                        'branches': [
                            {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$img_src'
                                        }, 1
                                    ]
                                }, 
                                'then': {
                                    '$arrayElemAt': [
                                        '$img_src', 0
                                    ]
                                }
                            }, {
                                'case': {
                                    '$eq': [
                                        {
                                            '$size': '$img_src'
                                        }, 0
                                    ]
                                }, 
                                'then': ''
                            }
                        ], 
                        'default': '$img_src'
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
        '$addFields': {
            'ratings_number': {
                '$add': [
                    {
                        '$cond': {
                            'if': {
                                '$ne': [
                                    '$ratings_gr_number', ''
                                ]
                            }, 
                            'then': {
                                '$toInt': '$ratings_gr_number'
                            }, 
                            'else': 0
                        }
                    }, {
                        '$cond': {
                            'if': {
                                '$ne': [
                                    '$ratings_lc_number', ''
                                ]
                            }, 
                            'then': {
                                '$toInt': '$ratings_lc_number'
                            }, 
                            'else': 0
                        }
                    }, {
                        '$cond': {
                            'if': {
                                '$ne': [
                                    '$ratings_tk_number', ''
                                ]
                            }, 
                            'then': {
                                '$toInt': '$ratings_tk_number'
                            }, 
                            'else': 0
                        }
                    }
                ]
            }
        }
    }, {
        '$addFields': {
            'rating': {
                '$divide': [
                    {
                        '$add': [
                            {
                                '$multiply': [
                                    {
                                        '$cond': {
                                            'if': {
                                                '$ne': [
                                                    '$ratings_lc_number', ''
                                                ]
                                            }, 
                                            'then': {
                                                '$toInt': '$ratings_lc_number'
                                            }, 
                                            'else': 0
                                        }
                                    }, {
                                        '$cond': {
                                            'if': {
                                                '$ne': [
                                                    '$rating_lc', ''
                                                ]
                                            }, 
                                            'then': {
                                                '$toDouble': '$rating_lc'
                                            }, 
                                            'else': 0
                                        }
                                    }, 0.5
                                ]
                            }, {
                                '$multiply': [
                                    {
                                        '$cond': {
                                            'if': {
                                                '$ne': [
                                                    '$ratings_tk_number', ''
                                                ]
                                            }, 
                                            'then': {
                                                '$toInt': '$ratings_tk_number'
                                            }, 
                                            'else': 0
                                        }
                                    }, {
                                        '$cond': {
                                            'if': {
                                                '$ne': [
                                                    '$rating_tk', ''
                                                ]
                                            }, 
                                            'then': {
                                                '$toDouble': '$rating_tk'
                                            }, 
                                            'else': 0
                                        }
                                    }
                                ]
                            }, {
                                '$multiply': [
                                    {
                                        '$cond': {
                                            'if': {
                                                '$ne': [
                                                    '$ratings_gr_number', ''
                                                ]
                                            }, 
                                            'then': {
                                                '$toInt': '$ratings_gr_number'
                                            }, 
                                            'else': 0
                                        }
                                    }, {
                                        '$cond': {
                                            'if': {
                                                '$ne': [
                                                    '$rating_gr', ''
                                                ]
                                            }, 
                                            'then': {
                                                '$toDouble': '$rating_gr'
                                            }, 
                                            'else': 0
                                        }
                                    }
                                ]
                            }
                        ]
                    }, {
                        '$cond': {
                            'if': {
                                '$eq': [
                                    '$ratings_number', 0
                                ]
                            }, 
                            'then': 1, 
                            'else': '$ratings_number'
                        }
                    }
                ]
            }
        }
    }, {
        '$out': 'books'
    }
]
result = db['books'].aggregate(pipeline, allowDiskUse=True)

