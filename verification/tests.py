"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": """2013-01-01-01-00-00;;Name;;http://checkio.org/task
2013-01-01-01-02-00;;name;;http://checkio.org/task2
2013-01-01-01-31-00;;Name;;https://admin.checkio.org
2013-01-01-03-00-00;;Name;;http://www.checkio.org/profile
2013-01-01-03-00-01;;Name;;http://example.com
2013-02-03-04-00-00;;user2;;http://checkio.org/task
2013-01-01-03-11-00;;Name;;http://checkio.org/task""",
            "answer": """name;;example.com;;1;;1
name;;checkio.org;;661;;2
name;;checkio.org;;1861;;3
user2;;checkio.org;;1;;1""",
        },
        {"input": """2013-01-01-01-00-00;;user1;;http://new.checkio.org
2013-01-01-01-10-00;;User2;;http://checkio.org/welcome/user
2013-01-01-01-11-02;;user1;;http://checkio.org/blog/
2013-01-01-01-16-44;;User2;;http://www.checkio.org/news/creators/
2013-01-01-01-37-40;;User2;;http://checkio.org/blog/
2013-01-02-01-00-00;;User2;;http://checkio.org/info/task/1""",
         "answer": """user1;;checkio.org;;663;;2
user2;;checkio.org;;1;;1
user2;;checkio.org;;1661;;3
"""}
            ],
        "Extra":[
    {
        "input": """2013-02-11-10-00-00;;admin;;http://example.org/2
2013-02-11-10-27-43;;admin;;http://example.org/1/3/4
2013-02-11-10-34-07;;admin;;http://example.org/1/3/4
2013-02-11-10-38-11;;admin;;http://example.org
2013-02-11-11-01-51;;admin;;http://example.org/2
2013-02-11-11-19-23;;admin;;http://example.org/1
2013-02-11-11-31-34;;admin;;http://example.org/get
2013-02-11-12-00-33;;admin;;http://example.org/1/3/4
2013-02-11-12-09-48;;admin;;http://example.org/get
2013-02-11-12-10-00;;Simple_User;;http://international.hubspot.com/
2013-02-11-12-11-31;;admin;;http://example.org/2
2013-02-11-12-37-57;;Simple_User;;http://blog.hubspot.com/
2013-02-11-12-57-13;;Simple_User;;http://www.hubspot.com/sitemap
2013-02-11-12-57-20;;Simple_User;;http://www.hubspot.com/sitemap
2013-03-10-01-00-00;;ADMIN;;http://example.com
2013-03-10-01-24-14;;ADMIN;;http://example.com/1/3/4""",

        "answer": """admin;;example.com;;1455;;2
admin;;example.org;;7892;;10
simple_user;;hubspot.com;;2841;;4"""},
    {"input": """2013-04-11-10-00-00;;admin;;http://www.hubspot.com/products/inbound-marketing/
2013-04-11-10-00-59;;admin;;http://www.hubspot.com/products/inbound-marketing/
2013-04-11-10-24-22;;admin;;http://www.hubspot.com/products
2013-04-11-10-45-52;;admin;;http://www.hubspot.com/products
2013-04-11-11-01-35;;admin;;http://www.hubspot.com/products
2013-04-11-11-31-12;;admin;;http://www.hubspot.com/products/inbound-marketing/
2013-04-11-11-39-08;;admin;;http://www.hubspot.com/
2013-04-11-11-41-33;;admin;;http://international.hubspot.com/
2013-04-11-11-47-16;;admin;;http://www.hubspot.com/products
2013-04-11-12-00-23;;User1;;http://www.hubspot.com/internet-marketing-company
2013-04-11-12-10-00;;Simple_user;;http://www.hubspot.com/products/inbound-marketing/
2013-04-11-12-16-08;;User1;;http://blog.hubspot.com/
2013-04-11-12-29-45;;Simple_user;;http://www.hubspot.com/sitemap
2013-04-11-12-35-33;;User1;;http://www.hubspot.com/products/inbound-marketing/
2013-04-11-12-44-58;;Simple_user;;http://blog.hubspot.com/
2013-04-11-12-47-47;;Simple_user;;http://www.hubspot.com/sitemap
2013-04-11-12-49-28;;Simple_user;;http://blog.hubspot.com/
2013-04-11-13-02-22;;User1;;http://blog.hubspot.com/
2013-04-11-13-04-00;;Simple_user;;http://www.hubspot.com/sitemap
2013-04-11-13-20-20;;Simple_user;;http://international.hubspot.com/
2013-04-11-13-31-58;;User1;;http://www.hubspot.com/sitemap
2013-04-11-13-39-56;;User1;;http://www.hubspot.com/
2013-04-11-13-48-47;;User1;;http://www.hubspot.com/internet-marketing-company
2013-04-11-13-49-37;;Simple_user;;http://www.hubspot.com/internet-marketing-company
2013-04-11-13-57-33;;User1;;http://www.hubspot.com/sitemap
2013-04-11-14-03-57;;Simple_user;;http://www.hubspot.com/
2013-04-11-14-11-17;;User1;;http://www.hubspot.com/""",

"answer": """admin;;hubspot.com;;6437;;9
simple_user;;hubspot.com;;6838;;9
user1;;hubspot.com;;7855;;9"""}
]
}
