import json
def toJSON(data, typ=None):
    if typ == 't':
        try:
            print(json.dumps(data, sort_keys=False, indent=4))
        except Exception as e:
            print(e)
    else:
        f = open('./main/d96/checker/param.json', 'w', encoding='utf-8')
        try:
            f.write(json.dumps(data, sort_keys=False, indent=4))
        except Exception as e:
            f.write(e)
        finally:
            f.close()

'''
    * HOW TO USE?
    * Place above function in global scope of your StaticCheck.py and `import json` module in top of file.
    * Want to print to a external file, call toJSON(<your param structure>)
    * Want to print to terminal while running, call toJSON(<your param strcuture>, 't')
    * That's all
'''
'''Example param's file'''
'''
{
    "global": {
        "Program": {
            "parent": "",
            "attribute": {
                "name": {
                    "kind": "<INSTANCE>",
                    "type": "<STRING>",
                    "init": null,
                    "const": false
                },
                "age": {
                    "kind": "<INSTANCE>",
                    "type": "<INT>",
                    "init": "<INT>",
                    "const": true
                }
            },
            "method": {
                "main": {
                    "type": "<VOID>",
                    "kind": "<INSTANCE>",
                    "body": [
                        {
                            "a": {
                                "type": "<INT>",
                                "kind": "<INSTANCE>",
                                "init": null,
                                "const": false
                            },
                            "b": {
                                "type": "<FLOAT>",
                                "kind": "<INSTANCE>",
                                "init": null,
                                "const": false
                            },
                            "c": {
                                "type": "<INT>",
                                "kind": "<INSTANCE>",
                                "init": "<INT>",
                                "const": true
                            }
                        }
                    ],
                    "param": {
                        "a": {
                            "type": "<INT>",
                            "kind": "<INSTANCE>",
                            "init": null,
                            "const": false
                        },
                        "b": {
                            "type": "<FLOAT>",
                            "kind": "<INSTANCE>",
                            "init": null,
                            "const": false
                        }
                    }
                }
            }
        }
    },
    "class": {
        "parent": "",
        "attribute": {
            "name": {
                "kind": "<INSTANCE>",
                "type": "<STRING>",
                "init": null,
                "const": false
            },
            "age": {
                "kind": "<INSTANCE>",
                "type": "<INT>",
                "init": "<INT>",
                "const": true
            }
        },
        "method": {
            "main": {
                "type": "<VOID>",
                "kind": "<INSTANCE>",
                "body": [
                    {
                        "a": {
                            "type": "<INT>",
                            "kind": "<INSTANCE>",
                            "init": null,
                            "const": false
                        },
                        "b": {
                            "type": "<FLOAT>",
                            "kind": "<INSTANCE>",
                            "init": null,
                            "const": false
                        },
                        "c": {
                            "type": "<INT>",
                            "kind": "<INSTANCE>",
                            "init": "<INT>",
                            "const": true
                        }
                    }
                ],
                "param": {
                    "a": {
                        "type": "<INT>",
                        "kind": "<INSTANCE>",
                        "init": null,
                        "const": false
                    },
                    "b": {
                        "type": "<FLOAT>",
                        "kind": "<INSTANCE>",
                        "init": null,
                        "const": false
                    }
                }
            }
        }
    },
    "method": {
        "type": "<VOID>",
        "kind": "<INSTANCE>",
        "body": [
            {
                "a": {
                    "type": "<INT>",
                    "kind": "<INSTANCE>",
                    "init": null,
                    "const": false
                },
                "b": {
                    "type": "<FLOAT>",
                    "kind": "<INSTANCE>",
                    "init": null,
                    "const": false
                },
                "c": {
                    "type": "<INT>",
                    "kind": "<INSTANCE>",
                    "init": "<INT>",
                    "const": true
                }
            }
        ],
        "param": {
            "a": {
                "type": "<INT>",
                "kind": "<INSTANCE>",
                "init": null,
                "const": false
            },
            "b": {
                "type": "<FLOAT>",
                "kind": "<INSTANCE>",
                "init": null,
                "const": false
            }
        }
    },
    "block": [
        {
            "e": {
                "type": "<INT>",
                "kind": "<INSTANCE>",
                "const": false,
                "init": "<INT>"
            }
        },
        {
            "a": {
                "type": "<INT>",
                "kind": "<INSTANCE>",
                "init": null,
                "const": false
            },
            "b": {
                "type": "<FLOAT>",
                "kind": "<INSTANCE>",
                "init": null,
                "const": false
            },
            "c": {
                "type": "<INT>",
                "kind": "<INSTANCE>",
                "init": "<INT>",
                "const": true
            }
        }
    ]
}
'''