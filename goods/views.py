from django.shortcuts import render


def catalog(request):
    context = {
        "title": "Home Catalog",
        "goods": [
            {
                "image": "deps/images/goods/set of tea table and three chairs.jpg",
                "name": "Tea table and three chairs",
                "description": "A set of three chairs and a designer table for the living room.",
                "price": 150.00,
            },
            {
                "image": "deps/images/goods/set of tea table and two chairs.jpg",
                "name": "Tea table and two chairs",
                "description": "A set of a table and two chairs in a minimalist style.",
                "price": 93.00,
            },
            {
                "image": "deps/images/goods/double bed.jpg",
                "name": "Double bed",
                "description": "A double bed with a headboard, highly orthopedic and comfortable.",
                "price": 670.00,
            },
            {
                "image": "deps/images/goods/kitchen table.jpg",
                "name": "Kitchen table with sink",
                "description": "A kitchen dining table with a built-in sink and chairs.",
                "price": 365.00,
            },
            {
                "image": "deps/images/goods/kitchen table 2.jpg",
                "name": "Kitchen table with built-in units",
                "description": "A kitchen table with a built-in stove and sink. Lots of shelves and a beautiful design.",
                "price": 430.00,
            },
            {
                "image": "deps/images/goods/corner sofa.jpg",
                "name": "Corner sofa for living room",
                "description": "A corner sofa that unfolds into a double bed, perfect for the living room and guests.",
                "price": 610.00,
            },
            {
                "image": "deps/images/goods/bedside table.jpg",
                "name": "Bedside table",
                "description": "Bedside table with two drawers (flower not included).",
                "price": 55.00,
            },
            {
                "image": "deps/images/goods/sofa.jpg",
                "name": "Regular sofa",
                "description": "A regular sofa, nothing special to describe.",
                "price": 190.00,
            },
            {
                "image": "deps/images/goods/office chair.jpg",
                "name": "Office chair",
                "description": "A chair, very comfortable, but after all it’s just a chair.",
                "price": 30.00,
            },
            {
                "image": "deps/images/goods/plants.jpg",
                "name": "Plant",
                "description": "A plant to decorate your interior, adding freshness and serenity to the atmosphere.",
                "price": 10.00,
            },
            {
                "image": "deps/images/goods/flower.jpg",
                "name": "Stylized flower",
                "description": "A designer flower (possibly artificial) to decorate your interior.",
                "price": 15.00,
            },
            {
                "image": "deps/images/goods/strange table.jpg",
                "name": "Bedside table",
                "description": "A rather unusual-looking table, suitable for placement next to the bed.",
                "price": 25.00,
            },
        ],
    }

    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/products.html")
